from flask import Flask, render_template

from random import random

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', l=["出力１", "出力2", "出力3"])