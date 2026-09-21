# herramientas

Utilidades internas para preparar el material de presentación de mis apps y
alimentar el portafolio.

| Script | Para qué sirve |
| --- | --- |
| [`folletos/`](folletos/) | Genera la carpeta `presentacion/` de cada app: ícono, gráfico destacado, capturas y un folleto en PDF con la guía de uso y los enlaces de descarga. |
| [`portfolio_assets.py`](portfolio_assets.py) | Lleva ese material al portafolio: íconos, banners, miniaturas en WebP, fichas en PDF y los códigos QR. |
| [`build_demos.sh`](build_demos.sh) | Compila las demos web (Flutter) de algunas apps y las deja en `portfolio/public/demo/`. |
| [`github-perfil/`](github-perfil/) | Borrador del README del perfil de GitHub. |

## Requisitos

    pip install pillow segno        # y Google Chrome instalado (genera los PDF)

## Uso

    cd folletos && python3 build.py <app>     # p. ej. python3 build.py fast
    python3 portfolio_assets.py               # regenera todo lo del portafolio
    bash build_demos.sh [slug ...]            # sin argumentos, compila todas

Los scripts asumen que los repositorios de las apps son carpetas hermanas de
esta, bajo `/home/cristian/X/Github/`.

`folletos/work/` guarda archivos intermedios (tipografías, recortes, capturas
del emulador, vistas previas) y no se versiona: se regenera solo.
