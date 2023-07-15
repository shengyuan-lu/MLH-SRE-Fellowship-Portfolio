#!/bin/bash
tmux kill-session
git fetch && git reset --hard origin/main
source python3-virtualenv/bin/activate
pip install -r requirements.txt

export FLASK_ENV=development
sudo systemctl daemon-reload
sudo systemctl restart myportfolio.service

