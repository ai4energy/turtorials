#!/usr/bin/env bash
set -euo pipefail

# 第三单元第 1 集示范脚本：apt 安装并启动 Nginx，随后验证本地 80 端口响应
sudo apt-get update
sudo apt-get install -y nginx
sudo cp "$(dirname "$0")/index.html" /var/www/html/index.html
sudo service nginx start || sudo nginx
curl -I http://127.0.0.1:80
