from lib import autocrop
R = '/home/cristian/X/Github/'
L = R + 'toctocapp/store-listing/'
Z = {n: autocrop(L + 'capturas/' + f, n) for n, f in [('t1','01-login.png'),('t2','02-negocios-cerca.png'),('t3','03-catalogo.png'),('t4','04-carrito.png')]}
CFG = {
 'slug': 'toctocapp', 'name': 'Toc Toc', 'project_dir': 'toctocapp',
 'tagline': 'Pide y vende en los negocios de tu barrio, con pago protegido.',
 'tagline_plain': 'Pide y vende en los negocios de tu barrio',
 'chips': ['Pago protegido', 'Negocios cerca', 'Hecha en Chile'],
 'foot': 'compra y vende en tu barrio',
 'colors': {'dark': '#B23C12', 'mid': '#F56333', 'accent': '#2F7D32', 'bg': '#fff6ec', 'ink': '#2a1a12', 'mute': '#6f5a4b', 'line': '#f0dcc8'},
 'icon_prep': {'src': L + 'icono-512x512.png'},
 'feature_src': L + 'feature-graphic-1024x500.png',
 'capturas': [L+'capturas/01-login.png', L+'capturas/02-negocios-cerca.png', L+'capturas/03-catalogo.png', L+'capturas/04-carrito.png', L+'capturas/05-referidos.png'],
 'intro': 'Toc Toc te conecta con los negocios y personas de tu barrio: panaderías, almacenes, cafeterías y también servicios a domicilio como gasfitería, peluquería o clases particulares. **Compras con pago protegido** y, si vendes, recibes tus pagos directo en tu cuenta de Mercado Pago.',
 'cards': [
  {'title': 'Para quienes compran', 'items': [
    'Descubre negocios cerca de ti, con **distancia real** y horario de apertura',
    'Compra productos o agenda un servicio, pagando dentro de la app',
    'Sigue tu pedido y conversa por **chat** con quien te vende',
    'Tu pago queda protegido hasta que confirmas que recibiste lo tuyo',
    'Mira reseñas, insignias y el perfil del vendedor antes de comprar',
    'Reporta o haz un reclamo formal si algo no se resuelve conversando']},
  {'title': 'Para quienes venden', 'items': [
    'Activa tu negocio o tus servicios en minutos',
    '**Comisión transparente**: la ves siempre antes de publicar',
    'Recibe tus pagos directo en tu cuenta de Mercado Pago',
    'Verificación de identidad para que tus clientes compren con confianza',
    'Arma **paquetes** con tus productos a un precio combinado para mover stock',
    'Invita a tus amigos y súmalos a la comunidad de Toc Toc']},
 ],
 'values': [
  {'title': 'Pago protegido', 'text': 'Tu pago queda resguardado hasta que confirmas tu pedido.'},
  {'title': 'Comercio de barrio', 'text': 'Apoya a los negocios cercanos a tu casa.'},
  {'title': 'Confianza real', 'text': 'Reseñas reales: no se puede calificar la propia venta.'}],
 'cta': {'title': 'Pruébala ahora', 'text': 'Está en prueba cerrada en Google Play: únete al grupo de testers e instálala en tu celular en un par de minutos.'},
 'guide': {'title': 'Cómo se usa, paso a paso', 'subtitle': 'De abrir la app a tener tu pedido en camino.',
  'steps': [
   {'title': 'Elige qué quieres hacer', 'text': 'Entra con tu cuenta de Google y elige si hoy vienes a comprar o a vender.', 'img': Z['t1']},
   {'title': 'Descubre negocios cerca', 'text': 'Verás los negocios de tu barrio con su distancia, si están abiertos ahora y su categoría.', 'img': Z['t2']},
   {'title': 'Elige y agrega', 'text': 'Entra a un negocio, revisa su catálogo y agrega al carrito lo que necesitas.', 'img': Z['t3']},
   {'title': 'Revisa y paga', 'text': 'Confirma tu pedido y paga dentro de la app. Tu pago queda protegido hasta que lo recibes.', 'img': Z['t4']}],
  'tips': [
   {'title': 'Invita a tus amigos', 'text': 'Comparte tu código: cuando un amigo se suma y hace su primera compra, queda activo en tu lista.'},
   {'title': 'Si vendes', 'text': 'Necesitas verificar tu identidad y conectar tu cuenta de Mercado Pago para recibir tus pagos.'},
   {'title': '¿Algo salió mal?', 'text': 'Puedes reportar un producto o negocio, o iniciar un reclamo formal desde la app.'}]},
 'install': {'mode': 'store', 'play': 'https://play.google.com/store/apps/details?id=com.toctoc.toctoc_app',
  'tip2_title': 'Entrar es simple', 'tip2': 'Para comprar solo necesitas tu cuenta de Google. Para vender, además, verificar tu identidad.',
  'closing': 'Compra cerca, vende cerca.'},
}
