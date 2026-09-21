from PIL import Image, ImageFilter
R = '/home/cristian/X/Github/'
SPD = '/home/cristian/X/Github/herramientas/folletos/work/img/'
PC = R + 'portfolio/capturas/misionapp/Screenshot_20260630-'
S = R + 'misionapp/store_assets/'

def blur_names(src, out):
    """Desenfoca los nombres de personas (datos sensibles); deja intacta el resto de la interfaz."""
    im = Image.open(src).convert('RGB')
    for (y0, y1) in [(715, 850), (958, 1095), (1208, 1348)]:
        box = (225, y0, 640, y1)
        im.paste(im.crop(box).filter(ImageFilter.GaussianBlur(16)), box)
    im.save(out)
    return out

LIST_LIGHT = blur_names(PC + '225215_misionapp.png', SPD + 'mision_list_light.png')
LIST_DARK = blur_names(PC + '225233_misionapp.png', SPD + 'mision_list_dark.png')
SETTINGS = PC + '225239_misionapp.png'

CFG = {
 'slug': 'misionapp', 'name': 'MisionApp', 'project_dir': 'misionapp',
 'tagline': 'Registro de personas y visitas para misioneros, organizado por grupos.',
 'tagline_plain': 'Registro para misioneros',
 'chips': ['Personas y visitas', 'Por grupos', 'Con Google'],
 'foot': 'registro para misioneros',
 'colors': {'dark': '#155E75', 'mid': '#3AA8C4', 'accent': '#0E8F6A', 'bg': '#f3fafc', 'ink': '#10262e', 'mute': '#50666e', 'line': '#d6eaf0'},
 'icon_prep': {'src': S + 'icon_512_play.png', 'black_to_alpha': True},
 'feature_src': S + 'feature_graphic_1024x500_play.png',
 'capturas': [LIST_LIGHT, LIST_DARK, SETTINGS],
 'intro': 'MisionApp ayuda a los misioneros a **llevar el registro de las personas que acompañan y de cada visita**, organizados por grupos de misión. Todo queda ordenado en un solo lugar y se puede buscar, filtrar y consultar cuando haga falta.',
 'cards': [
  {'title': 'Para misioneros', 'items': [
    'Registrar a cada persona con sus datos y su **grupo de misión**',
    'Anotar cada visita con su **fecha y su contenido**',
    'Buscar por nombre o dirección',
    'Ordenar por nombre, última visita o complejidad',
    'Filtrar quién quiere recibir visitas y quién lleva más de 30 o 60 días sin ellas',
    'Sin internet, seguir viendo los últimos datos guardados']},
  {'title': 'Para líderes y administradores', 'items': [
    '**Estadísticas**: visitas totales, personas por grupo y personas nunca visitadas',
    'Ver la distribución de complejidad (del 1 al 7)',
    '**Exportar a Excel** todo el registro',
    'Grupos de misión validados: cada persona entra con el nombre de su grupo',
    'Cuatro temas de color, incluido uno oscuro',
    'Política de privacidad y términos de uso dentro de la app']},
 ],
 'values': [
  {'title': 'Por grupos', 'text': 'Cada misionero ve el trabajo de su propio grupo.'},
  {'title': 'Ingreso con Google', 'text': 'Sin contraseñas nuevas que recordar.'},
  {'title': 'Todo registrado', 'text': 'Cada visita queda con su fecha y su contenido.'}],
 'cta': {'title': 'Pruébala ahora', 'text': 'Está en prueba cerrada en Google Play: únete al grupo de testers e instálala en tu celular en un par de minutos.'},
 'guide': {'title': 'Cómo se usa, paso a paso', 'subtitle': 'De entrar con Google a tener a tu grupo ordenado.',
  'steps': [
   {'title': 'Entra y arma tu perfil', 'text': 'Entra con tu cuenta de Google. En Ajustes escribe tu nombre, tus apellidos y tu grupo de misión (el nombre te lo confirma tu líder).', 'img': SETTINGS},
   {'title': 'Mira a las personas de tu grupo', 'text': 'En «Personas» ves a quienes acompañas. Busca, ordena y filtra por última visita, complejidad o quién quiere visitas.', 'img': LIST_LIGHT},
   {'title': 'Agrega y elige tu tema', 'text': 'Con el botón «+» sumas a una persona nueva. Y en Ajustes eliges el tema: Celeste, Verde, Rosado o el oscuro «Tech».', 'img': LIST_DARK}],
  'tips': [
   {'title': 'Registra cada visita', 'text': 'Al abrir a una persona ves su historial y puedes sumar visitas con su fecha y su contenido.'},
   {'title': 'Sin internet', 'text': 'Si no hay conexión, la app muestra los últimos datos guardados.'},
   {'title': 'Para administradores', 'text': 'Ven las estadísticas del registro y pueden exportarlo a Excel.'}]},
 'install': {'mode': 'store', 'play': 'https://play.google.com/store/apps/details?id=com.operonte.misionapp',
  'tip2_title': 'Ingreso con Google', 'tip2': 'Entras con tu cuenta de Google. El nombre de tu grupo de misión te lo confirma tu líder.',
  'closing': 'Buen trabajo en la misión.'},
}
