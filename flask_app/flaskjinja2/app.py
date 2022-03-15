from flask import Flask, render_template

app = Flask(__name__)

#app.pyのコメントアウトとtemplate/index.htmlのコメントアウトを外すとjinja2でのHTMLにpythonでの辞書型データにアクセスする

@app.route('/')
def index():
    return render_template('index.html', title="Hello World")
    """
    return render_template('index.html', obj={"title": "Hello Goodbye"})
    """

