# Bitácora: se regenera con `python3 build.py bitacora --solo-pdf` (no toca icono, gráfico ni capturas).
# Se omiten las capturas 08 y 09 (perfil de la persona autora: datos personales) del folleto.
R = '/home/cristian/X/Github/'
C = R + 'Bitacora/presentacion/capturas/'
CFG = {
 'slug': 'bitacora', 'name': 'Bitácora', 'project_dir': 'Bitacora',
 'tagline': 'Tareas, notas, asistencia y reuniones — todo en un solo lugar.',
 'tagline_plain': 'Tareas, notas, asistencia y reuniones',
 'chips': ['Android · iOS · Linux · Web'],
 'foot': 'tareas, notas, asistencia y reuniones, todo en un solo lugar',
 'colors': {'dark': '#115E59', 'mid': '#26938A', 'accent': '#C2570C', 'bg': '#fafaf9', 'ink': '#1c1917', 'mute': '#57534e', 'line': '#e7e5e4'},
 # El ícono y el gráfico destacado ya existen: se apuntan a sí mismos para que una
 # corrida completa los reescriba igual en vez de generar unos nuevos y perder los reales.
 'icon_prep': {'src': R + 'Bitacora/presentacion/icono-512.png'},
 'feature_src': R + 'Bitacora/presentacion/grafico-destacado-1024x500.png',
 'capturas': [],
 'intro': 'Bitácora organiza la vida académica de un curso completo: cada estudiante ve sus propias tareas y las que comparte con su clase, y cada docente tiene un panel propio para evaluar, tomar asistencia y detectar a tiempo quién se está atrasando. Funciona para cualquier carrera o institución, sin configuración especial.',
 'cards': [
  {'title': 'Para estudiantes', 'items': [
    'Tareas propias y compartidas, separadas en Pendientes, Vencidas y Entregadas',
    'Recordatorios configurables para no llegar tarde a ninguna',
    'Notas y asistencia por asignatura, siempre a mano',
    'Reuniones de clase con acceso directo (Zoom, Meet y similares)',
    'Material de estudio compartido por tus docentes',
    'Funciona sin conexión y sincroniza solo']},
  {'title': 'Para docentes', 'items': [
    'Evalúa entregas, pon notas y deja comentarios desde el celular',
    'Asistencia por asignatura, con resumen de todo el curso',
    'Panel de riesgo: quién se atrasa en tareas o asistencia, a tiempo',
    'Asigna tareas oficiales, con archivos adjuntos si hace falta',
    'Anuncios para tu asignatura o para todo el curso',
    'Solo ves las asignaturas que realmente dictas']},
 ],
 'values': [
  {'title': 'Gratis, sin publicidad', 'text': 'Ninguna función queda detrás de un pago ni de un anuncio.'},
  {'title': 'Tus archivos, tuyos', 'text': 'Lo que subes queda en tu propio Google Drive, no en un servidor ajeno.'},
  {'title': 'Para cualquier institución', 'text': 'No viene atada a una carrera en particular: se adapta a la tuya.'}],
 'cta': {'title': 'Pruébala ahora', 'text': 'Sin registro previo ni tarjeta: entras con tu cuenta de Google y armas tu carrera en un par de minutos. Está en prueba cerrada en Google Play: únete al grupo de testers e instálala.'},
 'gallery': {'kicker': 'Así se ve', 'title': 'Capturas reales, del teléfono',
  'subtitle': 'Esta versión suma un perfil como el de una red social, muro y chat del curso, historias y estados, sin perder de vista para qué nació la app: que ninguna tarea se te escape.',
  'shots': [
   {'img': C+'01.png', 'title': 'Entras con Google', 'text': 'Sin crear otra contraseña: un toque y estás adentro.'},
   {'img': C+'02.png', 'title': 'Hoy', 'text': 'Lo urgente primero: vencidas y por vencer, arriba de todo.'},
   {'img': C+'03.png', 'title': 'Pendientes', 'text': 'Calendario del mes o lista, como prefieras.'},
   {'img': C+'04.png', 'title': 'Vencidas', 'text': 'Avisa clarito lo que quedó atrás.'},
   {'img': C+'05.png', 'title': 'Mis archivos', 'text': 'Ordenados por asignatura, en tu propio Drive.'},
   {'img': C+'06.png', 'title': 'Mis reuniones', 'text': 'Todo el mes de un vistazo, con acceso directo.'},
   {'img': C+'07.png', 'title': 'Material docente', 'text': 'Lo que comparten tus profes, por materia.'},
   {'img': C+'10.png', 'title': 'A tu manera', 'text': 'Mascota y vista de tareas, a elección.'},
   {'img': C+'11.png', 'title': 'Modo oscuro', 'text': 'Y paleta de colores, para cuidar la vista de noche.'}]},
 'install': {'mode': 'store', 'play': 'https://play.google.com/store/apps/details?id=com.operonte.bitacora',
  'repo': 'https://github.com/operonte/Bitacora',
  'tip2_title': 'Un curso, no una carrera', 'tip2': 'No hace falta que toda tu institución la use: parte con tu curso y suma gente después.',
  'contact': 'Código en github.com/operonte/Bitacora. También puedes probar primero sin instalar nada, en bitacora-2d643.web.app.',
  'closing': 'Nos vemos adentro.'},
}
