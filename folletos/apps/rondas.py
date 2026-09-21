R = '/home/cristian/X/Github/'
CFG = {
 'slug': 'rondas', 'name': 'Control de Rondas', 'project_dir': 'Rondas',
 'tagline': 'Rondas de seguridad con check-in por NFC, QR y GPS, y una central que las supervisa.',
 'tagline_plain': 'Rondas de seguridad con NFC, QR y GPS',
 'chips': ['NFC · QR · Manual', 'Con o sin conexión', 'Central de supervisión'],
 'foot': 'rondas de seguridad móviles',
 'colors': {'dark': '#0F2A33', 'mid': '#12909A', 'accent': '#C77700', 'bg': '#f3f9f9', 'ink': '#0f1f24', 'mute': '#4c6167', 'line': '#d5e7e8'},
 'icon_prep': {'src': R + 'Rondas/web/icons/Icon-512.png', 'inset': 0.11},
 'feature_src': None,
 'capturas': [],
 'intro': 'Control de Rondas es un sistema para que los **guardias registren sus rondas desde el celular** y para que una **central de supervisión** vea cómo van. Cada punto de la ronda se marca con NFC, código QR o de forma manual, con la ubicación del guardia, y todo queda registrado aunque no haya internet.',
 'cards': [
  {'title': 'Para guardias', 'items': [
    'Ingresan con su contraseña personal y eligen la **instalación** donde harán la ronda',
    'Marcan cada punto de control con **NFC**, **código QR** o de forma manual, con foto opcional',
    'Cada check-in queda registrado con la **ubicación GPS**',
    'Reciben las verificaciones de ronda que pide la central y confirman su recepción',
    'La app avisa cuando la batería está baja o en nivel crítico',
    'Funciona **con o sin conexión**: lo pendiente se sincroniza cuando vuelve internet']},
  {'title': 'Para supervisores', 'items': [
    'Crean y administran **guardias e instalaciones**, con contraseñas seguras generadas por la app',
    'Ven en un **mapa** la última posición de cada guardia',
    'Revisan el registro de rondas y check-ins (NFC, QR o manual), con búsqueda',
    'Activan un **chequeo aleatorio** para verificar que los guardias estén atentos',
    'Pueden cerrar sesiones de guardias y cambiar contraseñas',
    'Advertencia si se detecta un GPS falso; datos cifrados en el dispositivo']},
 ],
 'values': [
  {'title': 'NFC, QR o manual', 'text': 'Tres formas de marcar cada punto de la ronda.'},
  {'title': 'Con o sin conexión', 'text': 'Los registros pendientes se envían solos después.'},
  {'title': 'Central de supervisión', 'text': 'Mapa, registros y alertas en un solo lugar.'}],
 'cta': {'title': 'Conócela', 'text': 'Control de Rondas aún no está en Google Play. Puedes descargar su versión para Android desde GitHub.'},
 'guide': {'kicker': 'Cómo funciona', 'title': 'Cómo funciona, paso a paso', 'subtitle': 'De la contraseña del guardia a la supervisión de la ronda.',
  'steps': [
   {'title': 'Ingresa', 'text': 'El guardia entra a «Control de Rondas» con su contraseña personal. La central crea y administra esas contraseñas.'},
   {'title': 'Elige la instalación', 'text': 'Selecciona el lugar donde hará la ronda y escribe la contraseña de esa instalación para comenzar.'},
   {'title': 'Marca cada punto', 'text': 'En cada punto de control hace el check-in con NFC, código QR o de forma manual, con foto si lo necesita. Queda registrado con su ubicación.'},
   {'title': 'La central supervisa', 'text': 'La central ve el mapa, los registros y las alertas, y puede pedir una verificación aleatoria que el guardia debe confirmar.'}],
  'tips': [
   {'title': 'Sin conexión', 'text': 'Si no hay internet, los registros se guardan en el celular y se envían cuando vuelve la conexión.'},
   {'title': 'Alertas', 'text': 'La app avisa por batería baja y por las verificaciones que solicita la central.'},
   {'title': 'Android y web', 'text': 'Funciona como app Android y también en el navegador; el escaneo de QR es solo en el celular.'}]},
 'install': {'mode': 'repo', 'repo': 'https://github.com/operonte/Rondas', 'release': True,
  'title': 'Descarga la versión para Android', 'title_page': 'Cómo obtenerla', 'sub_page': 'Control de Rondas todavía no está publicada en Google Play. La versión más reciente para Android está disponible en GitHub.',
  'text': 'Abre el enlace desde tu celular Android y descarga el archivo **APK** de la versión más reciente. Al instalarlo, Android puede pedirte permiso para **instalar apps de este origen**: es un paso normal cuando una app no viene de Google Play.',
  'note': 'Guardias y supervisores reciben sus contraseñas de quien administra el sistema: la app no tiene registro abierto.',
  'tips': [
   {'title': 'Solo Android', 'text': 'La versión descargable es para celulares Android. También existe una versión web.'},
   {'title': 'Contraseñas', 'text': 'Cada guardia y cada instalación tienen su propia contraseña.'},
   {'title': 'Código abierto', 'text': 'El código está publicado en el mismo repositorio de GitHub.'}],
  'closing': 'Rondas bien hechas.'},
}
