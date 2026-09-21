R = '/home/cristian/X/Github/'
CFG = {
 'slug': 'acceso', 'name': 'Control de Acceso', 'project_dir': 'acceso',
 'tagline': 'Control de acceso vehicular y peatonal que sigue funcionando sin internet.',
 'tagline_plain': 'Control de acceso vehicular y peatonal',
 'chips': ['Personas y vehículos', 'Pases QR', 'Sin conexión'],
 'foot': 'control de acceso vehicular y peatonal',
 'colors': {'dark': '#0F172A', 'mid': '#0E9F6E', 'accent': '#2563EB', 'bg': '#f5f8fa', 'ink': '#0f172a', 'mute': '#526075', 'line': '#dde5ec'},
 'icon_prep': {'src': '/home/cristian/X/Github/herramientas/folletos/work/img/acceso_icon_src.png'},
 'feature_src': None,
 'capturas': [],
 'intro': 'Control de Acceso ayuda a los guardias de un recinto a **registrar quién entra y quién sale**, a pie o en vehículo. Funciona sin conexión: todo se guarda primero en el celular y se sincroniza con la nube cuando hay internet, así no se pierde información si la red falla en el punto de control.',
 'cards': [
  {'title': 'Para guardias', 'items': [
    'Registrar ingresos y salidas de **personas y vehículos**',
    'Escanear el **código QR** de una visita pre-autorizada',
    'Tomar una **foto** del ingreso como respaldo del registro',
    'Ver cuántas personas, vehículos, motos, camiones y bicicletas hay dentro',
    'Ver la duración de cada visita',
    'Seguir trabajando **sin internet**, sin perder registros']},
  {'title': 'Para la administración', 'items': [
    'Crear **visitas pre-autorizadas**, con destino y fechas, y generar pases QR',
    'Mantener una **lista negra** de personas o vehículos restringidos, con su motivo',
    '**Importar listas** desde archivos CSV (pre-autorizaciones y lista negra)',
    'Exportar los registros',
    'Tres niveles de acceso: **Administrador, Operador guardia y Vista cliente**',
    'Sincronización con la nube en segundo plano']},
 ],
 'values': [
  {'title': 'Sin conexión', 'text': 'Registra primero en el celular y sincroniza después.'},
  {'title': 'Pases QR', 'text': 'Ingreso rápido de visitas pre-autorizadas.'},
  {'title': 'Tres perfiles', 'text': 'Administración, guardia y cliente, cada uno con lo suyo.'}],
 'cta': {'title': 'Conócela', 'text': 'Control de Acceso aún no está en Google Play. Puedes descargar su versión para Android desde GitHub.'},
 'guide': {'kicker': 'Cómo funciona', 'title': 'Cómo funciona, paso a paso', 'subtitle': 'De iniciar el turno a tener el recinto bajo control.',
  'steps': [
   {'title': 'Inicia el turno', 'text': 'El guardia ingresa con la clave que le asignaron. La clave define qué puede hacer: administrar, operar como guardia o solo consultar.'},
   {'title': 'Registra los accesos', 'text': 'Anota el ingreso de personas y vehículos, con foto opcional, o escanea el código QR de una visita pre-autorizada.'},
   {'title': 'Controla lo que hay dentro', 'text': 'El panel muestra cuántas personas, vehículos, motos, camiones y bicicletas hay dentro del recinto en este momento.'},
   {'title': 'Administra las listas', 'text': 'La administración carga pre-autorizaciones y lista negra, a mano o importando un archivo CSV, y exporta los registros.'}],
  'tips': [
   {'title': 'Sin conexión', 'text': 'Los datos se guardan primero en el celular, así que el registro no se detiene si falla internet.'},
   {'title': 'Sincronización', 'text': 'Cuando vuelve la conexión, la app envía lo pendiente y recibe los cambios de otros puntos.'},
   {'title': 'Cada perfil, lo suyo', 'text': 'El administrador gestiona; el guardia registra y escanea; el cliente consulta y exporta.'}]},
 'install': {'mode': 'repo', 'repo': 'https://github.com/operonte/acceso', 'release': True,
  'title': 'Descarga la versión para Android', 'title_page': 'Cómo obtenerla', 'sub_page': 'Control de Acceso todavía no está publicada en Google Play. La versión más reciente para Android está disponible en GitHub.',
  'text': 'Abre el enlace desde tu celular Android y descarga el archivo **APK** de la versión más reciente. Al instalarlo, Android puede pedirte permiso para **instalar apps de este origen**: es un paso normal cuando una app no viene de Google Play.',
  'note': 'La clave de acceso de cada persona la entrega quien administra el sistema.',
  'tips': [
   {'title': 'Solo Android', 'text': 'Esta versión es para celulares Android.'},
   {'title': 'Cámara', 'text': 'Para escanear QR y tomar fotos, la app te pedirá permiso de cámara.'},
   {'title': 'Código abierto', 'text': 'El código está publicado en el mismo repositorio de GitHub.'}],
  'closing': 'Recintos bajo control.'},
}
