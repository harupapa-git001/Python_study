#-*- coding: utf-8 -*-

'''ex1 #ウィンドウを表示

import tkinter as tk

root = tk.Tk()

root.mainloop()

'''

'''ex2 #tkバージョンの確認

import tkinter as tk

print(tk.TkVersion)

'''

'''ex3 #ジオメトリ1

import tkinter as tk

root = tk.Tk()

root.title("位置指定")

root.geometry("450x350")    # xは小文字、大文字はエラー(bad geometry specifier)

root.mainloop()

'''

'''ex4 #ジオメトリ2

import tkinter as tk

root = tk.Tk()

root.title("位置指定")

#下記の#を入れ替えてください。root.geometry("幅x高さ+x座標+y座標")

#root.geometry("+350+250")

root.geometry("450x350+350+250")

root.mainloop()

'''

'''ex5 #ウィジェットの作成

import tkinter as tk

root = tk.Tk()

root.title("部品(widget)の作成")

root.geometry("350x150")

#部品(widget)の作成

lb = tk.Label(text = "ラベル")

bt = tk.Button(text = "ボタン")

root.mainloop()

'''

'''ex6 #ラベルとボタンの配置

import tkinter as tk

root = tk.Tk()

root.title("部品(widget)の作成")

root.geometry("350x150")

lb = tk.Label(text = "ラベル")

bt = tk.Button(text = "ボタン")

#配置

lb.pack()   #追加行

bt.pack()   #追加行

#packの他にもplaceやgridがあります（他章で説明）

root.mainloop()

'''

'''ex7 #アクションの組み込み

import tkinter as tk

#ボタンが押された時に呼び出される

def action_btn_press():
    print("ボタンが押されました")

root = tk.Tk()

root.title("アクションの組み込み")

root.geometry("350x150")

lb = tk.Label(text = "ラベル")

# commandオプションに関数名を指定
#commandへの関数名指定は他のプログラミング言語でいうactionやbindのようなものだと思ってください。
bt = tk.Button(text = "ボタン", command = action_btn_press)

lb.pack()

bt.pack()

root.mainloop()

'''

'''ex8 #テキストボックス内容の取得
import tkinter as tk

def print_txtval():
    #テキストボックス内容の取得
    
    val_en = en.get()
    
    print(val_en)
    
root = tk.Tk()

root.title("テキストボックス内容の取得")

root.geometry("350x150")

lb = tk.Label(text = "ラベル")

#テキストボックスの作成

en = tk.Entry()

bt = tk.Button(text = "ボタン", command = print_txtval)

[widget.pack() for widget in (lb, en ,bt)]

root.mainloop()


#.focus_set()を使えばテキストボックスをクリックする手間が省けます。事項で使います。なお、テキストボックスやボタンのフォーカスはtabキーでも移動できます。
'''

'''ex8''' #classApplicationによる雛型

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        
        master.title("テキストボックス内容の取得")

        master.geometry("350x150")
        
        self.pack()
        
        self.create_widgets()
        
    #部品の作成/設定
    
    def create_widgets(self):
        self.lb = tk.Label(self)
        
        self.lb["text"] = "ラベル"
        
        self.pack(side = "top")
        
        self.en = tk.Entry(self)
        
        self.en.pack()
        
        self.en.focus_set()
        
        self.bt = tk.Button(self)
        
        #このようにも書けるself.bt = tk.Button(text = "ボタン", command = self.print_txtval)
        
        self.bt["text"] = "ボタン"
        
        self.bt["command"] = self.print_txtval
        
        self.bt.pack(side = "bottom")
        
    def print_txtval(self):
        val_en = self.en.get()
        
        print(val_en)
        
root = tk.Tk()

app = Application(master = root)

app.mainloop()
