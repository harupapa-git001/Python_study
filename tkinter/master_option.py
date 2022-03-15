#-*- coding: utf-8 -*-

'''
    部品構成の際にはマスターとオプションを渡すことができます。
    
    ・マスター
    
    マスターとは、配置先のことでrootであるメインウィンドウであったり、別途フレームであったりもします。
    
    前項のtk.Label(self)のような感じです。この時の場合はrootをマスターとしてclass Applicationに渡していたので、rootとなります。
    
    明示的な指定先がなければ、省略も可能です（本書ではメインウィンドウの場合は基本的に省略します）
    
    ・オプション
    オプションとはtextやcommandなどパラメータのことです。
    
'''

'''
    コンフィグ
    
        さてオプションですが、前項では2つのパターンにて設定をしました。
        
        1つ目は作成時にオプション名を引数キーといて値を渡す、よく使われるパターンです。カンマ区切りで複数のオプションを指定できるので、コードの簡潔化ができます。
        
        lb = tk.Label("text = "ラベル")
        
        2つ目は作成後に辞書型のキーを渡すような方式。
        
        コードは長くなりますが、可続生は上がるのでメンテナンスはしやすくなります。
        
        bt = tk.Button()
        
        bt["text"] = "ボタン"
        
        bt["command"] = action_btn_press
        
        もちろんこのように分けて書く事もできます。
        
        bt = tk.Button(text = "ボタン")
        
        bt["command"] = action_btn_press
        
        実はもうひとつ、.config()を使用する3つ目のパターンもあります。
        
        bt = tk.Button()
        
        bt.config(text = "ボタン", command = action_btn_press)
        
        この.config()の特筆すべきところは、その部品の持つオプションを表示することが出来るということです。
        
        試しにラベルの持つオプションを表示してみましょう。
        
'''

#オプション表示

import tkinter as tk

root = tk.Tk()

root.title(".config")

root.geometry("350x150")

lb = tk.Label()

#lb["text"] = "ラベル"

print(lb.config())

root.mainloop()



'''
    辞書型の形式で表示され、各オプションの中身は5つの要素を持つタプルとなっています。
    
    （オプション名, DB検索用オプション名, DB検索用オプションクラス, デフォルトの値, 現在の値）
    
    たまに"bg"のような短縮系情報のタプルもあります。

    lb["text"] = "ラベル"
    
    print(lb.config())
    
    とすると、"text"の箇所は
    
    'text': ('text', 'text', 'Text','', 'ラベル'),と表示されます。 #ex1の#を外して実行してください。
    

'''
