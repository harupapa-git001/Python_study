from flask import Flask, render_template, session, request, redirect, url_for
import os

#インスタンスの作成
app = Flask(__name__)

#session機能を扱うための暗号鍵を作成
key = os.urandom(21)
app.secret_key = key

#app.pyにログインするためのユーザIDをパスワードを作成する
id_pwd = {'hachi': 'password'}

# #メイン
# @app.route('/')
# def index():
#     return 'Hello demon Slayer'

#app.pyにHTMLを展開するための記述を作成
@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('login', None)
    return redirect(url_for('index'))

#app.route('/')にindex.htmlを割り当てる
@app.route('/')
def index():
    if not session.get('login'):
        return redirect(url_for('login'))

    else:
        return render_template('index.html')

#ログインの認証
@app.route('/logincheck', methods=['POST'])
def logincheck():
    user_id = request.form['user_id']
    password = request.form['password']

    if user_id in id_pwd:
        if password == id_pwd[user_id]:
            session['login'] = True

        else:
            session['login'] = False

    else:
        session['login'] = False

    if session['login']:
        return redirect(url_for('index'))

    else:
        return redirect(url_for('login'))

#アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)