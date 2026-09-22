#!/usr/bin/env bash
# Borra del historial de git (ramas Y ETIQUETAS) los secretos y los APK versionados.
#
# Por qué las etiquetas importan: cada release de GitHub cuelga de una etiqueta, y
# una etiqueta que apunta a un commit viejo lo mantiene accesible en GitHub aunque
# la rama ya esté limpia. Reescribir solo la rama no sirve de nada.
#
# Seguro de correr: NO toca archivos de trabajo. Tus google-services.json y
# firebase_options.dart locales quedan intactos.
#
# Uso:  bash purgar_claves_historial.sh
set -uo pipefail
R=/home/cristian/X/Github
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT

command -v git-filter-repo >/dev/null || { echo "Falta git-filter-repo"; exit 1; }

# repo:patrón de lo que hay que borrar
CLAVES_FIREBASE='AIza[A-Za-z0-9_-]{35}'
PASS_ACCESO='Operonte23#|admin123|guardia123|cliente123'

purgar() {
  local d=$1 patron=$2 quitar_apk=$3
  cd "$R/$d" || return 1
  local url rama
  url=$(git remote get-url origin)
  rama=$(git rev-parse --abbrev-ref HEAD)

  # 1) Traer TODAS las etiquetas del remoto, para reescribirlas junto con la rama.
  git fetch --force --tags origin >/dev/null 2>&1

  # 2) Juntar los secretos que aparezcan en cualquier ref (rama o etiqueta).
  #    Para Firebase se miran solo los archivos de config: dentro de los APK el
  #    patrón da falsos positivos.
  local rutas=()
  [ "$patron" = "$CLAVES_FIREBASE" ] && rutas=(-- "*google-services.json" "*firebase_options.dart")
  { git grep -ohE "$patron" $(git rev-list --all) "${rutas[@]}" 2>/dev/null || true; } \
    | sort -u | sed 's/$/==>***REMOVED-SECRET***/' > "$T/s.txt"

  if [ ! -s "$T/s.txt" ]; then
    echo "$d: sin secretos en el historial"
    return 0
  fi

  # 3) Reescribir TODAS las refs. Los APK pesan cientos de MB y llevan la clave dentro.
  local extra=()
  [ "$quitar_apk" = "si" ] && extra=(--path-glob '*.apk' --path-glob '*.aab' --invert-paths)
  git filter-repo --force --replace-text "$T/s.txt" "${extra[@]}" || return 1
  git remote add origin "$url" 2>/dev/null || git remote set-url origin "$url"

  # 4) Verificar en TODAS las refs, no solo en la rama.
  local quedan
  quedan=$({ git grep -lE "$patron" $(git rev-list --all) "${rutas[@]}" 2>/dev/null || true; } | wc -l)
  if [ "$quedan" -ne 0 ]; then
    echo "  >>> $d NO quedó limpio ($quedan), no lo subas"
    return 1
  fi
  echo "$d: limpio | commits=$(git rev-list --all --count) etiquetas=$(git tag|wc -l) .git=$(du -sh .git|cut -f1)"

  # 5) Subir rama y etiquetas. Sin las etiquetas, los commits viejos siguen vivos.
  git push --force origin "$rama" >/dev/null 2>&1 && git push --force --tags origin >/dev/null 2>&1 \
    && echo "  subido (rama + etiquetas)" || echo "  >>> fallo al subir $d"
}

purgar acceso        "$PASS_ACCESO"      no
purgar Holyapp       "$CLAVES_FIREBASE"  no
purgar preciobencina "$CLAVES_FIREBASE"  no
purgar coroapp       "$CLAVES_FIREBASE"  si
purgar misionapp     "$CLAVES_FIREBASE"  si
purgar sosapp        "$CLAVES_FIREBASE"  no

cat <<'FIN'

Hecho. Dos cosas que esto NO resuelve:
  - GitHub puede seguir sirviendo un commit viejo por su SHA directo hasta que
    haga limpieza. Para borrarlo del todo hay que pedirlo a GitHub Support.
  - Los APK ya publicados en las releases siguen llevando la clave dentro.
Por eso conviene igual rotar la contraseña y restringir las claves de Firebase.
FIN
