#!/usr/bin/env bash
# Borra del HISTORIAL de git las claves de API de Firebase y los APK versionados.
#
# Los archivos actuales ya están limpios; esto reescribe los commits antiguos, que
# es lo que mantiene abiertas las alertas de GitHub. Reescribir cambia todos los
# identificadores de commit: por eso hace falta `push --force`.
#
# Seguro de correr: NO toca ningún archivo de trabajo, solo el historial. Tus
# google-services.json y firebase_options.dart locales quedan intactos.
#
# Uso:  bash purgar_claves_historial.sh
set -euo pipefail
R=/home/cristian/X/Github
T=$(mktemp -d)
trap 'rm -rf "$T"' EXIT

command -v git-filter-repo >/dev/null || { echo "Falta git-filter-repo"; exit 1; }

for d in Holyapp preciobencina coroapp misionapp sosapp; do
  cd "$R/$d"
  url=$(git remote get-url origin)
  rama=$(git rev-parse --abbrev-ref HEAD)

  # Claves reales que aparecen en el historial, solo desde los archivos de config
  # (dentro de los APK el patrón da falsos positivos).
  git grep -ohE "AIza[A-Za-z0-9_-]{35}" $(git rev-list --all) \
      -- "*google-services.json" "*firebase_options.dart" 2>/dev/null \
    | sort -u | sed 's/$/==>***REMOVED-SECRET***/' > "$T/claves.txt"

  if [ ! -s "$T/claves.txt" ]; then
    echo "$d: sin claves en el historial, se omite"
    continue
  fi

  # Los APK versionados pesan cientos de MB y llevan la clave embebida dentro.
  git filter-repo --force \
    --replace-text "$T/claves.txt" \
    --path-glob '*.apk' --path-glob '*.aab' --invert-paths

  git remote add origin "$url" 2>/dev/null || git remote set-url origin "$url"

  quedan=$(git grep -ohE "AIza[A-Za-z0-9_-]{35}" $(git rev-list --all) \
           -- "*google-services.json" "*firebase_options.dart" 2>/dev/null | wc -l)
  echo "$d: claves restantes=$quedan  commits=$(git rev-list --all --count)  .git=$(du -sh .git | cut -f1)"
  [ "$quedan" -eq 0 ] || { echo "  >>> $d NO quedó limpio, revisa antes de subir"; exit 1; }
done

echo
echo "Listo en local. Ahora sube cada uno (reescribe el historial en GitHub):"
for d in Holyapp preciobencina coroapp misionapp sosapp; do
  cd "$R/$d"
  echo "  cd $R/$d && git push --force origin $(git rev-parse --abbrev-ref HEAD)"
done
