#!/usr/bin/env bash
set -euo pipefail

# Unit 04-14：在 WSL2 启动免代理 tmux 无人值守生产窗格
SESSION="u4-studio-batch"
unset all_proxy ALL_PROXY http_proxy https_proxy HTTP_PROXY HTTPS_PROXY || true

if tmux has-session -t "$SESSION" 2>/dev/null; then
  echo "Session $SESSION already running. Attach with: tmux attach -t $SESSION"
  exit 0
fi

tmux new-session -d -s "$SESSION" -n "runner"
tmux send-keys -t "$SESSION:runner" "export HF_HUB_OFFLINE=1 && echo '[ready] 16G single-GPU batch guard armed'" C-m
tmux split-window -v -t "$SESSION:runner"
tmux send-keys -t "$SESSION:runner.1" "watch -n 5 nvidia-smi" C-m
echo "Started tmux session: $SESSION (attach: tmux attach -t $SESSION)"
