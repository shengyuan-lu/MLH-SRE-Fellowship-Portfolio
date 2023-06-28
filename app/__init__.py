import os
from flask import Flask, render_template, request
from dotenv import load_dotenv


load_dotenv()


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', title="Meet MLH Fellows", url=os.getenv("URL"))

@app.route('/shengyuan')
def shengyuan():
    return render_template('fellow.html', title="Fellow - Shengyuan Lu", url=os.getenv("URL"))

@app.route('/rami')
def rami():
    return render_template('fellow.html', title="Fellow - Rami Elsayed", url=os.getenv("URL"))

if __name__ == '__main__':
    app.run(debug=True)