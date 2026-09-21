#!/usr/bin/env python3
"""Genera las imágenes que se ven al compartir el portafolio en WhatsApp, LinkedIn o X.

Produce `portfolio/public/og.png` (inglés) y `og-es.png` (español), 1200x630, con los
colores y la tipografía del sitio y los íconos reales de las apps.

Uso:  python3 og_portfolio.py
"""
import base64
import glob
import sys
from pathlib import Path

R = Path('/home/cristian/X/Github')
PUB = R / 'portfolio' / 'public'
sys.path.insert(0, str(R / 'herramientas' / 'folletos'))
import lib  # noqa: E402  (render_png: HTML -> PNG con Chrome)

# Los mismos tokens que src/styles/global.css
BG, SURFACE, TEXT, MUTED, ACCENT = '#0b0f17', '#131a28', '#e6ebf2', '#9aa7b8', '#34d399'

# Íconos que se muestran como prueba de trabajo (los de las apps publicadas en tiendas).
ICONOS = ['toctocapp', 'preciobencina', 'holyapp', 'horasmedicas', 'fast', 'coroapp', 'misionapp', 'sbox']

TEXTOS = {
    'en': dict(
        out='og.png',
        eyebrow='MOBILE &amp; FULL-STACK DEVELOPER',
        lead='Websites, apps, databases and <b>Power BI</b> for businesses',
        foot='16 products built end to end · Chile',
    ),
    'es': dict(
        out='og-es.png',
        eyebrow='DESARROLLADOR MOBILE &amp; FULL-STACK',
        lead='Páginas web, apps, bases de datos y <b>Power BI</b> para negocios',
        foot='16 productos propios, de punta a punta · Chile',
    ),
}


def data_uri(path, mime):
    return f'data:{mime};base64,' + base64.b64encode(Path(path).read_bytes()).decode()


def fuente(peso):
    """Toma la tipografía Inter del build de Astro, para que calce con el sitio."""
    hit = glob.glob(str(R / f'portfolio/dist/_astro/inter-latin-{peso}-normal.*.woff2'))
    assert hit, f'falta Inter {peso}: corre `npm run build` en portfolio/ primero'
    return data_uri(hit[0], 'font/woff2')


def html(t):
    caras = ''.join(
        f"@font-face{{font-family:Inter;font-weight:{p};font-style:normal;src:url({fuente(p)}) format('woff2')}}"
        for p in (400, 600, 800))
    iconos = ''.join(
        f'<img src="{data_uri(PUB / "projects/icons" / f"{s}.webp", "image/webp")}">' for s in ICONOS)
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>
{caras}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1200px;height:630px;background:{BG};font-family:Inter,sans-serif;color:{TEXT};
 position:relative;overflow:hidden}}
/* Mismo resplandor esmeralda que el hero del sitio */
.glow{{position:absolute;width:900px;height:900px;left:-220px;top:-380px;border-radius:50%;
 background:radial-gradient(circle,rgba(52,211,153,.20),transparent 62%)}}
.glow2{{position:absolute;width:700px;height:700px;right:-240px;bottom:-330px;border-radius:50%;
 background:radial-gradient(circle,rgba(52,211,153,.10),transparent 65%)}}
.in{{position:relative;padding:62px 70px;height:100%;display:flex;flex-direction:column}}
.top{{display:flex;align-items:center;gap:18px}}
.mark{{width:64px;height:64px;border-radius:16px;background:{ACCENT};color:{BG};font-weight:800;
 font-size:27px;display:flex;align-items:center;justify-content:center;letter-spacing:-.5px}}
.eyebrow{{font-size:16px;font-weight:600;letter-spacing:.17em;color:{ACCENT}}}
h1{{font-size:76px;font-weight:800;letter-spacing:-2.4px;margin-top:34px;line-height:1}}
.lead{{font-size:31px;font-weight:400;color:{MUTED};margin-top:20px;line-height:1.35;max-width:930px}}
.lead b{{color:{TEXT};font-weight:600}}
.rule{{height:1px;background:rgba(255,255,255,.10);margin-top:auto}}
.bot{{display:flex;align-items:center;justify-content:space-between;padding-top:26px}}
.icons{{display:flex;gap:11px}}
.icons img{{width:56px;height:56px;border-radius:13px;background:{SURFACE}}}
.right{{text-align:right}}
.foot{{font-size:18px;color:{MUTED}}}
.url{{font-size:21px;font-weight:600;color:{ACCENT};margin-top:5px}}
</style></head><body>
<div class="glow"></div><div class="glow2"></div>
<div class="in">
  <div class="top"><div class="mark">CB</div><div class="eyebrow">{t['eyebrow']}</div></div>
  <h1>Cristian Bravo</h1>
  <p class="lead">{t['lead']}</p>
  <div class="rule"></div>
  <div class="bot">
    <div class="icons">{iconos}</div>
    <div class="right"><div class="foot">{t['foot']}</div><div class="url">cristianbravo-dev.web.app</div></div>
  </div>
</div></body></html>'''


def main():
    tmp = lib.SP / 'build'
    tmp.mkdir(parents=True, exist_ok=True)
    for lang, t in TEXTOS.items():
        hp = tmp / f'og_{lang}.html'
        hp.write_text(html(t))
        out = PUB / t['out']
        lib.render_png(str(hp), str(out), 1200, 630)
        print(f'{t["out"]}: {out.stat().st_size // 1024} KB')


if __name__ == '__main__':
    main()
