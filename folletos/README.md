# Generador de folletos (carpetas `presentacion/`)

Genera, para cada app, la carpeta `<proyecto>/presentacion/` con:
`icono-512.png`, `grafico-destacado-1024x500.png`, `capturas/` y `<app>-folleto.pdf`
(portada, guía de uso y cómo instalarla), con el diseño del folleto de Bitácora.

## Requisitos
    pip install pillow segno        # y Google Chrome instalado (genera el PDF)

## Uso
    python3 build.py <app>          # p. ej. python3 build.py fast
    python3 build.py <app> --no-pdf # solo imágenes

La configuración de cada app (textos, colores, enlaces, capturas) está en `apps/<app>.py`.
Para actualizar un folleto: edita ese archivo (o cambia las capturas) y vuelve a ejecutar.

## Notas
- `work/emu/shots` guarda las capturas hechas con la app corriendo en Chrome (tamaño celular).
  `work/img` guarda recortes/emblemas derivados. `work/fonts` guarda las tipografías del PDF.
- Apps sin capturas (`'capturas': []`): el folleto usa "Cómo funciona" en texto. Al agregar
  capturas, pon las rutas en `capturas` y en `guide.steps[*].img` y se regenera con imágenes.
- Los enlaces de descarga: Google Play + grupo de testers si la app está en la tienda;
  si no, el repositorio de GitHub (solo si es público). Sin enlace si no aplica.
- Textos en español de Chile (tuteo, sin voseo).
