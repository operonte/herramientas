"""Generador de folletos (HTML -> PDF con Chrome) al estilo de Bitacora/presentacion."""
import base64, html, io, math, os, re, subprocess, tempfile
from pathlib import Path
from PIL import Image
import segno

SP = Path('/home/cristian/X/Github/herramientas/folletos/work')
ROOT = Path('/home/cristian/X/Github')
FONTS_CSS = (SP / 'fonts' / 'fonts.css').read_text().replace("url('", "url('file://" + str(SP / 'fonts') + "/")
GROUP_URL = 'https://groups.google.com/g/tech-club---acceso-anticipado-gratis'
PORTFOLIO = 'cristianbravo-dev.web.app'
DEFAULT_SUB = 'Acceso anticipado **gratis**, en pocos minutos. Ahora mismo la app está en **fase de prueba cerrada**: hace falta un paso extra antes de que Google Play te deje instalarla.'


# ---------- utilidades ----------
def autocrop(src, name, margin=0.05, max_ar=0.8):
    """Recorta el fondo vacío alrededor del contenido (para capturas con mucho margen)."""
    from PIL import ImageChops
    im = Image.open(src).convert('RGB')
    bg = im.getpixel((6, 6))
    diff = ImageChops.difference(im, Image.new('RGB', im.size, bg)).convert('L').point(lambda p: 255 if p > 22 else 0)
    x0, y0, x1, y1 = diff.getbbox()
    w, h = im.size
    mx, my = int((x1 - x0) * margin), int((y1 - y0) * margin)
    x0, x1, y0, y1 = max(0, x0 - mx), min(w, x1 + mx), max(0, y0 - my), min(h, y1 + my)
    cw, ch = x1 - x0, y1 - y0
    if cw / ch > max_ar:                      # demasiado ancha: agrega alto para dar forma de teléfono
        need = int(cw / max_ar)
        extra = need - ch
        y0 = max(0, y0 - extra // 2)
        y1 = min(h, y0 + need)
        y0 = max(0, y1 - need)
    out = SP / 'img' / f'{name}.png'
    out.parent.mkdir(exist_ok=True)
    im.crop((x0, y0, x1, y1)).save(out)
    return str(out)



def esc(t):
    return html.escape(t, quote=False)


def md(t):
    """**negrita** y ==acento== sobre texto escapado."""
    t = esc(t)
    t = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', t)
    t = re.sub(r'==(.+?)==', r'<span class="hl">\1</span>', t)
    return t


def uri(path, maxw=760, kind='jpg', q=90):
    im = Image.open(path)
    if im.mode in ('RGBA', 'LA', 'P'):
        im = im.convert('RGBA')
        if kind == 'jpg':
            bg = Image.new('RGB', im.size, (255, 255, 255))
            bg.paste(im, mask=im.split()[3])
            im = bg
    else:
        im = im.convert('RGB')
    if im.width > maxw:
        im = im.resize((maxw, round(im.height * maxw / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    if kind == 'jpg':
        im.save(buf, 'JPEG', quality=q, optimize=True)
        return 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode()
    im.save(buf, 'PNG', optimize=True)
    return 'data:image/png;base64,' + base64.b64encode(buf.getvalue()).decode()


def qr_uri(url, dark):
    q = segno.make(url, error='m', micro=False)
    return q.svg_data_uri(scale=10, border=1, dark=dark, light='#ffffff')


def url_html(url):
    t = re.sub(r'^https?://', '', url).rstrip('/')
    t = esc(t)
    for ch in ('/', '?', '&', '=', '.'):
        t = t.replace(ch, ch + '<wbr>')
    return t


def short(url):
    return re.sub(r'^https?://', '', url).rstrip('/')


CSS = r"""
@page { size: 210mm 297mm; margin: 0 }
*{box-sizing:border-box;margin:0;padding:0}
html,body{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'Nunito Sans',sans-serif;color:var(--ink);background:var(--bg);font-size:10pt;line-height:1.45}
.page{width:210mm;height:297mm;position:relative;overflow:hidden;background:var(--bg);break-after:page;page-break-after:always}
.page:last-child{break-after:auto;page-break-after:auto}
h1,h2,h3,.serif{font-family:'Fraunces',serif}
a{color:inherit;text-decoration:none}
b{font-weight:800}
.hl{color:var(--accent);font-weight:800}
/* portada */
.hero{height:72mm;background:linear-gradient(135deg,var(--dark),var(--mid));color:#fff;position:relative;overflow:hidden;padding:0 16mm}
.hero .c1{position:absolute;right:-22mm;top:-34mm;width:100mm;height:100mm;border-radius:50%;background:rgba(255,255,255,.10)}
.hero .c2{position:absolute;right:26mm;bottom:-46mm;width:84mm;height:84mm;border-radius:50%;background:rgba(255,255,255,.07)}
.hero-inner{position:relative;display:flex;align-items:center;gap:9mm;height:100%}
.appicon{width:33mm;height:33mm;border-radius:7.4mm;box-shadow:0 2mm 6mm rgba(0,0,0,.30);flex:none;background:transparent;object-fit:cover}
.hero h1{font-size:37pt;font-weight:700;line-height:1.04;letter-spacing:-.01em}
.hero p{font-size:13pt;margin-top:3mm;opacity:.96;line-height:1.35;max-width:118mm}
.body{height:182mm;padding:9mm 16mm 9mm;display:flex;flex-direction:column;justify-content:space-between}
.intro{font-size:11.2pt;line-height:1.55;color:var(--ink)}
.cards{display:grid;gap:6mm}
.cards.c1col{grid-template-columns:1fr}.cards.c2col{grid-template-columns:1fr 1fr}
.card{background:#fff;border:.3mm solid var(--line);border-radius:5mm;padding:7mm 7mm 6mm}
.card h3{font-size:14.5pt;color:var(--dark);margin-bottom:4mm}
.card ul{list-style:none}
.card li{position:relative;padding-left:6.5mm;font-size:9.4pt;line-height:1.4;margin-bottom:2.6mm}
.card li::before{content:"";position:absolute;left:0;top:1.5mm;width:2.6mm;height:2.6mm;border-radius:50%;background:var(--mid)}
.card.alt li::before{background:var(--accent)}
.c1col ul{columns:2;column-gap:8mm}.c1col li{break-inside:avoid}
.values{display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;text-align:center}
.values b{display:block;font-size:9pt;color:var(--dark);margin-bottom:1mm}
.values span{font-size:8.2pt;color:var(--mute);display:block;line-height:1.35}
.cta{position:absolute;left:0;right:0;bottom:0;height:43mm;background:var(--dark);color:#fff;padding:0 16mm;display:flex;align-items:center;justify-content:space-between;gap:10mm}
.cta h3{font-size:17pt;margin-bottom:2mm}
.cta p{font-size:9pt;opacity:.92;max-width:88mm;line-height:1.4}
.cta .links{text-align:right;font-size:9pt}
.cta .links div{margin-bottom:2.6mm}
.cta .links b{display:block;font-size:9.6pt}
.cta .links small{display:block;opacity:.78;font-size:7.8pt}
/* bandas */
.band{height:36mm;background:linear-gradient(120deg,var(--dark),var(--mid));color:#fff;padding:8.5mm 16mm 0;position:relative;overflow:hidden}
.band::after{content:"";position:absolute;right:-18mm;top:-30mm;width:80mm;height:80mm;border-radius:50%;background:rgba(255,255,255,.09)}
.kicker{font-size:7.4pt;letter-spacing:.24em;text-transform:uppercase;font-weight:800;opacity:.92}
.band h2{font-size:19.5pt;font-weight:700;margin-top:1.5mm;line-height:1.15;position:relative}
.band p{font-size:9.6pt;opacity:.94;margin-top:1.5mm;max-width:172mm;line-height:1.35;position:relative}
.foot{position:absolute;left:0;right:0;bottom:0;height:11mm;background:var(--dark);color:#fff;display:flex;align-items:center;justify-content:space-between;padding:0 16mm;font-size:7.8pt}
.foot .serif{font-weight:700;font-size:9pt;margin-right:1.5mm}
/* galería */
.gal{position:absolute;left:0;right:0;top:36mm;bottom:11mm;padding:8mm 16mm;display:flex;align-items:center}
.grid{display:grid;width:100%;grid-template-columns:repeat(var(--cols),1fr);gap:var(--gapy) 6mm;align-content:center}
.shot{width:100%;height:var(--imgh);border-radius:4.6mm;overflow:hidden;background:#fff;box-shadow:0 .8mm 3.5mm rgba(0,0,0,.20);border:.3mm solid rgba(0,0,0,.10)}
.shot img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
figure figcaption{margin-top:2.2mm;font-size:7.8pt;line-height:1.3;color:var(--mute)}
figure figcaption b{display:block;font-family:'Fraunces',serif;font-size:9.2pt;color:var(--dark);font-weight:700;margin-bottom:.4mm}
/* guía */
.guide{position:absolute;left:0;right:0;top:36mm;bottom:11mm;padding:8mm 16mm 6mm;display:flex;flex-direction:column;justify-content:space-between}
.steps{display:grid;grid-template-columns:repeat(var(--cols),1fr);gap:7mm 6mm;flex:1;align-content:center}
.step .head{display:flex;gap:2.6mm;align-items:flex-start;margin-bottom:2mm}
.num{flex:none;width:7.4mm;height:7.4mm;border-radius:50%;background:var(--mid);color:#fff;font-weight:800;font-size:10pt;display:flex;align-items:center;justify-content:center;font-family:'Nunito Sans'}
.step h3{font-size:11.2pt;color:var(--dark);line-height:1.18;padding-top:.6mm}
.step p{font-size:8.6pt;line-height:1.4;color:var(--ink);margin-bottom:3mm;min-height:var(--ptxt)}
.tips{display:grid;grid-template-columns:repeat(3,1fr);gap:7mm;margin-top:5mm;padding-top:5mm;border-top:.3mm solid var(--line)}
.tips b{display:block;font-family:'Fraunces',serif;font-size:10pt;color:var(--dark);margin-bottom:1mm}
.tips span{font-size:8.4pt;color:var(--mute);line-height:1.4;display:block}
.steps.side{grid-template-columns:1fr 1fr;gap:8mm 8mm}
.step.side{display:flex;gap:5mm;align-items:flex-start}
.step.side .shot{width:42mm;height:93.4mm;flex:none}
.step.side .txt{flex:1;padding-top:1mm}
.step.side .head{margin-bottom:2.5mm}
.step.side h3{font-size:12.4pt}
.step.side p{font-size:9.2pt;line-height:1.45;min-height:0}
.step.side .num{margin-top:.4mm}
.tsteps{display:grid;grid-template-columns:1fr 1fr;gap:8mm;flex:1;align-content:center}
.tstep{display:flex;gap:5mm;background:#fff;border:.3mm solid var(--line);border-radius:5mm;padding:10mm 8mm;align-items:flex-start;box-shadow:0 1mm 4mm rgba(0,0,0,.05);min-height:52mm}
.tstep .num{width:12mm;height:12mm;font-size:15pt;margin-top:.5mm}
.tstep h3{font-size:15pt;color:var(--dark);margin-bottom:2.5mm;line-height:1.2}
.tstep p{font-size:10.6pt;line-height:1.55;color:var(--ink)}
/* instalación */
.inst{position:absolute;left:0;right:0;top:36mm;bottom:11mm;padding:10mm 16mm 4mm;display:flex;flex-direction:column;justify-content:space-between}
.two{display:grid;grid-template-columns:1fr 1fr;gap:7mm}
.two.one{grid-template-columns:1fr}
.big{background:#fff;border:.3mm solid var(--line);border-radius:6mm;padding:8mm;box-shadow:0 1mm 4mm rgba(0,0,0,.06)}
.big .num{width:9mm;height:9mm;font-size:12pt;margin-bottom:5mm}
.big h3{font-size:16pt;color:var(--dark);line-height:1.15;margin-bottom:3mm}
.big p{font-size:9.6pt;line-height:1.5;margin-bottom:5mm;min-height:24mm}
.qrrow{display:flex;gap:5mm;align-items:center}
.how{font-size:8.4pt;color:var(--mute);line-height:1.4;display:block}
.qr{width:36mm;height:36mm;flex:none;border-radius:2mm}
.qrrow small{font-size:7pt;letter-spacing:.16em;text-transform:uppercase;font-weight:800;color:var(--mute);display:block;margin-bottom:1.5mm}
.qrrow a{font-size:8.2pt;font-weight:800;color:var(--dark);line-height:1.35;display:block}
.urlbox{margin-top:4.5mm;padding-top:3.5mm;border-top:.3mm solid var(--line);font-size:7.6pt;font-weight:800;color:var(--dark);line-height:1.5}
.urlbox a{display:block}
.note{background:#fff;border:.3mm solid var(--line);border-radius:5mm;padding:5mm 7mm;font-size:9.4pt;line-height:1.5}
.sign{text-align:center}
.sign .appicon{width:19mm;height:19mm;border-radius:4.4mm;display:block;margin:0 auto 3mm}
.sign b{font-family:'Fraunces',serif;font-size:12pt;color:var(--dark)}
"""


def root_vars(c):
    return (":root{--dark:%s;--mid:%s;--accent:%s;--bg:%s;--ink:%s;--mute:%s;--line:%s}" %
            (c['dark'], c['mid'], c['accent'], c.get('bg', '#faf9f6'), c.get('ink', '#1d2621'),
             c.get('mute', '#5b655f'), c.get('line', '#e4e6e1')))


def foot(cfg, n, total):
    return (f'<div class="foot"><span><span class="serif">{esc(cfg["name"])}</span> — {esc(cfg["foot"])}</span>'
            f'<span>{PORTFOLIO} &nbsp;·&nbsp; {n} / {total}</span></div>')


def band(cfg, kicker, title, sub):
    return (f'<div class="band"><div class="kicker">{esc(cfg["name"])} · {esc(kicker)}</div>'
            f'<h2>{esc(title)}</h2><p>{md(sub)}</p></div>')


# ---------- páginas ----------
def page_cover(cfg, icon_uri, links_html, cta_title, cta_text):
    cards = cfg['cards']
    cls = 'c1col' if len(cards) == 1 else 'c2col'
    cards_html = ''.join(
        f'<div class="card{" alt" if i % 2 else ""}"><h3>{esc(c["title"])}</h3><ul>' +
        ''.join(f'<li>{md(x)}</li>' for x in c['items']) + '</ul></div>' for i, c in enumerate(cards))
    vals = ''.join(f'<div><b>{esc(v["title"])}</b><span>{md(v["text"])}</span></div>' for v in cfg['values'])
    return f'''<section class="page"><div class="hero"><i class="c1"></i><i class="c2"></i>
<div class="hero-inner"><img class="appicon" src="{icon_uri}"><div><h1>{esc(cfg["name"])}</h1><p>{md(cfg["tagline"])}</p></div></div></div>
<div class="body"><p class="intro">{md(cfg["intro"])}</p><div class="cards {cls}">{cards_html}</div><div class="values">{vals}</div></div>
<div class="cta"><div><h3 class="serif">{esc(cta_title)}</h3><p>{md(cta_text)}</p></div><div class="links">{links_html}</div></div></section>'''


def page_gallery(cfg, n, total):
    g = cfg['gallery']
    shots = g['shots']
    k = len(shots)
    cols = 3 if k <= 3 or k in (5, 6, 9) else 4
    rows = math.ceil(k / cols)
    avail = 297 - 36 - 11 - 16           # mm útiles
    gapy = 7
    cap = 15
    imgh = (avail - (rows - 1) * gapy - rows * cap) / rows
    colw = (210 - 32 - (cols - 1) * 6) / cols
    imgh = min(imgh, colw * 2.05)
    figs = ''.join(
        f'<figure><div class="shot"><img src="{uri(s["img"], 640)}"></div><figcaption><b>{esc(s["title"])}</b>{md(s["text"])}</figcaption></figure>'
        for s in shots)
    return (f'<section class="page">{band(cfg, g.get("kicker", "Así se ve"), g["title"], g["subtitle"])}'
            f'<div class="gal"><div class="grid" style="--cols:{cols};--imgh:{imgh:.1f}mm;--gapy:{gapy}mm">{figs}</div></div>'
            f'{foot(cfg, n, total)}</section>')


def page_guide(cfg, n, total):
    g = cfg['guide']
    steps = g['steps']
    k = len(steps)
    tips = g.get('tips', [])
    tips_html = ''
    if tips:
        tips_html = '<div class="tips">' + ''.join(f'<div><b>{esc(t["title"])}</b><span>{md(t["text"])}</span></div>' for t in tips) + '</div>'
    if all(not st.get('img') for st in steps):
        items = ''.join(
            f'<div class="tstep"><span class="num">{i + 1}</span><div><h3>{esc(st["title"])}</h3><p>{md(st["text"])}</p></div></div>'
            for i, st in enumerate(steps))
        body = f'<div class="tsteps">{items}</div>'
    elif k == 4:
        def sw(p):
            iw, ih = Image.open(p).size
            return min(93.4 * iw / ih, 45)
        items = ''.join(
            f'<div class="step side"><div class="shot" style="width:{sw(st["img"]):.1f}mm;height:{sw(st["img"]) * Image.open(st["img"]).size[1] / Image.open(st["img"]).size[0]:.1f}mm"><img src="{uri(st["img"], 640)}"></div><div class="txt"><div class="head"><span class="num">{i + 1}</span><h3>{esc(st["title"])}</h3></div>'
            f'<p>{md(st["text"])}</p></div></div>' for i, st in enumerate(steps))
        body = f'<div class="steps side">{items}</div>'
    else:
        cols = k if k <= 3 else 3
        rows = math.ceil(k / cols)
        avail = 297 - 36 - 11 - 14 - (28 if tips else 0)
        gapy, head = 7, 30
        imgh = (avail - (rows - 1) * gapy - rows * head) / rows
        colw = (210 - 32 - (cols - 1) * 6) / cols
        imgh = min(imgh, colw * 2.22)
        items = ''.join(
            f'<div class="step"><div class="head"><span class="num">{i + 1}</span><h3>{esc(st["title"])}</h3></div>'
            f'<p>{md(st["text"])}</p><div class="shot"><img src="{uri(st["img"], 640)}"></div></div>'
            for i, st in enumerate(steps))
        body = f'<div class="steps" style="--cols:{cols};--imgh:{imgh:.1f}mm;--ptxt:10mm">{items}</div>'
    return (f'<section class="page">{band(cfg, g.get("kicker", "Cómo se usa"), g["title"], g["subtitle"])}'
            f'<div class="guide">{body}{tips_html}</div>'
            f'{foot(cfg, n, total)}</section>')


def page_install(cfg, icon_uri, n, total):
    ins = cfg['install']
    d = cfg['colors']['dark']
    if ins['mode'] == 'store':
        cards = f'''<div class="two">
<div class="big"><span class="num">1</span><h3 class="serif">Únete al grupo de testers</h3>
<p>Es el paso que habilita tu cuenta de Google para instalar la app mientras está en prueba cerrada. Es gratis y toma un minuto.</p>
<div class="qrrow"><img class="qr" src="{qr_uri(GROUP_URL, d)}"><div><small>Grupo de Google</small><span class="how">Escanea el código con la cámara o abre el enlace de abajo.</span></div></div><div class="urlbox"><a href="{GROUP_URL}">{url_html(GROUP_URL)}</a></div></div>
<div class="big"><span class="num">2</span><h3 class="serif">Instala desde Google Play</h3>
<p>Con la ==misma cuenta de Google== con la que te uniste al grupo, abre este enlace e instala como cualquier otra app.</p>
<div class="qrrow"><img class="qr" src="{qr_uri(ins["play"], d)}"><div><small>Google Play</small><span class="how">Escanea el código con la cámara o abre el enlace de abajo.</span></div></div><div class="urlbox"><a href="{ins["play"]}">{url_html(ins["play"])}</a></div></div></div>'''.replace('<p>Con la ==misma cuenta de Google== con la que te uniste al grupo, abre este enlace e instala como cualquier otra app.</p>', '<p>Con la <span class="hl">misma cuenta de Google</span> con la que te uniste al grupo, abre este enlace e instala como cualquier otra app.</p>')
        note = '<div class="note"><span class="hl">¿Ya ves la app directo en Google Play, sin unirte a ningún grupo?</span> Entonces ya salió de prueba cerrada: ve directo al paso 2, el enlace es el mismo.</div>'
        tip_list = [{'title': 'Misma cuenta, los dos pasos', 'text': 'Si te unes al grupo con una cuenta de Google e instalas con otra, Google Play no mostrará la app como disponible.'},
                    {'title': ins.get('tip2_title', 'Gratis y sin registro extra'), 'text': ins.get('tip2', 'Solo necesitas tu cuenta de Google y un celular Android.')},
                    {'title': '¿Dudas o comentarios?', 'text': ins.get('contact', f'Conoce más proyectos en {PORTFOLIO}.')}]
    else:  # repo
        rl = ins['repo'] + ('/releases/latest' if ins.get('release') else '')
        cards = f'''<div class="two one"><div class="big"><span class="num">{esc(ins.get("icon", "↓"))}</span><h3 class="serif">{esc(ins.get("title", "Descárgala desde GitHub"))}</h3>
<p>{md(ins["text"])}</p>
<div class="qrrow"><img class="qr" src="{qr_uri(rl, d)}"><div><small>{"Última versión (APK)" if ins.get("release") else "Repositorio en GitHub"}</small><span class="how">Escanea el código con la cámara o abre el enlace de abajo.</span></div></div><div class="urlbox"><a href="{rl}">{url_html(rl)}</a></div></div></div>'''
        note = f'<div class="note">{md(ins["note"])}</div>' if ins.get('note') else ''
        tip_list = ins['tips']
    tips = '<div class="tips" style="border:0;margin:0;padding:0">' + ''.join(f'<div><b>{esc(t["title"])}</b><span>{md(t["text"])}</span></div>' for t in tip_list) + '</div>'
    return (f'<section class="page">{band(cfg, "Cómo instalarla" if ins["mode"] == "store" else "Cómo obtenerla", ins.get("title_page", "Instálala en tu celular"), ins.get("sub_page", DEFAULT_SUB))}'
            f'<div class="inst">{cards}{note}{tips}<div class="sign"><img class="appicon" src="{icon_uri}"><b>{esc(ins.get("closing", "Nos vemos adentro."))}</b></div></div>'
            f'{foot(cfg, n, total)}</section>')


def build_html(cfg):
    icon_uri = uri(cfg['icon'], 320, 'png')
    ins = cfg.get('install')
    mode = ins['mode'] if ins else 'none'
    # enlaces del CTA en portada
    links = ''
    if mode == 'store':
        links += f'<div><b>Google Play</b><a href="{ins["play"]}">{short(ins["play"])}</a><small>Prueba cerrada · antes únete al grupo de testers</small></div>'
        if ins.get('repo'):
            links += f'<div><b>Código abierto</b><a href="{ins["repo"]}">{short(ins["repo"])}</a></div>'
        cta_title, cta_text = cfg['cta']['title'], cfg['cta']['text']
    elif mode == 'repo':
        rl = ins['repo'] + ('/releases/latest' if ins.get('release') else '')
        links += f'<div><b>GitHub</b><a href="{rl}">{short(rl)}</a><small>{"Descarga el APK en Releases" if ins.get("release") else "Código y documentación"}</small></div>'
        cta_title, cta_text = cfg['cta']['title'], cfg['cta']['text']
    else:
        cta_title, cta_text = cfg['cta']['title'], cfg['cta']['text']
    links += f'<div><b>{PORTFOLIO}</b><small>Más proyectos de Cristian Bravo</small></div>'
    pages = [('cover',)]
    if cfg.get('gallery'):
        pages.append(('gallery',))
    if cfg.get('guide'):
        pages.append(('guide',))
    if mode in ('store', 'repo'):
        pages.append(('install',))
    total = len(pages)
    out = []
    for i, (p,) in enumerate(pages, 1):
        if p == 'cover':
            out.append(page_cover(cfg, icon_uri, links, cta_title, cta_text))
        elif p == 'gallery':
            out.append(page_gallery(cfg, i, total))
        elif p == 'guide':
            out.append(page_guide(cfg, i, total))
        else:
            out.append(page_install(cfg, icon_uri, i, total))
    return (f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>{esc(cfg["name"])} — Folleto</title>'
            f'<style>{FONTS_CSS}\n{root_vars(cfg["colors"])}\n{CSS}</style></head><body>{"".join(out)}</body></html>')


def chrome(args):
    return subprocess.run(['google-chrome', '--headless=new', '--disable-gpu', '--no-sandbox', '--hide-scrollbars',
                           '--no-pdf-header-footer', '--allow-file-access-from-files'] + args,
                          capture_output=True, text=True, timeout=180)


def render_pdf(html_path, pdf_path):
    r = chrome([f'--print-to-pdf={pdf_path}', '--virtual-time-budget=8000', f'file://{html_path}'])
    if not Path(pdf_path).exists():
        raise RuntimeError('Chrome no generó el PDF: ' + r.stderr[-400:])


def render_png(html_path, png_path, w, h):
    r = chrome([f'--screenshot={png_path}', f'--window-size={w},{h}', '--virtual-time-budget=8000', '--default-background-color=00000000',
                f'file://{html_path}'])
    if not Path(png_path).exists():
        raise RuntimeError('Chrome no generó la imagen: ' + r.stderr[-400:])
    im = Image.open(png_path).convert('RGB')      # sin canal alfa (requisito de Play)
    im.save(png_path, 'PNG', optimize=True)


def feature_html(cfg, icon_uri):
    c = cfg['colors']
    chips = ''.join(f'<span>{esc(x)}</span>' for x in cfg.get('chips', []))
    return f'''<!doctype html><html><head><meta charset="utf-8"><style>{FONTS_CSS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1024px;height:500px;overflow:hidden;font-family:'Nunito Sans',sans-serif;background:linear-gradient(120deg,{c['dark']},{c['mid']});color:#fff;position:relative}}
.c1{{position:absolute;right:-90px;top:-110px;width:420px;height:420px;border-radius:50%;background:rgba(255,255,255,.10)}}
.c2{{position:absolute;right:190px;bottom:-190px;width:340px;height:340px;border-radius:50%;background:rgba(255,255,255,.07)}}
.in{{position:relative;display:flex;align-items:center;gap:52px;height:100%;padding:0 84px}}
img{{width:230px;height:230px;border-radius:52px;box-shadow:0 14px 40px rgba(0,0,0,.35);flex:none;object-fit:cover}}
h1{{font-family:'Fraunces',serif;font-size:82px;line-height:1.02;font-weight:700;letter-spacing:-.01em}}
p{{font-size:31px;margin-top:16px;line-height:1.28;opacity:.96;max-width:580px;text-wrap:balance}}
.chips{{margin-top:26px;display:flex;gap:12px;flex-wrap:wrap}}
.chips span{{background:rgba(255,255,255,.17);border-radius:30px;padding:7px 18px;font-size:19px;font-weight:700}}
</style></head><body><i class="c1"></i><i class="c2"></i><div class="in"><img src="{icon_uri}"><div><h1>{esc(cfg['name'])}</h1><p>{esc(cfg.get('feature_tagline', cfg['tagline_plain']))}</p><div class="chips">{chips}</div></div></div></body></html>'''
