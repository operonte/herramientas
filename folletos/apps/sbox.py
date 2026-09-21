R = '/home/cristian/X/Github/'
S = R + 'sbox/Capturas_desde_celular/Screenshot_20260709-'
PC = '/home/cristian/X/Github/herramientas/folletos/work/img/sbox_pc.png'
WIDGET = R + 'portfolio/capturas/sbox/Screenshot_20260630-224852_Moto App Launcher.png'
CFG = {
 'slug': 'sbox', 'name': 'sbox', 'project_dir': 'sbox',
 'tagline': 'Portapapeles universal entre tu PC y tu Android, por la misma WiFi. Sin servidor y sin nube.',
 'tagline_plain': 'Portapapeles universal PC ↔ Android, por la misma WiFi',
 'chips': ['Sin cuentas', 'Sin nube', 'Directo por tu red'],
 'foot': 'portapapeles universal PC ↔ Android',
 'colors': {'dark': '#0B1020', 'mid': '#2456C7', 'accent': '#0E9F6E', 'bg': '#f6f8fc', 'ink': '#0f1729', 'mute': '#56627a', 'line': '#dfe5f1'},
 'icon_prep': {'src': R + 'sbox/app/assets/icon/sbox_icon.png'},
 'feature_src': None,
 'capturas': [PC, S+'200911_sbox.png', S+'200939_sbox.png', S+'200928_sbox.png', WIDGET, S+'200955_sbox.png'],
 'intro': 'sbox es un portapapeles universal entre tu **PC** y tu **celular Android**. Copias un texto o envías un archivo en un dispositivo y aparece al instante en el otro, directo por tu WiFi, sin crear cuentas y sin pasar por la nube.',
 'cards': [
  {'title': 'Qué puedes hacer', 'items': [
    'Pasar **texto y archivos** entre tu PC (Linux) y tu Android al instante',
    'Lo que copias en un dispositivo se manda solo al otro',
    'Enviar archivos con el botón del clip o con «Compartir» desde cualquier app',
    'Usar el **widget** en la pantalla de inicio del Android',
    'Tener a mano una caja flotante siempre visible en el escritorio',
    'Ajustar el tamaño del texto y decidir si el portapapeles se envía solo']},
  {'title': 'Simple y privado', 'items': [
    '**Sin servidor y sin nube**: los dispositivos hablan directo por tu red local',
    'Sin cuentas: los emparejas una sola vez con un **código de 6 dígitos**',
    'La próxima vez se conectan solos',
    'Lo que recibes queda guardado en la carpeta Descargas/sbox',
    'El portapapeles es efímero: solo guarda lo último que copiaste',
    'Política de privacidad a un toque, dentro de la app']},
 ],
 'values': [
  {'title': 'Sin cuentas', 'text': 'Emparejas con un código y listo.'},
  {'title': 'Solo tu red', 'text': 'Los datos viajan directo entre tus dispositivos.'},
  {'title': 'Al instante', 'text': 'Lo que copias aquí, listo para pegar allá.'}],
 'cta': {'title': 'Pruébala ahora', 'text': 'Está en prueba cerrada en Google Play: únete al grupo de testers e instala la app en tu Android. La versión para PC se descarga desde la propia app.'},
 'guide': {'title': 'Cómo se usa, paso a paso', 'subtitle': 'Conecta tu PC y tu celular una vez y olvídate de mandarte cosas por correo.',
  'steps': [
   {'title': 'Instálala en los dos', 'text': 'Instala sbox en tu Android. En «Cómo usar sbox» encuentras el enlace para descargar la versión de PC.', 'img': S+'200939_sbox.png'},
   {'title': 'Conéctalos con un código', 'text': 'Abre sbox en el PC: muestra un código de 6 dígitos. Escríbelo en el Android, con ambos en la misma WiFi.', 'img': PC},
   {'title': 'Copia y pega entre ellos', 'text': 'Lo que copias en un dispositivo se manda solo al otro. También puedes escribir o pegar y enviar.', 'img': S+'200911_sbox.png'},
   {'title': 'Envía archivos', 'text': 'Usa el botón del clip o «Compartir». Lo recibido queda en Descargas/sbox. El widget te deja usarlo desde el inicio.', 'img': WIDGET}],
  'tips': [
   {'title': 'Solo en tu WiFi', 'text': 'sbox no funciona por datos móviles ni entre redes distintas: los dos deben estar en la misma red.'},
   {'title': 'Se recuerdan', 'text': 'Tras el primer emparejamiento no vuelve a pedir el código, a menos que olvides el dispositivo desde Configuración.'},
   {'title': 'Si no aparece la PC', 'text': 'Escribe a mano la IP que muestra la cajita del PC en el campo bajo el código.'}]},
 'install': {'mode': 'store', 'play': 'https://play.google.com/store/apps/details?id=com.sbox.sbox',
  'tip2_title': 'Versión para PC', 'tip2': 'La app de escritorio (Linux) se descarga desde «Cómo usar sbox», dentro de la app. Windows llegará próximamente.',
  'closing': 'Tu PC y tu celular, en sintonía.'},
}
