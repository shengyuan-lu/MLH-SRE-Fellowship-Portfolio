#!/bin/bash
tmux kill-server
git fetch && git reset --hard origin/main
python -m venv python3-virtualenv
source python3-virtualenv/bin/activate
pip install -r requirements.txt

# Start a new detached Tmux session and run the server
tmux new-session -d -s redeploy 'source venv/bin/activate && flask run'


