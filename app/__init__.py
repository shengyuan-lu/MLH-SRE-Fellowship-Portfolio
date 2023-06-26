import os
from flask import Flask, render_template, request
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/projects')
def projects():
    return render_template('projects.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/map')
def map():
    return render_template('map.html', title="MLH Fellow", url=os.getenv("URL"))

@app.route('/about_me')
def about_me():
    return render_template('index.html', title="MLH Fellow", url=os.getenv("URL"))

