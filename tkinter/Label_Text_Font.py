'''
    ラベル（Label）:テキスト更新/フォント/色
    
    まずはラベルからです。
    
    いうまでもなく、テキストの表示に使用します。
    
    lb = tk.Label(text = "ラベル")
    
    ・テキスト
    
    テキストを更新したい場合は単純にキー指定でlb["text"] = "更新"のようにします。また参照も同じようにできます。
    
    print(lb["text"])
    
    ・フォント
    
    fontオプションで設定を行います。
    
    タプルで(family[, size][, weight][,slant][,under][, overstrike])の順となりfamilyは必須となります。
    
    =fontオプション=
    
    family          フォント名（必須）
    size            フォントサイズ
    weight          "normal", "bold"
    slant           "roman", "italic"
    underline       "normal", "underline"
    overstrike      "normal", "overstrike"
    
    だいたい見ればわかると思いますが、サイズ以降は太字、斜体、下線、取消線の設定となります。
    
'''

'''

import tkinter as tk

root = tk.Tk()

lb = tk.Label(text = "MSゴシック, サイズ20, 太字でない, 斜体, 下線なし, 取消線あり", font = ("M S ゴシック", 20, "normal", "italic", "normal", "overstrike")) #取消線が出ない

lb.pack()

root.mainloop()

'''

'''
    なおfamily一覧はtkinter.fontの.families()を呼び出すことにより、確認できます。
    
'''

'''

import tkinter as tk

import tkinter.font as tk_font

root = tk.Tk()

print(tk_font.families())

'''

'''
    確認だけならrootの定義は必要なさそうですが、定義をしなければ.families()のreturn箇所でNoneTypeエラーが起きてしまいます（Python3.6系）。
'''

'''
    色
    
    ・文字色のオプション名
    
    foregroundもしくはfg(foregroundの短縮系)
    
    ・背景色のオプション名
    
    backgroundもしくはbg(bakgroudの短縮系)
    
    色の値は#rgb(4bit16色) #rrggbb(8bit256色) #rrrgggbbb(16bit4096色)もしくは色名で指定します。
    
    色名は"white", "black", "red", "green", "blue", "cyan", "yellow", "magenta"は全環境、その他の色名は使っているローカル環境によります。
    
'''

import tkinter as tk

root = tk.Tk()

root.geometry("200x150")

lb_rgb = tk.Label(text = "rgb", fg = "#000", bg = "#fff")

lb_rrggbb = tk.Label(text = "rrggbb", fg = "#abcdef", bg = "#123456")

lb_rrrgggbbb = tk.Label(text = "rrrgggbbb", fg = "#123456789", bg = "#987abcdef")

lb_colorname = tk.Label(text = "colorname", fg = "magenta", bg = "yellow")

[widget.pack() for widget in (lb_rgb, lb_rrggbb, lb_rrrgggbbb, lb_colorname)]

root.mainloop()
