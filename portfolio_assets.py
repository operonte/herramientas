#!/usr/bin/env python3
"""Prepara los recursos del portafolio a partir de las carpetas <proyecto>/presentacion/.

Genera en portfolio/public/:
  projects/icons/<slug>.webp      ícono de la app (192 px)
  projects/banners/<slug>.webp    gráfico destacado (1024x500)
  projects/<slug>-N.webp          miniaturas (450 px de ancho)
  projects/full/<slug>-N.webp     capturas grandes (720 px de ancho)
  fichas/<slug>.pdf               folleto en PDF del proyecto
  qr/<slug>-store.svg | -apk.svg  QR para probar la app desde el celular; qr/tester.svg

Requisitos: pillow, segno.  Uso: python3 portfolio_assets.py
"""
import re, shutil, sys
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import segno

R = Path('/home/cristian/X/Github')
PUB = R / 'portfolio' / 'public'
sys.path.insert(0, str(R / 'herramientas' / 'folletos'))
import lib  # noqa: E402  (plantilla del folleto: feature graphic + autocrop)

GROUP = 'https://groups.google.com/g/tech-club---acceso-anticipado-gratis'
PLAY = 'https://play.google.com/store/apps/details?id='
STORE = {
    'preciobencina': PLAY + 'cl.preciobencina.preciobencina', 'holyapp': PLAY + 'com.holyapp.holyapp',
    'horasmedicas': PLAY + 'com.operonte.horasmedicas', 'coroapp': PLAY + 'com.operonte.coroapp.coroapp',
    'fast': PLAY + 'com.operonte.fast', 'misionapp': PLAY + 'com.operonte.misionapp',
    'sbox': PLAY + 'com.sbox.sbox', 'toctocapp': PLAY + 'com.toctoc.toctoc_app',
    'bitacora': PLAY + 'com.operonte.bitacora',
}
APK = {  # apps sin tienda cuyo repo público tiene APK en Releases
    'acceso': 'https://github.com/operonte/acceso/releases/latest',
    'rondas': 'https://github.com/operonte/Rondas/releases/latest',
    'licitaciones': 'https://github.com/operonte/licitaciones/releases/latest',
    'sosapp': 'https://github.com/operonte/sosapp/releases/latest',
}
# slug -> (carpeta, capturas [n° de presentacion/capturas, en orden; el 1.º es la portada], ¿autocrop?, ¿ficha?)
PROJ = {
    'toctocapp': ('toctocapp', [2, 3, 4, 5, 1], True, True),
    'preciobencina': ('preciobencina', [1, 2, 3, 4, 5], False, True),
    'holyapp': ('Holyapp', [8, 3, 4, 5, 7, 9, 11], False, True),
    'horasmedicas': ('horasmedicas', [1, 2, 3, 6, 4], False, True),
    'coroapp': ('coroapp', [4, 5, 1, 3, 6], False, True),
    'fast': ('fast', [6, 5, 1, 8, 9, 7], False, True),
    'misionapp': ('misionapp', [1, 2, 3], False, True),
    'sosapp': ('sosapp', [7, 1, 2, 3, 4, 5], False, True),
    'sbox': ('sbox', [1, 2, 5, 3, 4], False, True),
    'logos': ('logos', [1, 3, 5, 8, 9, 10, 13], False, True),
    'bitacora': ('Bitacora', [2, 3, 4, 6, 7, 11, 1], False, True),   # se omite la 9 (perfil con datos personales)
    'acceso': ('acceso', [], False, True),
    'rondas': ('Rondas', [], False, True),
    'licitaciones': ('Licitaciones', [], False, True),
}
EXTRA = {  # proyectos sin carpeta presentacion/: ícono y banner generados con la plantilla del folleto
    'transcripcion': dict(name='Live Subtitles', glyph='closed_caption', top=(91, 33, 182), bot=(30, 27, 75),
                          colors={'dark': '#1E1B4B', 'mid': '#6D28D9', 'accent': '#0E9F6E'},
                          plain='Real-time subtitles for anything you play on your PC', chips=['English → Spanish', '100% offline speech', 'Linux']),
    'categoriaaldia': dict(name='Categoría al Día', glyph='inventory_2', top=(22, 163, 74), bot=(20, 83, 45),
                           colors={'dark': '#14532D', 'mid': '#16A34A', 'accent': '#B7791F'},
                           plain='Inventory counts and barcodes, automated in Excel', chips=['Excel + VBA', '13,000+ items', 'Reports']),
}
ICONS_DART = Path('/home/cristian/snap/flutter/common/flutter/packages/flutter/lib/src/material/icons.dart')
ICON_FONT = '/home/cristian/snap/flutter/common/flutter/bin/cache/artifacts/material_fonts/MaterialIcons-Regular.otf'


def webp(im, out, w, q=84):
    im = im.convert('RGBA') if im.mode in ('RGBA', 'LA', 'P') else im.convert('RGB')
    if im.width > w:
        im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    out.parent.mkdir(parents=True, exist_ok=True)
    im.save(out, 'WEBP', quality=q, method=6)


def glyph_cp(name):
    m = re.search(r'static const IconData %s = IconData\(0x([0-9a-f]+)' % name, ICONS_DART.read_text())
    return int(m.group(1), 16)


def emblem(glyph, top, bot):
    S = 1024
    img = Image.new('RGB', (S, S))
    px = img.load()
    for y in range(S):
        t = y / (S - 1)
        c = tuple(int(top[i] * (1 - t) + bot[i] * t) for i in range(3))
        for x in range(S):
            px[x, y] = c
    f = ImageFont.truetype(ICON_FONT, 620)
    d = ImageDraw.Draw(img)
    g = chr(glyph_cp(glyph))
    bb = d.textbbox((0, 0), g, font=f)
    d.text(((S - bb[2] + bb[0]) // 2 - bb[0], (S - bb[3] + bb[1]) // 2 - bb[1]), g, font=f, fill=(255, 255, 255))
    return img


def qr(url, out):
    out.parent.mkdir(parents=True, exist_ok=True)
    segno.make(url, error='m').save(str(out), kind='svg', scale=8, border=1, dark='#0b0f17', light='#ffffff')


def main():
    work = R / 'herramientas' / 'folletos' / 'work'
    for slug, (d, caps, crop, ficha) in PROJ.items():
        pres = R / d / 'presentacion'
        webp(Image.open(pres / 'icono-512.png'), PUB / 'projects/icons' / f'{slug}.webp', 192, 92)
        webp(Image.open(pres / 'grafico-destacado-1024x500.png'), PUB / 'projects/banners' / f'{slug}.webp', 1024, 82)
        if caps is not None:
            for old in list((PUB / 'projects').glob(f'{slug}-*.webp')) + list((PUB / 'projects/full').glob(f'{slug}-*.webp')):
                old.unlink()
            for i, n in enumerate(caps, 1):
                src = pres / 'capturas' / f'{n:02d}.png'
                if crop:
                    src = Path(lib.autocrop(str(src), f'site_{slug}_{n}'))
                im = Image.open(src)
                webp(im, PUB / 'projects' / f'{slug}-{i}.webp', 450, 82)
                webp(im, PUB / 'projects/full' / f'{slug}-{i}.webp', 720, 86)
        if ficha:
            (PUB / 'fichas').mkdir(parents=True, exist_ok=True)
            shutil.copyfile(pres / f'{slug if slug != "toctocapp" else "toctocapp"}-folleto.pdf', PUB / 'fichas' / f'{slug}.pdf')
        print(f'{slug:14s} ok  capturas={0 if caps is None else len(caps)}  ficha={ficha}')
    for slug, e in EXTRA.items():
        em = emblem(e['glyph'], e['top'], e['bot'])
        tmp = work / 'img' / f'{slug}_icon_src.png'
        em.save(tmp)
        icon512 = em.resize((512, 512), Image.LANCZOS)
        icon_png = work / 'img' / f'{slug}_icon512.png'
        icon512.save(icon_png)
        cfg = dict(name=e['name'], colors={**e['colors'], 'bg': '#fff'}, tagline_plain=e['plain'], chips=e['chips'], icon=str(icon_png))
        html = work / 'build' / f'{slug}_feature_site.html'
        html.parent.mkdir(exist_ok=True)
        html.write_text(lib.feature_html(cfg, lib.uri(str(icon_png), 320, 'png')))
        banner = work / 'build' / f'{slug}_banner.png'
        lib.render_png(str(html), str(banner), 1024, 500)
        webp(icon512, PUB / 'projects/icons' / f'{slug}.webp', 192, 92)
        webp(Image.open(banner), PUB / 'projects/banners' / f'{slug}.webp', 1024, 82)
        print(f'{slug:14s} ok  (ícono y banner generados)')
    qr(GROUP, PUB / 'qr/tester.svg')
    for slug, url in STORE.items():
        qr(url, PUB / 'qr' / f'{slug}-store.svg')
    for slug, url in APK.items():
        qr(url, PUB / 'qr' / f'{slug}-apk.svg')
    print('QR:', len(list((PUB / 'qr').glob('*.svg'))), 'archivos')


if __name__ == '__main__':
    main()
