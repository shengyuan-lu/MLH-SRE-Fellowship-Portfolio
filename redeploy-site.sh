#!/bin/bash
tmux kill-server
git fetch && git reset --hard origin/main
source python3-virtualenv/bin/activate
pip install -r requirements.txt

export FLASK_ENV=development
tmux new-session -d -s redeploy 'flask run'
