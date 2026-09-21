R = '/home/cristian/X/Github/'
E = '/home/cristian/X/Github/herramientas/folletos/work/emu/shots/sos_'
REAL = R + 'portfolio/capturas/sosapp/Screenshot_20260630-225331_SOS App.png'
CFG = {
 'slug': 'sosapp', 'name': 'SOS App', 'project_dir': 'sosapp',
 'tagline': 'Tu botón de pánico familiar: con un toque, tu familia recibe tu alerta y tu ubicación en tiempo real.',
 'tagline_plain': 'Protección familiar en tiempo real',
 'chips': ['Botón SOS', 'Mapa en vivo', 'Chat familiar'],
 'foot': 'protección familiar en tiempo real',
 'colors': {'dark': '#141733', 'mid': '#33418A', 'accent': '#D32F2F', 'bg': '#f8f8fc', 'ink': '#161a2e', 'mute': '#5a5e78', 'line': '#e3e3ef'},
 'icon_prep': {'src': '/home/cristian/X/Github/herramientas/folletos/work/img/sos_icon_src.png'},
 'feature_src': None,
 'capturas': [E+'a1.png', E+'a2.png', E+'a3.png', E+'a4.png', E+'a5.png', E+'c1_auth.png', REAL],
 'intro': 'SOS App es una **app de protección familiar**. Creas un grupo con las personas que quieres cuidar y, si ocurre una emergencia, presionas un botón: tu familia recibe la alerta con tu ubicación en tiempo real, puede ver cómo llegar a ti y coordinarse por el chat del grupo.',
 'cards': [
  {'title': 'Cómo te cuida', 'items': [
    '**Botón de pánico**: con un toque, tu familia recibe tu alerta',
    'Suena una **alarma**, incluso en modo No Molestar, y se comparte tu ubicación',
    '**Mapa en vivo**: tu familia ve tu ubicación moverse y cómo llegar a ti',
    '**Chat de emergencia** dentro del grupo, para coordinarse',
    'Botón «Estoy a salvo» para cerrar la alerta cuando pasa el peligro',
    'Un mensaje de emergencia que se envía junto con tu ubicación']},
  {'title': 'Pensada para familias', 'items': [
    'Crea un grupo familiar y comparte un **código de invitación de 6 dígitos**',
    'Puedes pertenecer a más de un grupo y alertarlos a todos',
    'Guarda tus **contactos de emergencia**',
    'Funciona en segundo plano, con la guía de permisos para activarlo bien',
    'Tu ubicación solo se comparte cuando activas el SOS, y solo con tu grupo familiar',
    'Ingreso con tu cuenta de Google']},
 ],
 'values': [
  {'title': 'Con un toque', 'text': 'Un solo botón para pedir ayuda.'},
  {'title': 'En tiempo real', 'text': 'Ubicación y chat mientras dura la alerta.'},
  {'title': 'Solo con tu familia', 'text': 'Tu ubicación nunca se comparte con terceros.'}],
 'cta': {'title': 'Conócela', 'text': 'SOS App aún no está en Google Play. Puedes descargar su versión para Android desde GitHub.'},
 'guide': {'title': 'Cómo funciona, paso a paso', 'subtitle': 'Pantallas de la app: desde crear tu grupo hasta pedir ayuda.',
  'steps': [
   {'title': 'Crea tu grupo familiar', 'text': 'Crea un grupo y comparte el código de invitación de 6 dígitos. Todos los miembros se cuidan entre sí.', 'img': E+'a2.png'},
   {'title': 'Activa el botón SOS', 'text': 'En una emergencia, presiona el botón: suena una alarma, incluso en modo No Molestar, y se comparte tu ubicación.', 'img': REAL},
   {'title': 'Tu familia te ve en el mapa', 'text': 'Tu familia ve tu ubicación moverse en el mapa, cómo llegar a ti, y se coordina por el chat del grupo.', 'img': E+'a4.png'},
   {'title': 'Tu privacidad importa', 'text': 'Tu ubicación solo se comparte cuando activas el SOS y solo con tu grupo familiar. Nunca con terceros.', 'img': E+'a5.png'}],
  'tips': [
   {'title': 'Ingreso con Google', 'text': 'Entras con tu cuenta de Google; no hay contraseñas nuevas que recordar.'},
   {'title': 'Permisos', 'text': 'La app te guía para activar ubicación, batería, notificaciones y No Molestar, y así funcione en segundo plano.'},
   {'title': 'Cerrar la alerta', 'text': 'Cuando pasa el peligro, cualquiera del grupo puede marcar que la persona está a salvo.'}]},
 'install': {'mode': 'repo', 'repo': 'https://github.com/operonte/sosapp', 'release': True,
  'title': 'Descarga la versión para Android', 'title_page': 'Cómo obtenerla', 'sub_page': 'SOS App todavía no está publicada en Google Play. La versión más reciente para Android está disponible en GitHub.',
  'text': 'Abre el enlace desde tu celular Android y descarga el archivo **APK** de la versión más reciente. Al instalarlo, Android puede pedirte permiso para **instalar apps de este origen**: es un paso normal cuando una app no viene de Google Play.',
  'note': 'Después de instalarla, la app te guiará para **activar los permisos** (ubicación, notificaciones y No Molestar) que necesita para funcionar bien en una emergencia.',
  'tips': [
   {'title': 'Solo Android', 'text': 'Esta versión es para celulares Android.'},
   {'title': 'Ingreso con Google', 'text': 'Necesitas una cuenta de Google para entrar.'},
   {'title': 'Código abierto', 'text': 'El código está publicado en el mismo repositorio de GitHub.'}],
  'closing': 'Cuidarnos entre todos.'},
}
