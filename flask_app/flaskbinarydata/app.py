from flask import Flask, request, render_template
#from werkzeug.utils import secure_filename

"""
app.pyのコメントアウトとresult.htmlのコメントアウトを外すとファイルセキュリティ付きの画像表示になる
"""

app = Flask(__name__)

@app.route('/login', methods=['GET'])
def render_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    if request.form['username'] and request.form['email']:
        return render_template('check.html', email=request.form['email'], username=request.form['username'])
    
    else:
        return render_template('error.html')

@app.route('/upload', methods=['GET'])
def render_upload_from():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.form['name'] and request.files['image']:
        f = request.files['image']
        f.save('static/IMG_6328.PNG')
        return render_template('result.html', name=request.form['name'])
        # filepath = 'static/' + secure_filename(f.filename)
        # f.save(filepath)
        #return render_template('result.html', name=request.form['name'], image_url=filepath)
