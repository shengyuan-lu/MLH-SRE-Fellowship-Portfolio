#!/bin/bash
tmux kill-session
git fetch && git reset --hard origin/main
source python3-virtualenv/bin/activate
pip install -r requirements.txt

export FLASK_ENV=development
tmux new-session -d -s redeploy 'source python3-virtualenv/bin/activate && flask run --host=0.0.0.0'
