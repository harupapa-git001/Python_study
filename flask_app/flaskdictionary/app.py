from flask import Flask, render_template

from random import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', l=[{"name": "出力1", "value": "1"}, {"name": "出力2", "value": "2"}, {"name": "出力3", "value": "3"}])