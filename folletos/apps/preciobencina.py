R = '/home/cristian/X/Github/'
P = R + 'preciobencina/play_store/'
CFG = {
 'slug': 'preciobencina', 'name': 'PrecioBencina', 'project_dir': 'preciobencina',
 'tagline': 'Encuentra la bencina más barata cerca de ti, con precios en vivo de la CNE.',
 'tagline_plain': 'Encuentra la bencina más barata cerca de ti',
 'chips': ['Precios en vivo · CNE Chile'],
 'foot': 'la bencina más barata cerca de ti',
 'colors': {'dark': '#C4500B', 'mid': '#FF7A30', 'accent': '#15803D', 'bg': '#fff8f1', 'ink': '#2b1d14', 'mute': '#6b5a4d', 'line': '#f1e1d2'},
 'icon_prep': {'src': P + 'icono/icono_512x512.png'},
 'feature_src': P + 'feature_graphic/feature_graphic_1024x500.png',
 'capturas': [P+'capturas/01_home_mapa.png', P+'capturas/02_lista.png', P+'capturas/04_filtros.png', P+'capturas/03_detalle.png', P+'capturas/05_acerca_de.png'],
 'intro': 'PrecioBencina te muestra en un mapa las bencineras cercanas y **cuánto cuesta el litro en cada una**, con precios que vienen directo de la Comisión Nacional de Energía (CNE). Elige tu combustible, compara por precio o por distancia y llega a la más conveniente con un toque.',
 'cards': [
  {'title': 'Qué puedes hacer', 'items': [
    'Ver en un mapa las bencineras cercanas y su precio por litro',
    'Destacar **la más barata** cerca de ti',
    'Filtrar por combustible: 93, 95, 97, Diésel, Parafina o GLP',
    'Ordenar por precio o por distancia',
    'Buscar una bencinera o una dirección para mirar otra zona',
    'Guardar tus bencineras favoritas con un toque']},
  {'title': 'Datos en que puedes confiar', 'items': [
    'Precios en vivo desde la **API oficial de la CNE**, organismo del Estado de Chile',
    'Cada precio indica cuándo se actualizó',
    'Sin conexión, muestra el último dato guardado en tu celular',
    '«Cómo llegar» abre tu app de mapas',
    'El GPS se usa solo en tu dispositivo, para mostrar lo cercano',
    'Preguntas frecuentes y enlaces para reclamos (SEC, SERNAC, ChileAtiende)']},
 ],
 'values': [
  {'title': 'Fuente oficial', 'text': 'Precios que cada bencinera declara a la CNE.'},
  {'title': 'Abre y usa', 'text': 'No hay registro ni cuenta que crear.'},
  {'title': 'Para todo Chile', 'text': 'Bencineras de todo el país registradas en la CNE.'}],
 'cta': {'title': 'Pruébala ahora', 'text': 'Está en prueba cerrada en Google Play: únete al grupo de testers e instálala en tu celular en un par de minutos.'},
 'guide': {'title': 'Cómo se usa, paso a paso', 'subtitle': 'De abrir la app a llegar a la bencinera más conveniente.',
  'steps': [
   {'title': 'Abre la app', 'text': 'Verás el mapa con las bencineras cercanas y sus precios. La más barata aparece destacada.', 'img': P+'capturas/01_home_mapa.png'},
   {'title': 'Compara precios', 'text': 'En «Lista» las estaciones aparecen ordenadas, con su precio, su distancia y cuándo se actualizó cada una.', 'img': P+'capturas/02_lista.png'},
   {'title': 'Filtra por combustible', 'text': 'Elige 93, 95, 97, Diésel, Parafina o GLP, y decide si ordenas por precio o por cercanía.', 'img': P+'capturas/04_filtros.png'},
   {'title': 'Elige y llega', 'text': 'Toca una estación para ver su precio y su ubicación. «Cómo llegar» abre tu app de mapas.', 'img': P+'capturas/03_detalle.png'}],
  'tips': [
   {'title': 'Busca otra zona', 'text': 'Escribe una bencinera o una dirección en el buscador para ver precios en otro lugar.'},
   {'title': 'Preguntas frecuentes', 'text': 'En «Acerca de» encuentras de dónde vienen los datos y cada cuánto se actualizan.'},
   {'title': 'Si algo no cuadra', 'text': 'La app incluye enlaces para hacer un reclamo ante la SEC o el SERNAC.'}]},
 'install': {'mode': 'store', 'play': 'https://play.google.com/store/apps/details?id=cl.preciobencina.preciobencina',
  'tip2_title': 'Sin registro', 'tip2': 'No necesitas crear una cuenta dentro de la app: la abres y ya puedes comparar precios.',
  'closing': 'Buen viaje y buen precio.'},
}
