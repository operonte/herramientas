#!/usr/bin/env python3
"""Uso: build.py <slug> [--no-pdf | --solo-pdf]   (lee apps/<slug>.py con CFG).

--solo-pdf: regenera únicamente el PDF, usando el ícono y las capturas que ya existen en presentacion/
(no toca icono-512.png, el gráfico destacado ni capturas/).
"""
import importlib, subprocess, sys
from pathlib import Path
from PIL import Image
sys.path.insert(0, str(Path(__file__).parent))
import lib
from lib import ROOT, SP


def prep_icon(src, out, inset=0.0, bg=None, black_to_alpha=False):
    im = Image.open(src).convert('RGBA')
    if black_to_alpha:
        px = im.load()
        for y in range(im.height):
            for x in range(im.width):
                r, g, b, a = px[x, y]
                if r < 14 and g < 14 and b < 14:
                    px[x, y] = (r, g, b, 0)
    if inset:
        w, h = im.size
        d = int(w * inset)
        im = im.crop((d, d, w - d, h - d))
    if bg:
        base = Image.new('RGBA', im.size, bg)
        base.alpha_composite(im)
        im = base
    im.resize((512, 512), Image.LANCZOS).save(out, 'PNG', optimize=True)


def prep_feature(src, out):
    im = Image.open(src).convert('RGB')
    w, h = im.size
    if (w, h) != (1024, 500):
        target = 1024 / 500
        if w / h > target:                      # demasiado ancha: recorta a los lados
            nw = round(h * target)
            x = (w - nw) // 2
            im = im.crop((x, 0, x + nw, h))
        else:
            nh = round(w / target)
            y = (h - nh) // 2
            im = im.crop((0, y, w, y + nh))
        im = im.resize((1024, 500), Image.LANCZOS)
    im.save(out, 'PNG', optimize=True)


def render(slug, cfg, pres):
    """Genera el folleto PDF en presentacion/ y sus vistas previas."""
    build = SP / 'build'
    build.mkdir(exist_ok=True)
    hp = build / f'{slug}.html'
    hp.write_text(lib.build_html(cfg))
    pdf = pres / f'{slug}-folleto.pdf'
    lib.render_pdf(str(hp), str(pdf))
    prev = SP / 'preview'
    prev.mkdir(exist_ok=True)
    for f in prev.glob(f'{slug}-*.png'):
        f.unlink()
    subprocess.run(['pdftoppm', '-r', '75', '-png', str(pdf), str(prev / slug)], check=True)
    info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout
    pages = [l for l in info.splitlines() if l.startswith('Pages')][0]
    print(f'{slug}: PDF OK — {pages.strip()} — {pdf.stat().st_size // 1024} KB — previews en {prev}')


def main():
    slug = sys.argv[1]
    cfg = importlib.import_module(f'apps.{slug}').CFG
    proj = ROOT / cfg['project_dir']
    assert proj.is_dir(), proj
    pres = proj / 'presentacion'
    if cfg['capturas']:
        (pres / 'capturas').mkdir(parents=True, exist_ok=True)
    else:
        pres.mkdir(parents=True, exist_ok=True)
    if '--solo-pdf' in sys.argv:
        cfg['icon'] = str(pres / 'icono-512.png')
        render(slug, cfg, pres)
        print('carpeta:', pres)
        return
    # 1) ícono
    ic = cfg['icon_prep']
    prep_icon(ic['src'], pres / 'icono-512.png', ic.get('inset', 0.0), ic.get('bg'), ic.get('black_to_alpha', False))
    cfg['icon'] = str(pres / 'icono-512.png')
    # 2) gráfico destacado
    build = SP / 'build'
    build.mkdir(exist_ok=True)
    if cfg.get('feature_src'):
        prep_feature(cfg['feature_src'], pres / 'grafico-destacado-1024x500.png')
    else:
        hp = build / f'{slug}_feature.html'
        hp.write_text(lib.feature_html(cfg, lib.uri(cfg['icon'], 320, 'png')))
        lib.render_png(str(hp), str(pres / 'grafico-destacado-1024x500.png'), 1024, 500)
    # 3) capturas (PNG sin canal alfa, numeradas)
    for i, src in enumerate(cfg['capturas'], 1):
        Image.open(src).convert('RGB').save(pres / 'capturas' / f'{i:02d}.png', 'PNG', optimize=True)
    # 4) folleto PDF
    if '--no-pdf' not in sys.argv:
        render(slug, cfg, pres)
    print('carpeta:', pres)


if __name__ == '__main__':
    main()
