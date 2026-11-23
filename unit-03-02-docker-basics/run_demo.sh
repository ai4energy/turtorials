#!/usr/bin/env bash
set -euo pipefail

HTML_DIR="$(cd "$(dirname "$0")/html" && pwd)"
docker pull nginx:alpine
docker rm -f my_web >/dev/null 2>&1 || true
docker run -d --name my_web -p 8081:80 -v "${HTML_DIR}:/usr/share/nginx/html:ro" nginx:alpine
docker ps --filter "name=my_web"
curl -I http://127.0.0.1:8081
