from flask import Flask, render_template, session, request, redirect, url_for

#インスタンスの作成
app = Flask(__name__)

#メイン
@app.route('/')
def index():
    return 'Hello demon Slayer'

@app.route('/kaminari')
def kaminari():
    return '霹靂一閃'

#アプリケーションの起動
if __name__ == '__main__':
    app.run(debug=True)


#仮想環境の構築方法
#app.pyのあるフォルダにcdで移動
#python -m venv application ←仮想環境のパッケージをインストール
                #↑applicationの場所は自由に名前をつける

                #application
                     #|-bin
                        #|-activate ←このactivateにsourceコマンドで連結

                        #source application/bin/activate
                        #(カレントディレクトリのバーの左に(application)付与=仮想環境内での作業可能状態)
                        #この状態でpip install されたモジュールはこの仮想環境内で使用可能になるはず(module error時)

#python app.pyで仮想環境内でのパイソンのメインファイル実行(Flaskの起動)
#http://127.0.0.1:5000/で接続画面確認
#ターミナルの仮想サーバー接続はCTRL+Cで切断
#仮想環境の解除はdeactivate
