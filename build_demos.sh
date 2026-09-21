#!/usr/bin/env bash
# Compila las demos web (Flutter) de algunas apps y las copia a portfolio/public/demo/<slug>/.
# Trabaja sobre COPIAS temporales: no modifica los repositorios de las apps.
# El motor gráfico de Flutter (CanvasKit) se carga desde el CDN de Google, así cada demo pesa pocos MB.
# Uso: bash build_demos.sh [slug ...]   (sin argumentos compila todas)
set -euo pipefail
ROOT=/home/cristian/X/Github
OUT=$ROOT/portfolio/public/demo
WORK=${TMPDIR:-/tmp}/portfolio_demos
mkdir -p "$WORK" "$OUT"

build() {
  local dir=$1 slug=$2
  echo "== $slug"
  rm -rf "$WORK/$dir" && mkdir -p "$WORK/$dir"
  rsync -a --exclude build --exclude .dart_tool --exclude android --exclude ios --exclude macos \
        --exclude linux --exclude windows --exclude .git --exclude release --exclude dist \
        --exclude presentacion "$ROOT/$dir/" "$WORK/$dir/"
  (cd "$WORK/$dir" && flutter pub get >/dev/null && flutter build web --release --no-wasm-dry-run --base-href "/demo/$slug/" 2>&1 | grep -E "Built|Error" || true)
  rm -rf "$OUT/$slug" && mkdir -p "$OUT/$slug"
  cp -r "$WORK/$dir/build/web/." "$OUT/$slug/" && rm -f "$OUT/$slug/.last_build_id"
  # El motor gráfico se descarga del CDN de Google: la copia local (37 MB) no se usa.
  rm -rf "$OUT/$slug/canvaskit"
  # Sin service worker: evita cachear archivos que ya no existen y versiones viejas de la demo.
  rm -f "$OUT/$slug/flutter_service_worker.js"
  python3 - "$OUT/$slug/flutter_bootstrap.js" <<'PY'
import re, sys
p = sys.argv[1]
s = open(p).read()
s = re.sub(r"_flutter\.loader\.load\(\{.*?\}\s*\);\s*$", "_flutter.loader.load({});\n", s, flags=re.S)
open(p, "w").write(s)
PY
  printf '   %s: %s\n' "$slug" "$(du -sh "$OUT/$slug" | cut -f1)"
}

want=("$@")
run() { [ ${#want[@]} -eq 0 ] || printf '%s\n' "${want[@]}" | grep -qx "$2" && build "$1" "$2" || true; }
run fast fast
run Holyapp holyapp
run horasmedicas horasmedicas
run logos logos
du -sh "$OUT"
