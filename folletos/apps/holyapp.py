R = '/home/cristian/X/Github/'
H = '/home/cristian/X/Github/herramientas/folletos/work/emu/shots/holy_'
P = R + 'Holyapp/dist/playstore/'
CFG = {
 'slug': 'holyapp', 'name': 'HolyApp', 'project_dir': 'Holyapp',
 'tagline': 'Trivia bíblica y teológica con el método de fallo y corrección.',
 'tagline_plain': 'Trivia bíblica y teológica · método de fallo y corrección',
 'chips': ['7 niveles', 'Sin conexión', 'Explicación y citas'],
 'foot': 'trivia bíblica y teológica',
 'colors': {'dark': '#3F2E7A', 'mid': '#6A4FB6', 'accent': '#B7791F', 'bg': '#faf8ff', 'ink': '#1e1a2e', 'mute': '#5f5a73', 'line': '#e6e0f4'},
 'icon_prep': {'src': P + 'icon-512.png'},
 'feature_src': P + 'feature-graphic-1024x500.png',
 'capturas': [H+'a1_welcome.png', H+'b1_home.png', H+'c1_question.png', H+'c2_wrong.png', H+'c3_correct.png', H+'c4_exit.png', H+'d1_results.png', H+'e1_home_score.png', H+'e2_review.png', H+'f1_settings.png', H+'g1_dark_home.png'],
 'intro': 'HolyApp es una trivia para **aprender la Biblia y la teología jugando**. Respondes preguntas por niveles y, si fallas, la app te muestra la respuesta correcta con su explicación y sus citas bíblicas, y te vuelve a preguntar hasta que la aprendes.',
 'cards': [
  {'title': 'Cómo se aprende', 'items': [
    '**7 niveles**, de Entrada a Evangelista, con casi 300 preguntas',
    'Tu nivel desbloquea en cascada todos los niveles inferiores',
    'Si fallas, la pregunta **vuelve al final** hasta que la aciertes',
    'Tras cada respuesta ves una explicación y las citas bíblicas',
    'Historial de respuestas correctas y de preguntas para repasar',
    'Tests de 10 o 20 preguntas, o modo infinito']},
  {'title': 'A tu ritmo', 'items': [
    'Puntaje según el nivel: de **1 a 5 puntos** por acierto al primer intento',
    'Funciona **sin conexión**: las preguntas viven en tu celular',
    'Puedes jugar como invitado, sin crear cuenta',
    'Con tu cuenta de Google guardas tu progreso y entras al ranking global',
    'Modo claro u oscuro, sonidos y vibración al responder',
    'Elige si las preguntas pueden repetirse o verlas una sola vez']},
 ],
 'values': [
  {'title': 'Aprende de cada error', 'text': 'Cada fallo trae su explicación y sus citas.'},
  {'title': 'Sin conexión', 'text': 'Juega donde quieras, sin internet.'},
  {'title': 'Para todos los niveles', 'text': 'Desde lo básico hasta la teología.'}],
 'cta': {'title': 'Pruébala ahora', 'text': 'Está en prueba cerrada en Google Play: únete al grupo de testers e instálala en tu celular en un par de minutos.'},
 'gallery': {'kicker': 'Así se ve', 'title': 'La app, pantalla por pantalla', 'subtitle': 'Pantallas de HolyApp en funcionamiento, jugando como invitado: sin datos inventados ni retoques.',
  'shots': [
   {'img': H+'a1_welcome.png', 'title': 'Bienvenida', 'text': 'Una guía rápida explica los niveles y el método.'},
   {'img': H+'b1_home.png', 'title': 'Inicio', 'text': 'Elige el largo del test; tu puntaje siempre a la vista.'},
   {'img': H+'c1_question.png', 'title': 'Pregunta', 'text': 'Cuatro alternativas y una sola correcta.'},
   {'img': H+'c2_wrong.png', 'title': 'Aprende del error', 'text': 'Ves la respuesta correcta y las citas para corregir.'},
   {'img': H+'c3_correct.png', 'title': 'Acierto', 'text': 'Explicación y citas para entender el porqué.'},
   {'img': H+'d1_results.png', 'title': 'Resultados', 'text': 'Aciertos, puntos ganados y preguntas por repasar.'},
   {'img': H+'e2_review.png', 'title': 'Repasar', 'text': 'Tus preguntas falladas, con su respuesta.'},
   {'img': H+'g1_dark_home.png', 'title': 'Modo oscuro', 'text': 'La app sigue el tema de tu celular.'}]},
 'guide': {'title': 'Cómo se usa, paso a paso', 'subtitle': 'De abrir la app a terminar tu primer test.',
  'steps': [
   {'title': 'Elige cuánto jugar', 'text': 'En el inicio escoge un test de 10 o 20 preguntas, o el modo infinito, y toca «Comenzar test».', 'img': H+'b1_home.png'},
   {'title': 'Responde', 'text': 'Lee la pregunta y toca la alternativa que creas correcta. Cada acierto al primer intento suma puntos.', 'img': H+'c1_question.png'},
   {'title': 'Aprende con cada respuesta', 'text': 'Si te equivocas, verás la respuesta correcta con sus citas y la pregunta volverá más adelante hasta que la aciertes.', 'img': H+'c2_wrong.png'},
   {'title': 'Revisa tu avance', 'text': 'Al terminar ves tus puntos. En «Repasar» quedan las preguntas que fallaste, para estudiarlas.', 'img': H+'d1_results.png'}],
  'tips': [
   {'title': 'Siete niveles', 'text': 'De Entrada a Evangelista. Tu nivel incluye los inferiores, y cada nivel da más puntos por acierto.'},
   {'title': 'Sin conexión', 'text': 'Las preguntas están en tu celular, así que puedes jugar sin internet.'},
   {'title': 'Ranking opcional', 'text': 'Inicia sesión con Google desde Configuración para guardar tu progreso. También puedes jugar como invitado.'}]},
 'install': {'mode': 'store', 'play': 'https://play.google.com/store/apps/details?id=com.holyapp.holyapp',
  'tip2_title': 'Juega como invitado', 'tip2': 'No necesitas iniciar sesión para jugar: el login con Google es opcional.',
  'closing': 'A aprender jugando.'},
}
