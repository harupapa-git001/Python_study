'''
    縦か横一列に配置する（１次元配列）
    
    ウィジェットの配置にはpack/grid/placeの3つの方法が用意されています。
    
    本項では.pack()の説明をします。.pack()はウィジェットを縦もしくは横一列へと１次元的に配置していきます。
    
    これまでだいぶ使ってきたので、オプションなしでの配置イメージはついているかと思いますので、オプションの指定を色々としてみましょう。
    
    位置詰め
    
    sideオプションは位置詰めの方向を設定するオプションです。
    
    "left"      左詰め
    "right"     右詰め
    "top"       上詰め
    "bottom"    下詰め
    
'''

'''ex49

import tkinter as tk

import random

root = tk.Tk()

root.title("pack")

side_list = ["left", "right", "top", "bottom"]

label_list = []

for i in range(1, 31):
    side = side_list[random.randint(0, 3)]
    
    label_list.append(tk.Label(root, text = "{0}:{1}".format("%02d"%i, side), relief = "groove"))
    
    #ループにて"left", "right", "top", "bottom"の順
    
    label_list[-1].pack(side = side)
    
root.mainloop()

#sideオプションの値をランダムとし30このラベルを配置

'''

'''
    余白
    
    padx        ウィジェット外側の横余白
    pady        ウィジェット外側の縦余白
    ipadx       ウィジェット内側の横余白
    ipady       ウィジェット内側の縦余白
    
'''

'''

label = tk.Label(root, text = "padx = 50, pady = 25, ipadx = 75, ipady = 150", background = "cyan")

#外側横余白 = 50, 外側縦余白 = 25, 内側横余白 = 75, 内側縦余白 = 150

label.pack(padx = 50, pady = 25, ipadx = 75, ipady = 150)

'''

'''ex50

import tkinter as tk

root = tk.Tk()

root.title("padx, pady, ipadx, ipady")
    
label = tk.Label(root, text = "padx = 50, pady = 25, ipadx = 75, ipady = 150", background = "cyan")

label.pack(padx = 50, pady = 25, ipadx = 75, ipady = 150)
    
root.mainloop()

'''

'''
    拡大
    
    ウィジェットを目一杯拡大するにはfillオプションを使います。
    
    "none"      特に拡大しない（デフォルト）
    "x"         横の方向に拡大
    "y"         縦の方向に拡大
    "both"      縦横両方の方向に拡大
    
    なお"y"や"both"（縦の方向）の反映はexpandオプションにTrueを渡しレスポンシブありにする必要があります。
    
'''

'''
    root.geometry("300x150")
    
    label = tk.Label(root, text = "fill = "x", padx = 5, pady = 50, relief = "groove")
    
    #横方向拡大　外側横余白 = 5, 外側縦余白 = 50
    
    label.pack(fill = "x", padx = 5, pady = 50)
    
'''

'''ex51

import tkinter as tk

root = tk.Tk()

root.geometry("300x150")

root.title("fill")

label = tk.Label(root, text = 'fill = "x", padx = 5, pady = 50', relief = "groove")

label.pack(fill = "x", padx = 5, pady = 50)

root.mainloop()

'''

'''
    レスポンシブ
    
    レスポンシブをありにする場合は、expandオプションにTrueを渡します。
    
    False       レスポンシブなし（デフォルト）
    True        レスポンシブあり
    
'''

'''ex52

import tkinter as tk

root = tk.Tk()

root.geometry("300x250")

root.title("expand")

label = tk.Label(root, text = 'fill = "y", expand = True, pady = 10', relief = "groove")

#レスポンシブあり

label.pack(fill = "y", expand = True, pady = 10)

root.mainloop()

'''

'''
    空きスペースへの配置位置
    
    anchorは空きスペースがある場合の配置位置を指定するオプションです。
    
    n       北（上）
    ne      北東（右上）
    e       東（右）
    se      南東（右下）
    s       南（下）
    sw      南西（左下）
    w       西（左）
    nw      北西（左上）
    
'''

'''ex53

import tkinter as tk

root = tk.Tk()

root.geometry("300x150")

root.title("anchor")

label1 = tk.Label(root, text = "text", relief = "groove")

#指定なし

label1.pack()

label2 = tk.Label(root, text = 'anchor = "se"', relief = "groove")  #' 'の位置に注意

#南東（右下）

label2.pack(anchor = "se")

label3 = tk.Label(root, text = "text", relief = "groove")

#指定なし

label3.pack()

label4 = tk.Label(root, text = 'anchor = "nw"', relief = "groove")

#北西（左上）

label4.pack(anchor = "nw")

root.mainloop()

#label2のtext = 'anchor = "se"'はanchor = "se"を' 'で囲み
#label4のtext = 'anchor = "nw"'はanchor = "nw"を' 'で囲んでいる

'''

'''
    格子状（２次元的）に配置する
    
    ウィジェットを格子状（２次元的）に配置していく場合は.grid()を使います。
    
    row/columnで行と列を指定します。
    
    row     何行に配置
    column  何列に配置
    (0からスタートします)
    
'''

'''ex54

import tkinter as tk

root = tk.Tk()

root.title("grid: row, column")

root.geometry("300x100")

label1 = tk.Label(root, text = "row = 0, column = 0", relief = "groove")

label1.grid(row = 0, column = 0)

label2 = tk.Label(root, text = "row = 0, column = 1", relief = "groove")

label2.grid(row = 0, column = 1)

label3 = tk.Label(root, text = "row = 1, column = 0", relief = "groove")

label3.grid(row = 1, column = 0)

label4 = tk.Label(root, text = "row = 1, column = 1", relief = "groove")

label4.grid(row = 1, column = 1)

root.mainloop()

'''

'''
    範囲
    
    rowspan/columnspanは行屋列の範囲指定に使います
    
    rowspan     何行へ渡るかの範囲
    columnspan  何列へ渡るかの範囲
    
'''

'''ex55

import tkinter as tk

root = tk.Tk()

root.title("grid: rowspan, columnspan")

root.geometry("350x170")

frame1 = tk.Frame(root, background = "#ece")

frame2 = tk.Frame(root, background = "#cec")

#rowspan = 2

label11 = tk.Label(frame1, text = "r0, c0, rs2", relief = "groove")

label11.grid(row = 0, column = 0, rowspan = 2)

label12 = tk.Label(frame1, text = "row0, col1", relief = "groove")

label12.grid(row = 0, column = 1)

label13 = tk.Label(frame1, text = "row1, col1", relief = "groove")

label13.grid(row = 1, column = 1)

label14 = tk.Label(frame1, text = "row2, col1", relief = "groove")

label14.grid(row = 2, column = 1)

#columnspan = 3

label21 = tk.Label(frame2, text = "+++ r0, c0, cs3 +++", relief = "groove")

label21.grid(row = 0, column = 0, columnspan = 3)

label22 = tk.Label(frame2, text = "row1, col0", relief = "groove")

label22.grid(row = 1, column = 0)

label23 = tk.Label(frame2, text = "row1, col1", relief = "groove")

label23.grid(row = 1, column = 1)

label24 = tk.Label(frame2, text = "row1, col2", relief = "groove")

label24.grid(row = 1, column = 2)

frame1.pack(padx = 5, pady = 5)

frame2.pack(padx = 5, pady = 5)

root.mainloop()

'''

'''
    「r0, c0, rs2」ラベルがrowspan = 2の指定
    
    「+++ r0, c0, cs3 +++」ラベルがcolunspan = 3の指定
    
    そして見ての通り、範囲指定だけでは自動に拡大されるわけでもありません。
    
'''

'''
    拡大
    
    sickyは.pack()のfillとanchorを組み合わせたようなオプションです。
    
    例えば上から下までならsticky = "ns"、左から右までならsticky = "we"といった感じです。
    
    sicky = tkinter.N + tkinter.Sやsicky =tkinter.W + tkinter.Eのように書くこともできます。
    
'''

'''ex56

import tkinter as tk

root = tk.Tk()

root.title("grid: sticky")

root.geometry("340x140")

frame1 = tk.Frame(root, background = "#eee")

frame2 = tk.Frame(root, background = "#eee")

#rowspan = 2

label11 = tk.Label(frame1, text = "r0, c0, rs2", relief = "groove")

#sticky = tk.N + tk.Sのようにも書ける（上から下）

label11.grid(row = 0, column = 0, rowspan = 2, sticky = "ns")

label12 = tk.Label(frame1, text = "row0, col1", relief = "groove")

label12.grid(row = 0, column = 1)

label13 = tk.Label(frame1, text = "row1, col1", relief = "groove")

label13.grid(row = 1, column = 1)

label14 = tk.Label(frame1, text = "row2, col1", relief = "groove")

label14.grid(row = 2, column = 1)

#columnspan = 3

label21 = tk.Label(frame2, text = "+++ r0, c0, cs3 +++", relief = "groove")

#sticky = tk.W + tk.Eのようにも書ける（左から右）

label21.grid(row = 0, column = 0, columnspan = 3, sticky = "we")

label22 = tk.Label(frame2, text = "row1, col0", relief = "groove")

label22.grid(row = 1, column = 0)

label23 = tk.Label(frame2, text = "row1, col1", relief = "groove")

label23.grid(row = 1, column = 1)

label24 = tk.Label(frame2, text = "row1, col2", relief = "groove")

label24.grid(row = 1, column = 2)

frame1.pack(padx = 5, pady = 5)

frame2.pack(padx = 5, pady = 5)

root.mainloop()

'''

'''
    位置（座標）を指定し配置する
    
    .place()はウィジェットの位置（座標）を指定し配置するメソッドです。
    
    各ウィジェットの位置を直接指定できるのが利点です。
    
    x           マスターに対しての絶対的なx座標
    y           マスターに対しての絶対的なy座標
    width       幅
    height      高さ
    relx        マスターに対しての相対的なx座標
    rely        マスターに対しての相対的なy座標
    relwidth    マスターに対しての相対的な幅
    relheight   マスターに対しての相対的な高さ
    
'''

'''ex57

import tkinter as tk

root = tk.Tk()

root.geometry("600x600")

root.title(" .place() ")

#frame1

frame1 = tk.Frame(root, width = 600, height = 300, background = "#fef")

label11 = tk.Label(frame1, text = "[frame1 600x300]\nrelx=0.25, rely=0.25\nrelwidht=0.5, relheight=0.5", background = "#fdf")

#.place()で配置、マスターに対して座標やサイズを設定

label11.place(relx = 0.25, rely = 0.25, relwidth = 0.5, relheight = 0.5)

frame1.pack()

#frame2

frame2 = tk.Frame(root, width = 600, height = 300, background = "#eef")

label21 = tk.Label(frame2, text ="[frame2 600x300]\nx=50, y=50\nwidth=150, height=150", background = "#ddf")

#.place()で配置、絶対的な座標やサイズを設定

label21.place(x = 50, y = 50, width = 150, height = 150)

label22 = tk.Label(frame2, text = "[frame2 600x300]\nrelx=0.5, rely=0.5\nrelwidth=0.25\nrelheight=0.25", background = "#ddf")

#.place()で配置、マスターに対して座標やサイズを設定

label22.place(relx = 0.5, rely = 0.5, relwidth = 0.25, relheight = 0.25)

frame2.pack()

#root

label01 = tk.Label(root,text = "[root 600x600]\nx=100, y=100\nwidth=150, height=150", background = "#efe")

#.place()で配置、絶対的な座標やサイズを設定

label01.place(x = 100, y = 100, width = 150, height = 150)

label02 = tk.Label(root, text = "[root 600x600]\nrelx=0.25, rely=0.25\nrelwidth=0.25\nrelheight=0.25", background = "#efe")

#.place()で配置、マスターに対して座標やサイズを設定

label02.place(relx = 0.5, rely = 0.5, relwidth = 0.25, relheight = 0.25)

root.mainloop()

'''

'''
    ファンクションキーの割り当て
    
    今まではウィジェットを対象に仮想イベントを紐づけていましたが、この対象をメインウィンドウにして単純に"<F1>"など割り当てると、ファンクションキーのように使用できます。
    
'''

'''ex58

import tkinter as tk

def press_f1(event):
    label["text"] = "pressed F1"
    
root = tk.Tk()

root.geometry("300x150")

root.title("function key")

label = tk.Label(root, text = "function key(F1)", relief = "groove")

#メインウィンドウを対象にキーのイベントをつける

root.bind("<F1>", press_f1)

label.pack()

root.mainloop()

#もし反応しなかったときは後項で説明するキー識別子の確認から分岐もあります。この辺りは環境にもよるので、状況に応じて使い分けましょう。

'''

'''
    キーの識別子を確認する
        
    これまでもウィジェットのバインドで仮想イベントを割り当ててきましたが、各キーの識別子を見てみましょう。
    
    また使用するPCやOS環境により識別子が異なることもあるので、再確認をするにも役に立ちます。
    
    簡単な手順としては
    
    1. <Key>を仮想イベントとしたコールバック関数を作成
    2. 受け取ったイベントの.keysymを確認
    
    となります
    
'''

'''ex59

import tkinter as tk

def callback_func(event):
    #識別子の取得
    
    label["text"] = event.keysym

root = tk.Tk()

root.geometry("300x150")

root.title("keysym")

label = tk.Label(root, text = "keysym", relief = "groove")

#キーイベント

root.bind("<Key>", callback_func)

label.pack()

root.mainloop()

'''

'''
    立ち上げ時の状態から「a」キーを押下すると<Key>イベントの.keysymよりaキーの識別子を取得

    なおevent.keysymはstr型なので文字列比較による分岐もできます。
    
'''

'''ex60

import tkinter as tk

def callback_func(event):
    #識別子の取得
    
    #label["text"] = event.keysym
    
    ks = event.keysym
    
    if ks == "l" or ks == "r":
        label["text"] = "pressed control"

root = tk.Tk()

root.geometry("300x150")

root.title("keysym")

label = tk.Label(root, text = "keysym", relief = "groove")

#キーイベント

root.bind("<Control-Key>", callback_func)

label.pack()

root.mainloop()

'''

'''
    キーのショートカット押し
    
    Ctrl + c　のようなショートカット押しは - をつけ"<Control-c>"のようにします。
    
    （または"<Control-Key-c>"）
    
    ややこしいことに"<Control_L-c>"はエラーとなります。
    
    左右で分けたい場合は"<Control_L><c>"のように連続押しで代用もできます。
    
    ただしこの場合は"<Control_L>"の後に"<c>"（連続であれば時間が空いても可）なので少しニュアンスが違ってくる点に注意しましょう。
    
'''

'''ex61

import tkinter as tk

def press_ctrlc(event):
    label["text"] = "ctrl c"
    
def press_ctrl_l_c(event):
    lbal["text"] = "ctrl_l after c"
    
def press_ctrl_r_c(event):
    label["text"] = "ctrl_r after c"
    
root = tk.Tk()

root.geometry("300x150")

root.title("shortcut key")

label = tk.Label(root, text = "shortcut key test(ctrl c)", relief = "groove")

#Ctrl + cのショートカット押し

root.bind("<Control-c>", press_ctrlc)

#これはエラーになります
#root.bint("<Control_L-c>", press_ctrl_l_c)

#連続押しによる代用、ただしニュアンスが違ってくる

root.bind("<Control_L><c>", press_ctrl_l_c)

root.bind("<Control_R><c>", press_ctrl_r_c)

label.pack()

root.mainloop()

#立ち上げ時Ctrl + cでラベルの更新

'''

'''
    "<Control-c>"と"<Control_L><c>"が両方あると「ctrl c」ではなく「ctrl_l after c」のコメントとなり"<Control_L><c>のイベントの方が優先されてしまいます。
    
    このような場合は"<Control_L><c>"のバインドを削除すれば"<Control-c>"のイベント処理をすることができます。
    
'''

'''
    各種マウスイベント
    
    マウスボタンのイベントは<Button>を使います。
    
    イベント発生カーソル位置
    
    .xと.yで押下時のカーソル位置も取得できます。
    
'''

'''ex62

import tkinter as tk

def callback_func(event):
    #カーソル位置の取得
    
    label["text"] ="x:{0},y:{1}".format(event.x, event.y)
    
root = tk.Tk()

root.geometry("250x280")

root.title("mouse x, y")

label = tk.Label(root, text = "mouse", relief = "groove")

#マウスボタンのイベント

root.bind("<Button>", callback_func)

label.pack()

root.mainloop()

'''

'''
    ボタンの種類
    
    何ボタンかは.numで取得します
    
    def callback_func(event):
        #何ボタンかを取得
        
        button_num = event.num
        
        label["text"] = "button num:{0}".format(button_num)
'''

'''ex63

import tkinter as tk

def callback_func(event):
    #カーソル位置の取得
    
    #label["text"] ="x:{0},y:{1}".format(event.x, event.y)
    
    #何ボタンかを取得
    
    button_num = event.num
    
    label["text"] = "button num:{0}".format(button_num)
    
root = tk.Tk()

root.geometry("250x280")

root.title("mouse x, y")

label = tk.Label(root, text = "mouse", relief = "groove")

#マウスボタンのイベント

root.bind("<Button>", callback_func)

label.pack()

root.mainloop()

'''

'''
    なおevent.numを元に分岐しても良いのですが、各ボタンに応じたイベントは最初から用意されています。
    
    <Button-1>または<1>    左ボタン押下（クリック）
    <Button-2>または<2>    中ボタン押下
    <Button-3>または<3>    右ボタン押下（右クリック）
    
    #　Macでは左<1>右<2>中<3>の仕様になっていました
    
    これらを活用し、ボタン毎のコールバック関数を作成しても良いでしょう。
    
'''

'''
    マウス移動中イベント
    
    マウス移動中のイベントは<Motion>を使います。
    
'''

'''ex64

import tkinter as tk

def callback_func(event):
    label["text"] = "x:{0},y:{1}".format(event.x, event.y)
    
root = tk.Tk()

root.geometry("300x200")

root.title("mouse motion")

label = tk.Label(root, text = "mouse motion", relief = "groove")

#マウス移動中のイベント

root.bind("<Motion>", callback_func)

label.pack()

root.mainloop()

'''

'''
    ボタン押下中移動イベント
    
    ボタン押しながら移動のイベントも用意されています。
    
    <Button1-Motion>または<B1-Motion>  左ボタン押しながら移動
    <Button2-Motion>または<B2-Motion>  中ボタン押しながら移動
    <Button3-Motion>または<B3-Motion>  右ボタン押しながら移動
    
'''

'''ex65

import tkinter as tk

def callback_func(event):
    label["text"] = "x:{0}, y:{1}".format(event.x, event.y)
    
root = tk.Tk()

root.geometry("300x200")

root.title("mouse motion button3")

label = tk.Label(root, text = "mouse motion button3", relief = "groove")

#右ボタン押しながら移動のイベント

root.bind("<Button3-Motion>", callback_func)

label.pack()

root.mainloop()

 #ウィンドウ内で右ボタン(Macは中ボタンでした)を押しながらカーソルを動かしている間は、リアルタイムでカーソル位置を取得する

'''

'''
    これまでいろんなマウスイベントを使ってきましたが、以下ざっと簡単にまとめた一覧です。
    
    <Button>                        ボタン押下
    <Button-○>or<○>                 各ボタン押下
    <Motion>                        マウス移動中
    <Button○-Motion>or<B○-Motion>   何ボタン押下移動中
    event.num                       何ボタンか
    event.x, event.y                カーソル位置
    
'''

'''
    ウィジェット内外/対象オブジェクト
    
    マウスカーソルがウィジェット内に入った、外に出たのイベントは<Enter>と<Leave>になります。
    
    また.widgetでイベント対象となっているウィジェットのオブジェクトを取得できます。
    
    <Enter> マウスカーソルがウィジェットの中
    <Leave> マウスカーソルがウィジェットの外
    
    もちろん.widgetでのオブジェクト取得は<Enter><Leave>以外のイベントにも適用されます。
    
'''

'''ex66

import tkinter as tk

def enter_label(event):
    #.widgetでイベント対象ウィジェットのオブジェクトを取得できる
    
    event.widget["background"] = "#bfb"
    
def leave_label(event):
    event.widget["background"] = "#bbf"
    
root = tk.Tk()

root.geometry("300x120")

root.title("Enter/Leave")

label = tk.Label(root, text = "mouse here", background = "#bbf")

label.pack(ipadx = 70, pady = 35)

#<Enter>:マウスカーソルがウィジェットの中

label.bind("<Enter>", enter_label)

#<Leave>:マウスカーソルがウィジェットの外

label.bind("<Leave>", leave_label)

root.mainloop()

'''

'''
    ウィジェットの状態
    
    ウィジェットの状態はstateオプションに紐づいています。
    
    tkinter.NORMAL      通常（デフォルト）
    tkinter.DISABLED    無効
    tkinter.ACTIVE      アクティブ
    
    アクティブというのは、ウィジェット上にマウスカーソルがあり、背景色が少し変わっている状態のことです。
    
'''

'''ex67

import tkinter as tk

def update_state(event):
    #チェックボックス押下時にイベント発生なので、押下前のチェック状況が取得される
    
    button["state"] = tk.DISABLED if boolvar.get() else tk.NORMAL
    
root = tk.Tk()

boolvar = tk.BooleanVar()

root.geometry("280x120")

root.title("state")

checkbutton = tk.Checkbutton(text = "はい、同意します", variable = boolvar)

button = tk.Button(text = "次へ", state = tk.DISABLED)

checkbutton.pack(pady = 5)

button.pack(pady = 5)

checkbutton.bind("<Button-1>", func = update_state)

[widget.pack(pady = 10) for widget in (checkbutton, button)]

root.mainloop()

#「はい、同意します」にチェックを入れると次へボタンが通常状態、チェックなしだと無効状態になります。

'''

'''
    Web上よりTkの仕様を更に調べよう
    
    今後、GUIアプリケーション作成にあたり、更に仕様を調べたい場合はTcl/Tkのサイトで確認すると良いでしょう。
    
    http://www.tc.tk/
    
    （例）キー識別子やイベントを調べる
    
    例えばバインド時のキーの識別子を調べたい場合は
    
    1. SEARCH欄にbindと入力
    
    （検索結果一覧）
    
    「bind manual page - Tk Built-In Commands - Tcl/Tk」をクリック
    
    （バインドのマニュアルページ）
    
    2. 「SEE ALSO」をクリック
    
    （ページ内リンク）
    
    3. 「keysyms」をクリック
    
    （バインドkey名の一覧ページへたどり着く）
    
    https://www.tcl.tk/man/tcl/TkCmd/keysyms.htm
    
    また更に「SEE ALSO」の「event」をクリックでイベント一覧に遷移します。
    
    https://www.tcl.tk/tcl/TkCmd/event.htm
    
    英語にはなりますが、仕様が幅広く掲載されているので今後の役に立つと思います。
'''

'''
    簡単なGUIアプリケーションを作成しよう
    
    これまでウィジェットの基本的な使い方を学習してきました。
    
    せっかくなので、簡単なGUIアプリケーションを作成してみましょう。
    
    スケールを動かすことにより、文字と背景のRGB値（色）を調整し、配色の感覚を確認したり、色彩値（RGB値の16進数及び10進数）を取得するシンプルな配色確認ツールとなります。
    
    用途としては、ホームページやアプリケーションを作る時に配色のイメージを掴むためのものです。
    
    このcolortool.pyに関してのみGitHubにアップしています。
    
    https://github.com/dream-developer/project-tkinter
    
'''

#colortoo.py

import tkinter as tk

import tkinter.ttk as ttk

#1. pipなどであらかじめインストールが必要

import pyperclip

#スケール値を取得し、色彩値ラベル（10進数）の文字列を返す

def get_rgb_int_text(area):
    res = "("
    
    for rgb in rgbs:
        res = res + str(color_intvar[area][rgb].get()) + ", "
        
    res = res.rstrip(", ")
    
    return res + ")"
    
#スケール値を取得し、色彩値ラベル（16進数）の文字列を返す

def get_rgb_hex_text(area):
    res = "#"
    
    for rgb in rgbs:
        #16進数、左の"0x"削除、0文字埋めの2桁
        
        res = res + str(hex(color_intvar[area][rgb].get())).lstrip("0x").zfill(2)
        
    return res
    
#スケールが更新された

def update_scale(event = None):
    for area in areas:
        #配色エリアの色の更新
        
        if area == area_text:
            message["foreground"] = get_rgb_hex_text(area)
            
        else:
            message["background"] = get_rgb_hex_text(area)
            
        #色彩値ラベル（16進数）の更新
        
        label_hex[area]["text"] = get_rgb_hex_text(area)
        
        #色彩値ラベル（10進数）の更新
        
        label_int[area]["text"] = get_rgb_int_text(area)

#ラベルがクリックされた

def click_label(event):
    #ラベルのテキストをコピー
    
    pyperclip.copy(event.widget["text"])
    
root = tk.Tk()

root.geometry("400x500")

root.title("color tool")

#2. 配色エリア

message = tk.Message(font = ("MSゴシック", 20, "bold"))

m_pady = m_ipady = 20

m_padx = m_ipadx = 40

message["text"] = "色彩値ラベルをクリックで\n色彩値をコピーできます"

#配色エリアを配置

message.pack(padx = m_padx, pady = m_pady, ipadx = m_ipadx, ipady = m_ipady)

#3. 対象エリアと色のキー、キー配列

area_text = 0

area_back = 1

r = 0

g = 1

b = 2

areas = [area_text, area_back]

rgbs = [r, g, b]

#4. スケールのvariable

color_intvar = [[tk.IntVar(), tk.IntVar(), tk.IntVar()], #text[r, g, b]
                [tk.IntVar(), tk.IntVar(), tk.IntVar()]] #back[r, g, b]
                
#5. 色彩値ラベルのフレーム[text, back]

frame = [tk.Frame(root), tk.Frame(root)]

f_padx = f_pady = f_ipadx = f_ipady = 2

#色彩値ラベル（10進数/16進数）[text, back]

label_int = []

label_hex = []

l_padx = 5

l_ipadx = 30

l_pady = 5

l_ipady = 5

#6. RGB値スケールの配列。１次キーは対象エリア、２次キーはR値、G値,B値

scale = []

for area in areas:
    #色彩値ラベルを作成
    
    label_int.append(tk.Label(frame[area], relief = "groove"))
    
    label_hex.append(tk.Label(frame[area], relief = "groove"))
    
    #色彩値ラベルをフレームに配置
    
    label_hex[area].pack(side = "left", padx = l_padx, pady = l_pady, ipadx = l_ipadx, ipady = l_ipady)
    
    label_int[area].pack(side = "left", padx = l_padx, pady = l_pady, ipadx = l_ipadx, ipady = l_ipady) #([area]にしていました。1134行のlabel_hex[area].bindにエラー表示
    
    #色彩値ラベルをクリックしたらclick_label関数（ラベルのテキストをコピー）にコールバック
    
    label_hex[area].bind("<Button-1>", click_label)
    
    label_int[area].bind("<Button-1>", click_label)
    
    rgb_each = []
    
    for rgb in rgbs:
        color_intvar[area][rgb].set(255 - ((area + 1) * 80))
        
        rgb_each.append(ttk.Scale(root, from_ = 0, to = 255, variable = color_intvar[area][rgb], length = 255, command = update_scale))
        
    #area[r, g, b]
    
    scale.append(rgb_each)
    
for area in areas:
    #色彩値ラベルのフレームを配置
    
    frame[area].pack(padx = f_padx, pady = f_pady, ipadx = f_ipadx, ipady = f_ipady)
    
    for rgb in rgbs:
        scale[area][rgb].pack()
        
#7. あらかじめ配色エリアと色彩値ラベルを更新

update_scale()

root.mainloop()

'''
    1. pyperclipのインポート
    
    色彩値ラベルのクリックによる値のコピーで使用します。
    
    なおpyperclipは標準ライブラリではないので、pipなどであらかじめインストールが必要となります。
    
    2. 配色エリア
    
    テキストと背景の配色確認をする場所となります。
    
    扱いの簡単なMessageを使います。
    
    3. 対象エリアと色のキー、キー配列
    
    まず配色エリアはテキストと背景の２種類あり、そのさきは更にR値、G値、B値と枝分かれします。
    
    各々のウィジェット作成配置や、スケール調整処理などをそのまま書くことも可能ですが、今回はループ処理でできるだけコードを短くします。
    
    そのループで使うためのキー（テキスト、背景/R値、G値、B値）となります。
    
    4. スケールのvariable
    
    先にも述べたようにループを回していくのでウィジェット（とvariableや処理）は配列となっております。
    
    繰り返しになりますが、１次キーはテキストと背景（対象エリア）そこから２次キーとしてR,G,Bへ枝分かれが基本となります。
    
    5. 色彩値ラベルのフレーム
    
    配置も例によりループで行います。
    
    単純に.pack()で配置していきますが、ラベルは10進数、16進数と横並びにしたいので、フレームに入れています。
    
    6. RGB値スケールの配列。１次キーは対象エリア、２次キーはR値、G値、B値
    
    １次キー[text, back] ２次キーは[r, g, b]となります。
    
    後のループはまず対象エリア２種で回し、RGB値３種でネストされています。
    
    ここでウィジェットの作成や配置などを一気に行います。
    
    7. あらかじめ配色エリアと色彩値ラベルを更新
    
    update_scale()は配色エリアの色や色彩値ラベルの文字列を更新します。
    
    スケールのコールバックで定義していますが、ウィンドウ立ち上げの際にも呼び出します。
    
'''
