R = '/home/cristian/X/Github/'
E = '/home/cristian/X/Github/herramientas/folletos/work/emu/shots/fast_'
I = '/home/cristian/X/Github/herramientas/folletos/work/img/fast_'
CFG = {
 'slug': 'fast', 'name': 'fasT', 'project_dir': 'fast',
 'tagline': 'Abre WhatsApp al instante desde cualquier número de teléfono.',
 'tagline_plain': 'Abre WhatsApp al instante desde un número',
 'chips': ['Historial y favoritos', 'Modo oscuro', 'Hecha para Chile'],
 'foot': 'abre WhatsApp al instante',
 'colors': {'dark': '#1E4D2B', 'mid': '#2E9E4F', 'accent': '#C26A00', 'bg': '#f6faf6', 'ink': '#14211a', 'mute': '#56655b', 'line': '#dfe9df'},
 'icon_prep': {'src': R + 'fast/assets/icon.png', 'inset': 0.19},
 'feature_src': None,
 'capturas': [E+'a1.png', E+'a2.png', E+'a3.png', E+'b1_home.png', E+'b2_typed.png', E+'b4_history.png', E+'c1_settings.png', E+'c2_message.png', E+'d1_dark_home.png'],
 'intro': 'fasT te ahorra pasos: escribes o pegas un número de teléfono y **abres la conversación en WhatsApp al instante**, sin tener que agregar a nadie a tus contactos. Está pensada para Chile: agrega el código +56 por ti y valida que el número sea de un celular.',
 'cards': [
  {'title': 'Qué hace', 'items': [
    'Abre una conversación de WhatsApp a partir de un número de teléfono',
    'Agrega el código de Chile (**+56**) automáticamente si falta',
    'Valida que sea un celular chileno de 9 dígitos',
    'Botón **Pegar** para traer el número desde el portapapeles',
    'Guarda un **historial** de los últimos números que usaste',
    'Marca tus contactos frecuentes con una estrella y déjalos en **Favoritos**']},
  {'title': 'A tu manera', 'items': [
    'Modo claro, oscuro o el mismo de tu celular',
    'Mensaje inicial opcional, que se rellena solo en WhatsApp',
    'Guía de bienvenida que puedes volver a ver cuando quieras',
    'Limpia tu historial o tus favoritos con un toque',
    'Política de privacidad, términos de uso y contacto dentro de la app',
    'Sin cuentas ni registros: la abres y la usas']},
 ],
 'values': [
  {'title': 'Pensada para Chile', 'text': 'Agrega el +56 y valida celulares de 9 dígitos.'},
  {'title': 'Un número, un toque', 'text': 'De escribirlo a la conversación, sin vueltas.'},
  {'title': 'Tus datos, en tu celular', 'text': 'El historial y los favoritos se guardan en tu dispositivo.'}],
 'cta': {'title': 'Pruébala ahora', 'text': 'Está en prueba cerrada en Google Play: únete al grupo de testers e instálala en tu celular en un par de minutos.'},
 'guide': {'title': 'Cómo se usa, paso a paso', 'subtitle': 'De abrir la app a estar conversando en WhatsApp, en cuatro pasos.',
  'steps': [
   {'title': 'Abre la app', 'text': 'La primera vez verás una guía de tres pantallas. Puedes volver a verla desde Configuración.', 'img': E+'a1.png'},
   {'title': 'Escribe el número', 'text': 'Escríbelo o pégalo. Si no pones el código de país, la app agrega el 56 de Chile y te muestra cómo quedará.', 'img': I+'b2_typed_crop.png'},
   {'title': 'Abre WhatsApp', 'text': 'Toca «Abrir WhatsApp». Los números que usas quedan en el historial y, con la estrella, en Favoritos.', 'img': I+'b4_history_crop.png'},
   {'title': 'Ajusta la app', 'text': 'Elige modo claro u oscuro, deja un mensaje inicial o limpia tu historial y tus favoritos.', 'img': E+'c1_settings.png'}],
  'tips': [
   {'title': 'Mensaje inicial', 'text': 'Deja un texto que se rellena solo al abrir la conversación, por ejemplo un saludo.'},
   {'title': 'Modo oscuro', 'text': 'Sigue el modo de tu celular o elígelo tú desde Configuración.'},
   {'title': 'Todo en tu celular', 'text': 'Tu historial y tus favoritos se guardan en tu dispositivo, sin crear cuenta.'}]},
 'install': {'mode': 'store', 'play': 'https://play.google.com/store/apps/details?id=com.operonte.fast',
  'tip2_title': 'Sin registro', 'tip2': 'fasT no pide crear cuenta: la abres, escribes un número y listo.',
  'closing': 'Un número, un toque.'},
}
