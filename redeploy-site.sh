#!/bin/bash

# Step 1: end service
echo 'End myportfolio service'
systemctl stop myportfolio

# Step 2: Change directory to your project folder
cd /root/mlh-sre-fellowship-portfolio

# Step 3: Fetch and reset the Git repository to the latest changes from GitHub
git fetch && git reset origin/main --hard

# Step 4: Activate Python virtual environment and install dependencies
echo 'Activate Python virtual environment'
source /root/mlh-sre-fellowship-portfolio/python3-virtualenv/bin/activate
pip install -r requirements.txt

# Step 5: restart service
echo 'Restart myportfolio service'
systemctl daemon-related
systemctl start myportfolio
