#このフォルダには複数のプログラム.pyが含まれます
#それぞれの.pyファイルをpythonで実行する前に仮想環境を構築してください

[仮想環境の構築方法]
ターミナルで以下のコマンドを実行してください

$ python3 -m venv scraping

$ source scraping/bin/activate

#仮想環境に入ったのちに各モジュールのインストールを下記の要領で実行してください

$ pip3 install bs4

#全てのモジュールをインストールし終わったら通常のpythonの起動を行ってください

ex.

$ python3 catchimg.py
