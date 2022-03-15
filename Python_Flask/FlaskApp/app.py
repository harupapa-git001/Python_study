from flask import Flask, render_template, session, request, redirect, url_for
import os
from pref_question import pref_location
from wiki import wiki

#インスタンスの作成
app = Flask(__name__)

#session機能を扱うための暗号鍵を作成
key = os.urandom(21)
app.secret_key = key

#app.pyにログインするためのユーザIDをパスワードを作成する
id_pwd = {'user': 'password'}

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

@app.route('/answercheck', methods=['POST'])
def answercheck():
    user_answer = request.form['city']
    prefecture = session.get('prefecture')
    city = session.get('city')
    url = session.get('url')

    if user_answer == city:
        result = '正解!!'

    else:
        result = '残念!!'

    return render_template('result.html', result=result, prefecture=prefecture, city=city, url=url)

@app.route('/pref_quiz', methods=['POST'])
def pref_quiz():
    random_pref, city_name, pref_url = pref_location()
    session['prefecture'] = random_pref
    session['city'] = city_name
    session['url'] = pref_url
    return render_template('quiz.html', prefecture=random_pref)

@app.route('/wikipedia', methods=['POST'])
def wikipedia():
    return render_template('wiki_result.html', result='')

@app.route('/wiki_answer', methods=['POST'])
def wiki_answer():
    word = request.form['word']
    if word == '':
        result = '入力がないため、該当する結果がありませんでした。'
    
    else:
        result = wiki(word)

    return render_template('wiki_result.html', result=result)

#アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)