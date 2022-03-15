'''
    メッセージ(Message):枠の種類/幅
    
    メッセージラベルはラベルの複数行版です。
    
    ラベルも改行コード"\n"で改行自体はできますが、メッセージは必要に応じて改行をしてくれます。
    
'''

'''ex1

import tkinter as tk

root = tk.Tk()

root.geometry("300x200")

lb = tk.Label(text = "This is a Label. This is a Label. This is a label. ")

#メッセージの作成

ms = tk.Message(text = "This is a Message. This is a Message. This is a Message. ")

[widget.pack() for widget in (lb, ms)]

root.mainloop()

'''

'''
    枠の種類
    
    枠の種類はreliefオプションで設定します。
    
    設定値は"flat", "raised", "sunken", "groove", "ridge"とあります。
    
'''

'''ex2

import tkinter as tk

root = tk.Tk()

root.geometry("250x250")

ms_dict = {}

for relief_val in ["flat", "raised", "sunken", "groove", "ridge"]:

    #枠の種類はreliefを使う、ここではループで種類を回し設定
    
    ms_dict[relief_val] = tk.Message(text = relief_val, relief = relief_val, bd = 10)
    
    ms_dict[relief_val].pack()
    
root.mainloop()

'''

'''ex3

import tkinter as tk

root = tk.Tk()

root.geometry("300x270")

ms_dict = {}

for bw_int in range(1, 6):
    bw_str = str(bw_int)
    
    #枠の幅はborderwidthを使う、ここではループで1から5まで設定
    
    ms_dict[bw_str] = tk.Message(text = "borderwidth= " + bw_str, relief = "ridge", bd = bw_int)
    
    ms_dict[bw_str].pack()
    
root.mainloop()

'''

'''
    ボタン(Button):bitmapアイコン
    
    ボタンはcommandオプションで押下時に呼び出す関数を設定します（第1章で既に説明しました）
'''

'''ex4

import tkinter as tk

def btn_press():
    print("ボタンが押されました")
    
root = tk.Tk()

root.geometry("150x80")

#ボタンの作成、commandオプションで押下時に呼び出す関数を指定できる。

bt = tk.Button(text = "ボタン", command = btn_press)

bt.pack()

root.mainloop()

'''

'''
    bitmapアイコン
    
    bitmapアイコン（をつける場合）の種類はbitmapオプションで設定します。
    
    設定値は"info", "error", "gray12", "gray25", "gray50", "gray75", "hourglass", "questhead", "question", "warning"とあります。
    
'''

'''ex5

import tkinter as tk

root = tk.Tk()

bt_dict = {}

for bitmap_val in ["info", "error", "gray12", "gray25", "gray50", "gray75", "hourglass", "questhead", "question", "warning"]:

    #bitmapアイコンをつける事もできる。ここではループで種類を回し表示
    
    bt_dict[bitmap_val] = tk.Button(bitmap = bitmap_val)
    
    bt_dict[bitmap_val].pack()

root.mainloop()

'''

'''
    テキストボックス(Entry):Variable
    
    このテキストボックスも第1章にて少し触れましたが、.Entry()で作成し、.get()で内容を取得します。
    
    またフォーカスも.focus_set()で当てることができます。
    
'''

'''
    テキストボックス(Entry):Variable
    
    このテキストボックスも第1章にて少し触れましたが、.Entry()で作成し.get()で内容を取得します。
    
    またフォーカスも.focus_set()で当てることができます。
'''

'''ex6

import tkinter as tk

def print_txtval():

    #内容の取得
    
    val_en = en.get()
    
    print(val_en)
    
root = tk.Tk()

#テキストボックスの作成

en = tk.Entry()

bt = tk.Button(text = "ボタン", command = print_txtval)

[widget.pack() for widget in (en, bt)]

#フォーカスを当てる

en.focus_set()

root.mainloop()

'''

'''
    テキストの削除は.delete(開始位置[, 終了位置])を使います。
    
    開始いちは必須です。開始位置のみの場合は指定位置の１文字削除となります。
    
    ・Entryオブジェクト.delete(2)を繰り返す
    
    "abcdef"→"abdef"→"abef"→"abef"→"abf"→"ab"→"ab"→"ab"
    
    ・Entryオブジェクト.delete(1, 3)を繰り返す
    
    "abcdef"→"adef"→"af"→"a"→"a"→"a"
    
    全部削除する場合は開始位置を0、終了位置をtkinter.END(tkinter.ENDは最後という意味を持つ)とします。
    
    ・Entryオブジェクト.delete(0, tkinter.END)の場合
    
    "abcdef"→""
    
    なお開始位置をtkinter.ENDとした場合は特に何もしません。
    
    ・Entryオブジェクト.delete(tkinter.END)の場合
    
    "abcdef"→"abcdef"
    
    #最初から最後まで削除
    
    en.delete(0, tk.END)
    
    追加
    
    テキストの追加は.insert(追加位置, 追加文字列)を使います。
    
    追加位置は先頭なら0、3であれば3、最後ならtkinter.ENDと指定します。
    
    en.insert(0, "先頭に追加")
    
    en.insert(3, "3の位置に追加")
    
    en.insert(tk.END, "最後に追加")
    
    更新
    
    とりあえず更新したいという場合は決して追加という方法もあります。
    
    en.delete(0, tk.END)
    
    en.insert(0, "更新しました")
    
    より良い方法としてtkinter.StringVar()を使います。
    
    StringVarはVariableのサブクラスです。StringVarオブジェクトを作成し部品のtextvariableオプションに設定、StringVarオブジェクトの.set()でテキストを更新します。
    
    1. まずStringVarのオブジェクトを作成します。（検証としてのprint）
    
'''

'''ex7

import tkinter as tk

#rootの定義をしないと.StringVar()使用時にエラーになる

root = tk.Tk()

strvar = tk.StringVar()

#strvar = tk.StringVar()

#strvar = tk.StringVar()

print(strvar)

print(type(strvar))

#strvar = tk.StringVar()を複数作成するとPY_VAR0, PY_VAR1, PY_VAR2と増えていきます。

'''

'''
    2. 部品のtextvariableオプションに設定します。
    
'''

'''ex8

import tkinter as tk

root = tk.Tk()

strvar = tk.StringVar()

en = tk.Entry(textvariable = strvar)

en.pack()

root.mainloop()

'''

'''
    3. 更新の際にはStringVarオブジェクトの.set()を使う
    
'''

'''ex9

import tkinter as tk

root = tk.Tk()

strvar = tk.StringVar()

en = tk.Entry(textvariable = strvar)

strvar.set("あいうえお")

en.pack()

root.mainloop()

'''

'''
    Variableサブクラスには他にもIntVarやBooleanVar等があり、例えばチェックボックス(CheckButton)の場合variableオプションにBooleanVarオブジェクトを渡します。
    
    それではバインドも合わせて試してみましょう。"<Return>"はEnterキー押下時の仮想イベントです。
    
'''

'''ex10

import tkinter as tk

def return_press(event):
    en_val = strvar.get()
    
    print(en_val)
    
    strvar.set("")

root = tk.Tk()

strvar = tk.StringVar()

en = tk.Entry(textvariable = strvar)

en.bind("<Return>", return_press)

en.pack()

root.mainloop()

#出力と同時にテキストボックスの中身はクリアされる

'''

'''
    テキストエリア(Text):折り返し/タブ/ScrolledText
    
    テキストエリアはテキストボックス(Entry)の複数行版です。
    
    tkinter.Text()で作成します。
    
'''

'''ex11

import tkinter as tk

root = tk.Tk()

tx = tk.Text()

tx.pack()

root.mainloop()

'''

'''
    折り返し設定
    
    テキストエリアの折り返しに関しては　wrapオプションで設定します。
    
    tkinter.CHAR        文字単位（デフォルト）
    tkinter.WORD        単語単位
    tkinter.NONE        折り返しをしない
    
    #単語単位で折り返し
    
    tx = tk.Text(wrap = tk.WORD)
    
    行数/文字数
    
    行数はheightオプション、文字数はwidthオプションで指定します。
    
    #5行、（1行につき）30文字
    
    tx = tk.Text(height = 5, width = 30)
    
    選択範囲の位置
    
    マウスでどこからどこまで洗濯しているかの位置を取得する場合は.index()を使用します。
    
    選択開始位置は"sel.first"、選択終了位置は"sel.last"を引数として渡します。
    
    "1.5"(1行目5文字目)のように何行の何文字目かが「.」区切りで返されます。
    
    ※ただし開始位置は「より後ろから」という形になるので"1.5"であれば1行目の6文字目から選択されているという意味になります。
    
'''

'''ex12

import tkinter as tk

def get_selpoint():
    #選択された開始/終了位置
    
    sel_start = tx.index("sel.first")
    
    sel_end = tx.index("sel.last")
    
    lb["text"] = "sel_start:{0}, sel_end:{1}".format(sel_start, sel_end)
    
root =tk.Tk()

lb = tk.Label()

tx = tk.Text(width = 30, height = 5)

bt = tk.Button(text = "選択範囲", command = get_selpoint)

[widget.pack() for widget in (lb, tx, bt)]

root.mainloop()

#root画面上部に最初は何も表示されていない。文字を入力して文字列のうち任意の範囲を指定してから"選択範囲"のボタンを押すと、画面上部に選択した範囲の開始文字と終了文字のラベルが表示される

'''

'''
    また単純にカーソルの位置を取得する場合は"insert"を引数として渡します。
'''

'''ex13

import tkinter as tk

def get_selpoint():
    #選択された開始/終了位置
    
    #sel_start = tx.index("sel.first")
    
    #sel_end = tx.index("sel.last")
    
    #lb1["text"] = "sel_start:{0}, sel_end:{1}".format(sel_start, sel_end)
    
    cursor_point = tx.index("insert")
    
    lb2["text"] = "cursor_point:{0}".format(cursor_point)
    
root =tk.Tk()

#lb1 = tk.Label()

lb2 = tk.Label()

tx = tk.Text(width = 30, height = 5)

bt = tk.Button(text = "選択範囲", command = get_selpoint)

[widget.pack() for widget in (lb2, tx, bt)] #ex12と同じ出力にcursor_pointの出力を加えて出力する場合はlb1の引数をlb2の前に[widget.pack() for widget in（lb1, lb2, tx, bt)]と加える

root.mainloop()

'''

'''
    選択範囲の内容取得
    
    まずテキストの取得は.get()でしますが、その取得範囲を引数にて指定することができます。
    
    1.5のように何行の何文字目かを「.」区切りで表記した文字列を取得開始位置は第１引数、取得終了位置は第２引数として渡します。
    
    ※ただし開始位置は「より後ろから」という形になるので"1.5"であれば１行目の６文字目からの取得となります。
    
'''

'''ex14

import tkinter as tk

def get_text():
    #内容の取得(1行6文字から3行4文字まで) テキスト入力で/改行/を入れ忘れると出力結果は３行以降も表示されるので注意（１行として認識される）
    
    print(tx.get("1.5", "3.4"))
    
root = tk.Tk()

tx = tk.Text(width = 30, height = 5)

bt = tk.Button(text = "1行6文字から3行4文字まで取得", command = get_text)

[widget.pack() for widget in (tx, bt)]

root.mainloop()

'''

'''
    では選択範囲の位置の取得と組み合わせて、選択範囲のテキストの取得をしてみましょう。
    
'''

'''ex15

import tkinter as tk

def print_selpoint():
    #選択範囲の内容取得
    
    sel_start = tx.index("sel.first")
    
    sel_end = tx.index("sel.last")
    
    print(tx.get(sel_start, sel_end))
    
root = tk.Tk()

tx = tk.Text(width = 30, height = 5)

bt = tk.Button(text = "選択範囲を出力", command = print_selpoint)

[widget.pack() for widget in (tx, bt)]

root.mainloop()

'''

'''
    追加
    
    テキストの追加は.insert(何行.何文字目, 追加文字列)で行い、追加位置は何行の何文字目かを「.」区切りで指定します。
    
    また単純にカーソルの位置に追加する場合は"insert"を引数として渡します。
    
    では文字列を追加してみましょう。
    
'''

'''ex16

import tkinter as tk

def ins_cursor_point():
    #テキストの追加
    
    tx.insert(tx.index("insert"), "+++++")
    
root = tk.Tk()

tx = tk.Text(width = 30, height = 5)

bt = tk.Button(text = "カーソル位置に+++++を追加", command = ins_cursor_point)

[widget.pack() for widget in (tx, bt)]

root.mainloop()

'''

'''
    ScrolledText
    
    tkinter.scrolledtextのクラスにあるScrolledTextで縦スクロール付きテキストエリアの作成をすることができます。
    
    （tkinter.scrolledtextのインポートが必要となります）
    
'''

'''ex17

import tkinter as tk

#tkinter.scrolledtextのインポート

import tkinter.scrolledtext as tksc

root = tk.Tk()

#縦スクロール付きテキストエリア

st = tksc.ScrolledText(width = 30, height = 5)

st.pack()

root.mainloop()

'''

'''
    ScrolledTextは単にスクロール付きのテキストエリアといった感じですが、各部品につけることの出来るスクロールばー（Scrollbar）も別途あります（他項で説明します）
    
    ちなみにtkinterがインストールされているフォルダのscrolledtext.pyを見れば、部品へのスクロールバーの付け方の参考になります。
    
'''

'''
    チェックボックス(Checkbutton)
    
    チェックボックスはtkinter.Checkbutton()で作成します。
    
'''

'''ex18

import tkinter as tk

root = tk.Tk()

root.geometry("250x100")

ck = tk.Checkbutton(text = "チェックボックス")

ck.pack()

root.mainloop()

'''

'''
    チェック状態
    
    内容の操作に関して、テキストボックスの項ではtkinter.StringVar()を使用し更新などを行いましたが、チェックボックスではtkinterBooleanVar()を使います。
    
    ・確認
    
    variableオプションに渡したBooleanVarオブジェクト.get()で真偽値を取得し判定します。
    
'''

'''ex19

import tkinter as tk

def get_ckval():
    #チェックされているかの判定
    
    lb["text"] = "チェックされている" if boolvar.get() else "チェックされていない"
    
root = tk.Tk()

root.geometry("250x100")

boolvar = tk.BooleanVar()

lb = tk.Label()

ck = tk.Checkbutton(text = "チェックボックス", variable = boolvar)

bt = tk.Button(text = "判定", command = get_ckval)

[widget.pack() for widget in (lb, ck, bt)]

root.mainloop()

#チェック判定のテキストはroot画面上部に出力されます

'''

'''
    ・更新
    
    variabelオプションに渡したBooleanVarオブジェクト.set()でbool値を更新できます。
    
'''

'''ex20

import tkinter as tk

def upd_ckval():
    #チェックの設定
    
    boolvar.set(not boolvar.get())
    
root = tk.Tk()

root.geometry("250x100")

boolvar = tk.BooleanVar()

#variableオプションにBooleanVarオブジェクトをセット

ck = tk.Checkbutton(text = "チェックボックス", variable = boolvar)

bt = tk.Button(text = "更新", command = upd_ckval)

[widget.pack() for widget in (ck, bt)]

root.mainloop()

#ボタン押下でチェックボックスにチェックがつく、もう一度更新ボタンを押すと外れる

'''

'''
    ラジオボタン(Radiobutton)
    
    ラジオボタンはtkinter.Radiobutton()で作成します。
    
    グループ化という特性上、基本的には以下の手順となります。
    
    1. tkinter.IntVarなどVariableのサブクラスを定義（これがグループ化の元となります）
    
    2. このIntVarにラジオボタンの初期値を.set()メソッドにて設定します。
    
    3. ラジオボタンを作成、valueオプションに値を指定します。
    
    4. ラジオボタンのvariableオプションにIntVarを渡します。
    
'''

'''ex21

import tkinter as tk

root = tk.Tk()

root.geometry("150x100")

root.title("Radiobutton")

intvar = tk.IntVar()

#初期値をセット

intvar.set(1)

#選択されていない状態にする場合はどれにも該当しない値を設定します。

#intvar.set(0)

#ラジオボタンを作成

rd1 = tk.Radiobutton(text = "ラジオ１", value = 1, variable = intvar)

rd2 = tk.Radiobutton(text = "ラジオ２", value = 2, variable = intvar)

[widget.pack() for widget in (rd1, rd2)]

root.mainloop()

'''

'''
    選択されている値は.get()で取得します。
    
    ※厳密にはvariableの値なので.set(0)の直後は当然0が取得されます。
    
'''

'''ex22

import tkinter as tk

def get_rdval():
    #選択値を取得する
    
    print(intvar.get())
    
root = tk.Tk()

root.geometry("150x100")

root.title("Radiovutton get")

intvar = tk.IntVar()

intvar.set(0)

rd1 = tk.Radiobutton(text = "ラジオ１", value = 1, variable = intvar)

rd2 = tk.Radiobutton(text = "ラジオ２", value = 2, variable = intvar)

bt = tk.Button(text = "選択値を出力", command = get_rdval)

[widget.pack() for widget in (rd1, rd2, bt)]

root.mainloop()

'''

'''
    tkinter.StringVarで値を文字列にすることもできます。
    
    またvariableオプションに渡すVariableオプジェクトごとにグループ化されることも確認しましょう。
    
'''

'''ex23

import tkinter as tk

def get_rdval():
    #選択値を取得する
    
    print(intvar.get())
    
root = tk.Tk()

root.geometry("150x150")

root.title("Radiovutton get")

intvar = tk.IntVar()

intvar.set(0)

strvar = tk.StringVar()

strvar.set("0")

#1つ目のグループ

rd1 = tk.Radiobutton(text = "ラジオ１", value = 1, variable = intvar)

rd2 = tk.Radiobutton(text = "ラジオ２", value = 2, variable = intvar)

#2つ目のグループ

rdabc = tk.Radiobutton(text = "ラジオ A B C", value = "abc", variable = strvar)

rddef = tk.Radiobutton(text = "ラジオ D E F", value = "def", variable = strvar)

bt = tk.Button(text = "選択値を出力", command = get_rdval)

[widget.pack() for widget in (rd1, rd2, rdabc, rddef, bt)]

root.mainloop()

#rd1のみ出力1になり、残りは全て2になっています

'''

'''
    スクロールバー(Scrollbar)/フレーム(Frame)
    
    以前の項でScrolledTextで縦スクロール付きのテキストエリアの作成をしましたが、今回は各部品にスクロールバーを設定する方法を説明します。
    
    スクロールばーは単体で使うものではなく、各部品と組み合わせて使うものです。
    
    基本的には以下の手順となります。
    
    1. フレームを作成する
    
        作成時に幅と高さの設定もしておきましょう。
        
    2. スクロールバーを作成する
    
        マスターを上記1.で作成したフレームとします。
        
    3. スクロールバーを配置する時にsideやfillで位置などを指定する
    
        side = tkinter.RIGHTは右位置、fill = "y"は縦に一杯という意味です（詳細はレイアウトの章にて説明します。）
        
    4. 部品を作成する
    
        マスターを上記1.で作成したフレームとします。
        
    5. 部品の動きをスクロールバーに反映するようにする
    
        (x方向:xscrollcommand, y方向:yscrollcommand)オプションんにスクロールセットを指定
        
    6. スクロールバーの動きを部品に反映するようにする
    
        commandオプションに部品のビューを指定(x方向:xview, y方向:yview)
        
'''

'''ex24

import tkinter as tk

root = tk.Tk()

root.title("Scrollbar Frame")

root.geometry("300x200")

#1. フレームを作成する

fr = tk.Frame(width = 300, height = 200)

fr.pack()

#2. スクロールバーを作成する

sc = tk.Scrollbar(fr)

#3. スクロールバーを配置する時にsideやfillで位置などを指定する

sc.pack(side = tk.RIGHT, fill = "y")

#4. 部品を作成する

tx = tk.Text(fr)

tx.pack()

#5. 部品の動きをスクロールアーに反映するようにする

tx["yscrollcommand"] = sc.set

#6. スクロールバーの動きを部品に反映するようにする

sc["command"] = tx.yview

root.mainloop()

'''

'''
    特に「部品の動きをスクロールバーに反映するようにする」「スクロールバーの動きを部品に反映するようにする」の2つの処理は重要なので意識しましょう。
    
    javaとかなら勝手にやってくれますが、tkinterでは自分でやらなければ動作してくれません。
    
'''

'''
    水平スクロールバー
    
    x方向（横方向）のスクロールバーはorientオプションに"horizontal"（もしくは"h"）を渡します。
    
    下記コードではついでに折り返しも無しにしています。
    
'''

'''ex25

import tkinter as tk

root = tk.Tk()

root.title("Scrollbar Frame horizontal")

root.geometry("350x200")

fr = tk.Frame(width = 300, height = 200)

fr.pack()

sc = tk.Scrollbar(fr)

#x方向（横方向）にスクロールバー作成

scx = tk.Scrollbar(fr, orient = "horizontal")

sc.pack(side = tk.RIGHT, fill = "y")

#下位置、横に一杯

scx.pack(side = tk.BOTTOM, fill = "x")

tx = tk.Text(fr)

#折り返しをしない

tx["wrap"] = tk.NONE

tx.pack()

tx["yscrollcommand"] = sc.set

#部品の動きをx方向（横方向）スクロールバーに反映

tx["xscrollcommand"] = scx.set

sc["command"] = tx.yview

#x方向（横方向）スクロールバーの動きを部品に反映

scx["command"] = tx.xview

root.mainloop()

'''

'''
    ちなみにy方向（縦方向）は"vartical"（もしくは"v"）ですが、デフォルト値なので使う機会は明示的な書き方をしたい場面ぐらいでしょう。
    
'''

'''
    ラベルフレーム(LabelFrame)
    
    ラベルフレームはその名の通り、ラベル付きのフレームとなります。
    
    よくチェックボックスやラジオボタンに使われます。
    
    tkinter.LabelFrame()で作成します。
    
'''

'''ex26

import tkinter as tk

root = tk.Tk()

root.geometry("250x130")

root.title("LabelFrame")

#ラベルフレームを作成

frame = tk.LabelFrame(root, text = "ラベルフレーム", foreground = "#008800")   #tk.Labelにしていました

intvar = tk.IntVar()

intvar.set(0)

radio1 = tk.Radiobutton(frame, text = "ラジオ１", value = 1, variable = intvar)

radio2 = tk.Radiobutton(frame, text = "ラジオ２", value = 2, variable = intvar)

radio3 = tk.Radiobutton(frame, text = "ラジオ３", value = 3, variable = intvar)

[widget.pack() for widget in (frame, radio1, radio2, radio3)]

root.mainloop()

'''

'''
    ラベルの位置
    
    ラベルの位置はlabelanchorオプションにて8方向に設置できます。
    
    n       北（上）
    ne      北東（右上）
    e       東（右）
    se      南東（右下）
    s       南（下）
    sw      南西（左下）
    w       西（左）
    nw      北西（左上:デフォルト）
    
'''

'''ex27

import tkinter as tk

root = tk.Tk()

root.geometry("200x150")

root.title("labelanchor")

frame1 = tk.LabelFrame(root, text = "n", labelanchor = "n", width = 60, height = 40)

frame2 = tk.LabelFrame(root, text = "ne", labelanchor = "ne", width = 60, height = 40)

frame3 = tk.LabelFrame(root, text = "e", labelanchor = "e", width = 60, height = 40)

frame4 = tk.LabelFrame(root, text = "se", labelanchor = "se", width = 60, height = 40)

frame5 = tk.LabelFrame(root, text = "s", labelanchor = "s", width = 60, height = 40)

frame6 = tk.LabelFrame(root, text = "sw", labelanchor = "sw", width = 60, height = 40)

frame7 = tk.LabelFrame(root, text = "w", labelanchor = "w", width = 60, height = 40)

frame8 = tk.LabelFrame(root, text = "nw", labelanchor = "nw", width = 60, height = 40)

frame1.grid(column = 1, row = 0)

frame2.grid(column = 2, row = 0)

frame3.grid(column = 2, row = 1)

frame4.grid(column = 2, row = 2)

frame5.grid(column = 1, row = 2)

frame6.grid(column = 0, row = 2)

frame7.grid(column = 0, row = 1)

frame8.grid(column = 0, row = 0)

root.mainloop()

'''

'''
    枠の種類
    
    メッセージの項でも触れましたが、枠の種類はreliefオプションで設定します。
    
    設定値は"flat", "raised", "sunken", "groove", "ridge"とあります。
    
'''

'''ex28

import tkinter as tk

root = tk.Tk()

root.geometry("300x150")

root.title("LabelFrame relief")

frame1 = tk.LabelFrame(root, text = "flat", relief = "flat", width = 60, height = 40)

frame2 = tk.LabelFrame(root, text = "raised", relief = "raised", width = 60, height = 40)

frame3 = tk.LabelFrame(root, text = "sunken", relief = "sunken", width = 60, height = 40)

frame4 = tk.LabelFrame(root, text = "groove", relief = "groove", width = 60, height = 40)

frame5 = tk.LabelFrame(root, text = "ridge", relief = "ridge", width = 60, height = 40)

frame1.grid(column = 0, row = 0)

frame2.grid(column = 1, row = 0)

frame3.grid(column = 2, row = 0)

frame4.grid(column = 0, row = 1)

frame5.grid(column = 1, row = 1)

root.mainloop()

#なおラベルフレームの枠のデフォルトは"groove"となります。

'''

'''
    リストボックス(Listbox)
    
    リストボックスはListboxで作成し、.insert(index, item)でアイテムの追加をしていきます。
    
    インデックスはアイテムの追加位置です。最後に追加する場合はtkinter.ENDを渡します。
    
    よくあるのはアイテムの配列をループで回し、.insert(tkinte.END, item)のような形で追加していくパターンです(itemは項目の文字列)。
    
    またあらかじめ高さも指定しておきましょう。
    
'''

'''ex29

import tkinter as tk

root = tk.Tk()

root.geometry("250x150")

root.title("listbox")

listbox = tk.Listbox(root, height = 5)

for item in ["北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州沖縄"]:
    listbox.insert(tk.END, item)
    
listbox.pack()

root.mainloop()

#listvariabeleオプション

#.insert()を使わずにStringVarをlistvariableオプションに渡すやり方もあります。

'''

'''
    選択方式
    
    選択方式はselectmodeオプションで指定します。
    
    browse(デフォルト)       単数選択のみ。ドラッグで洗濯の移動ができる。
    
    single          単数選択のみ。browseとの違いはドラッグによる選択の移動ができない。
    
    muliple         クリックで複数行選択可。もう一度クリックで選択解除。
    
    extended        ドラッグで複数行選択可。さらにctrlキーを押しながらで洗濯を跨ぐこともできる。
    
    選択されているアイテムのインデックスを取得
    
    選択されているアイテムはcurselection()で取得します。
    
    返り値は単数複数関係なくインデックスのタプルとなります（未選択の場合は空のタプル）。
    
'''

'''ex30

import tkinter as tk

def get_listitem():
    #選択中アイテムのインデックス
    
    print(listbox.curselection())
    
root = tk.Tk()

root.geometry("280x150")

root.title("get listitem")

strvar = tk.StringVar()

strvar.set(["北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州沖縄"])

#１行で書くこともできるstrvar = tk.StringVar(value=["北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州沖縄"])
#アイテムの定義にStringVarを使用、また複数行選択可にする

listbox = tk.Listbox(root, listvariable = strvar, selectmode = "multiple", height = 5)

button = tk.Button(text = "選択値を出力", command = get_listitem)

[widget.pack() for widget in(listbox, button)]

root.mainloop()

'''

'''
    イベント
    
    選択時の仮想イベントは<<ListboxSelect>>を指定します。
    
    ＃選択時に第2引数に指定したget_listitem関数がコールバックされる
    
    listbox.bind("<<ListboxSelect>>", get_listitem)
    
    アイテムの選択/解除
    
    ・選択
    
    プログラムが話で動的にアイテムを選択する場合は.selet_set()を使います。
    
    .select_set(2)ならインデックス2を選択.select_set(1, 3)ならインデックス1から3までを選択.select_set(0, tkinter.END)なら全選択となります。
    
    ・解除
    
    また解除をする時は.select_clear()を使います。引数の渡し方は.select_set()と同じです。
    
'''

'''ex31

import tkinter as tk

def set_allitem():
    #0,tkinter.ENDですべtのアイテムが選択される
    
    listbox.select_set(0, tk.END)
    
def clear_item():
    #引数の渡し方は.select_set()と同じ
    
    listbox.select_clear(0, tk.END)
    
root = tk.Tk()

root.geometry("280x150")

root.title("listbox set clear")

strvar = tk.StringVar()

strvar.set(["北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州沖縄"])

listbox = tk.Listbox(root, listvariable = strvar, selectmode = "multiple", height = 5)

button1 = tk.Button(text = "全選択", command = set_allitem)

button2 = tk.Button(text = "全解除", command = clear_item)

[widget.pack() for widget in(listbox, button1, button2)]

root.mainloop()

#全選択押下で全て選択され、全解除押下で全て解除される

'''

'''
    アイテムの要素数
    
    カスタム的な選択/解除をしたければ対象インデックスを格納した配列などで回せば良いかと思います。
    
    偶数なら下記のコードのような形でしょうか。リストボックスのアイテム数は.size()で取得します。
    
'''

'''ex32

import tkinter as tk

def set_eventitem():
    #.size()で要素数を取得しループ
    
    for i in range(1, listbox.size(), 2):
        listbox.select_set(i)

  
  #[listbox.select_set(i) for i in range(1, listbox.size(), 2)]
  
#def delete_eventitem():
#    listbox.delete(0, tk.END)
        
root = tk.Tk()

root.geometry("280x250")

root.title("listbox size")

strvar = tk.StringVar()

strvar.set(["北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州沖縄"])

listbox = tk.Listbox(root, listvariable = strvar, selectmode = "multiple", height = 5)

button1 = tk.Button(text = "偶数選択", command = set_eventitem)

#button2 = tk.Button(text = "全削除", command = delete_eventitem)

[widget.pack() for widget in(listbox, button1)]

#[widget.pack() for widget in(listbox, button1, button2)]

root.mainloop()

#ちなみにこのような偶数など単純なパターンのアイテム選択指定の場合

#[listbox.select_set(i) for i in range(1, listbox.size(), 2]

#のように内包表記で書くこともできます

'''

'''
    アイテムの削除
    
    アイテムの削除は.delete()を使います。引数の渡し方は.select_set()と同じです。
    
    #.delete()でアイテムの削除、0, tk.ENDで最初から最後まで
    
    listbox.delete(0, tk.END)
    
    なお削除するという事は、当然要素数が変わるという事です。したがってループで回す場合の.size()は使えないので注意が必要です。
    
'''

'''ex33

import tkinter as tk

def set_eventitem():
    #.size()で要素数を取得しループ(内包表記)

  [listbox.select_set(i) for i in range(1, listbox.size(), 2)]
  
def delete_eventitem():
    listbox.delete(0, tk.END)
        
root = tk.Tk()

root.geometry("280x250")

root.title("listbox size")

strvar = tk.StringVar()

strvar.set(["北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州沖縄"])

listbox = tk.Listbox(root, listvariable = strvar, selectmode = "multiple", height = 5)

button1 = tk.Button(text = "偶数選択", command = set_eventitem)

button2 = tk.Button(text = "全削除", command = delete_eventitem)

[widget.pack() for widget in(listbox, button1, button2)]

root.mainloop()

'''

'''
    スクロールバー追加/指定アイテムを見える状態にする
    
    ・スクロールバー追加
    
    スクロールバー追加の詳細は別の項で説明しているので、今回の怪セウはコメントへ簡単に書くのみとします。
    
    ・指定アイテムを見える状態にする
    
    .selectset()は選択したアイテムが表示の範囲が立った場合、自動で移動する事はないので.see()と組み合わせましょう。
    
    .see()は引数に渡したインデックスのアイテムが見える状態にする関数です。
    
'''

'''ex34

import tkinter as tk

root = tk.Tk()

root.geometry("280x250")

root.title("listbox scrollbar")

frame = tk.Frame(width = 300, height = 200)

frame.pack()

scrollbar = tk.Scrollbar(frame)

#side = tkinter.RIGHTは右位置、fill = "y"は縦にいっぱいと言う意味

scrollbar.pack(side = tk.RIGHT, fill = "y")

#マスターはウィンドウではなくフレーム

listbox = tk.Listbox(frame, height = 10)

[listbox.insert(tk.END, "アイテム{0}".format(i)) for i in range(1, 21)]     #[0]になっていました

listbox.pack()

#部品の動きをスクロールバーに反映するようにする

listbox["yscrollcommand"] = scrollbar.set

#スクロールバーの動きを部品に反映するようにする

scrollbar["command"] = listbox.yview

#指定のインデックスを選択し、さらに見える状態にする

default_index = 14

listbox.select_set(default_index)

listbox.see(default_index)

root.mainloop()

'''

'''
    コンボボックス(Combobox)
    
    コンボボックスはtkinter.ttk.Combobox()で作成します。
    
    最低限必要な事は以下の3つです。
    
    1. tkinter.ttkのインポート
    
    2. itemはvaluesにタプルで渡す
    
    3. 入力値または選択されたitemは.get()で取得する
    
'''

'''ex35

import tkinter as tk

#Comboboxはtkinter.ttkにある

import tkinter.ttk as ttk

def get_comboitem():
    #.get()で取得する
    
    print(combobox.get())
    
root = tk.Tk()

root.geometry("280x150")

root.title("combobox")

#itemはvaluesにタプルで渡します

combobox = ttk.Combobox(root, values = ("北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州沖縄")) #values = ("北海道",　の ( が抜けていました

button = tk.Button(text = "入力/選択値を出力", command = get_comboitem)

combobox.pack()

button.pack()

root.mainloop()

'''

'''
    ステータス
    
    コンボボックスはさしづめテキストボックス兼ドロップダウンリストといったところでしょうか。
    
    stateオプションに"readonly"を渡せば、機能的にはドロップダウンリストと変わりません。
    
    stateオプション
    
    normal          入力/選択可(デフォルト)
    readonly        選択のみ可
    disable         無効化
    
    disable以外で、選択時のアローボタンがクリックで無反応の時はダブルクリックにしたりtabキーでフォーカスを当てたりしてみましょう。
    
    #読み込み専用なので選択値の編集は不可、機能的にはドロップダウンリストと同じ
    
    combobox["state"] = "readonly"
    
'''

'''ex36

import tkinter as tk

#Comboboxはtkinter.ttkにある

import tkinter.ttk as ttk

def get_comboitem():
    #.get()で取得する
    
    print(combobox.get())
    
root = tk.Tk()

root.geometry("280x150")

root.title("combobox")

#itemはvaluesにタプルで渡します

combobox = ttk.Combobox(root, values = ("北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州沖縄"))

combobox["state"] = "normal"

button = tk.Button(text = "入力/選択値を出力", command = get_comboitem)

combobox.pack()

button.pack()

root.mainloop()

'''

'''
    イベント
    
    選択時の仮想イベントは<<ComboboxSelected>>を指定します。
    
'''

'''ex37

import tkinter as tk

import tkinter.ttk as ttk

def get_comboitem(event):
    print(combobox.get())
    
root = tk.Tk()

root.geometry("280x150")

root.title("combobox event")

combobox = ttk.Combobox(root, values = ("北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州沖縄"))

#コンボボックス選択のイベントは<<ComboboxSelected>>を渡す

combobox.bind("<<ComboboxSelected>>", get_comboitem)

#入力時のEnter用

combobox.bind("<Return>", get_comboitem)

combobox.pack()

root.mainloop()

#なおコンボボックスは入力もあるので、<Return>のキーバインドもしておくと良いでしょう。
#もちろんstate = "readonly"の場合は<<ComboboxSelected>>だけで良いです。

'''

'''
    入力/選択
    
    ・入力
    
    入力は.set(value)でします。
    
    #入力は.set(value)でする
    
    combobox.set("あらかじめ入力")
    
    ・選択
    
    選択は.current(index)を使います。
    
    #選択は.current(index)でする
    
    combobox.current(4)
    
'''

'''ex38

import tkinter as tk

#Comboboxはtkinter.ttkにある

import tkinter.ttk as ttk

def return_press(event):
    en_val = strvar.get()
    print(en_val)
    strvar.set("")
    
def get_comboitem():
    #.get()で取得する
    
    print(combobox.get())
    
root = tk.Tk()

root.geometry("280x150")

root.title("combobox")

#itemはvaluesにタプルで渡します

combobox = ttk.Combobox(root, values = ("北海道", "東北", "関東", "中部", "近畿", "中国", "四国", "九州沖縄"))

#.setか.currentのどちらか選択

combobox.set("ドロップボックスから選択")

#combobox.current(4)


# Enterキー押下でテキスト入力値の出力

strvar = tk.StringVar()

en = tk.Entry(textvariable = strvar)

en.bind("<Return>", return_press)

en.pack()

button = tk.Button(text = "入力/選択値を出力", command = get_comboitem)

combobox.pack()

button.pack()

root.mainloop()

'''

'''
    スピンボックス(Spinbox)
    
    スピンボックスは上下のアローボタンにて数値の調整をするウィジェットです。
    
    tkinter.Spinbox(from_ = 下限値, to = 上限値, increment = 増減値)
    
    ※「from」ではなく「from_」となる点に注意
    
    textvariable        Variableオブジェクト
    command             コールバック関数（アローボタンの押下）
    state               状態(normal, reaonly, disabled)
    value               タプルで項目の設定
    
'''

'''ex39

import tkinter as tk

def upd_spinbox(event = None):
    label["text"] = var_spinbox.get()
    
root = tk.Tk()

root.geometry("280x250")

root.title("spinbox")

var_spinbox = tk.StringVar()

label = tk.Label(root, text = "スピンボックスの値")

#スピンボックス: -10から10まで0.5ずつ

spinbox = tk.Spinbox(root, from_ = -10, to = 10, increment = 0.5, textvariable = var_spinbox, command = upd_spinbox)

var_spinbox.set(0.0)

spinbox.bind("<Return>", upd_spinbox)

[widget.pack() for widget in (label, spinbox)]

root.mainloop()

'''

'''
    state = "readonly"選択のみにした場合
    
    spinbox = tk.Spinbox(root, from_ = -10, to = 10, increment = 0.5, state = "reaonly", textvariable = var_spinbox, command = upd_spinbox)
    
    reakonlyなので、アローボタンによる選択はできるが、テキスト入力はできない。
    
    下のアローボタンを2回押下後の状態、0.5ずつ減るので-1.0となる
    
    またvalueにタプルを渡すことによりテキスト項目の設定もできます。
    
    #valueにタプルを渡しテキスト項目の設定
    
    spinbox = tk.Spinbox(root, value = tuple("item_{0}".format(i) for i in range(1, 11)), textvariable = var_spinbox, command = upd_spinbox)
    
'''

'''ex40

import tkinter as tk

def upd_spinbox(event = None):
    label["text"] = var_spinbox.get()
    
root = tk.Tk()

root.geometry("280x250")

root.title("spinbox")

var_spinbox = tk.StringVar()

label = tk.Label(root, text = "スピンボックスの値")

#スピンボックス: -10から10まで0.5ずつ

spinbox = tk.Spinbox(root, from_ = -10, to = 10, increment = 0.5, textvariable = var_spinbox, command = upd_spinbox)

#state = "readonly"の場合

#spinbox = tk.Spinbox(root, from_ = -10, to = 10, increment = 0.5, state = "readonly", textvariable = var_spinbox, command = upd_spinbox)

#タプルを渡した場合

#spinbox = tk.Spinbox(root, value = tuple("item_{0}".format(i) for i in range(1, 11)), textvariable = var_spinbox, command = upd_spinbox)

var_spinbox.set(0.0)

spinbox.bind("<Return>", upd_spinbox)

[widget.pack() for widget in (label, spinbox)]

root.mainloop()

'''

'''
    スケール(Scale)
    
    スケールはバーにて数値の調整をするウィジェットです。
    
    スライダー/スライドバーと言ったほうがピンとくる方も多いかと思います。
    
    なおスケールはtkinter.ttkの中にあります。
    
    tkinter.ttk.Scale(from_ = 下限値, to = 上限値)
    
    variable            Variableオブジェクト
    command             コールバック関数
    orient              方向(horizontal, vertical)
    length              長さ(ピクセル単位)
    
'''


'''ex41

import tkinter as tk

#tkinter.ttkのインポート

import tkinter.ttk as ttk

def upd_scale(event = None):
    message["text"] = "callback\n{0}\n\nIntVar.get()\n{1}\n\nscale.get()\n{2}\n\nscale[\"value\"]\n{3}".format(event, var_scale.get(), scale.get(), scale["value"])
    
root = tk.Tk()

root.geometry("280x250")

root.title("scale")

message = tk.Message(root, width = 500, aspect = 300, text = "scale value")

#浮動小数点数の場合

#var_scale = tk.DoubleVar()

var_scale = tk.IntVar()

#スケールの作成

scale = ttk.Scale(root, from_ = -10, to = 10, variable = var_scale, length = 150, command = upd_scale)

[widget.pack() for widget in(message, scale)]

var_scale.set(0)

root.mainloop()

#IntVar以外は不動小数点にて取得されている

'''

'''
    値の取得方法はたくさんあり浮動小数点数となりますが、variableはIntVar()を渡すと整数になります。
    
    またコメントも書いておきましたが、DboubleVar()で浮動小数点数にすることもできます。

'''

'''
    メニュー(Menu)
    
    メニューの作成はまずウィンドウにメニューバーを作り、各メニューをつけ、メニューごとにメニューアイテムを追加していきます。
    
    基本的には以下の手順となります。
    
    1. メニューバーを作成
    
        tkinter.Menu()で作成。マスターとしてウィンドウを渡します。
        
    2. メニューを作成
    
        tkinte.Menu()で作成。マスターとしてメニューバーを渡します。
        
    3. メニューにアイテムを追加
    
        .add_command(label = アイテム名, command = コールバック関数)で追加します。
        
    4. メニューバーにメニューをカスケード
    
        .add_cascade(label = メニュー名, menu = メニューオブジェクト)でカスケードします。
        
    5. ウィンドウにメニューバーを追加
    
        menuオプションにメニューバーを渡します。
        
    なおセパレーターは.add_separator()でつけます。
    
'''

'''ex42

import tkinter as tk

def file_open():
    label["text"] = "File open"
    
def file_save():
    label["text"] = "File save"
    
def edit_copy():
    label["text"] = "Edit copy"
    
def edit_paste():
    label["text"] = "Edit paste"
    
root = tk.Tk()

root.geometry("200x100")

root.title("menu")

#1. メニューバーを作成(マスターはウィンドウ)

menubar = tk.Menu(root)

#2. メニューを作成(マスターはメニューバー)、tearoff = Falseにして切り取らせないようにする

menu1 = tk.Menu(menubar, tearoff = False)

#3. メニューにアイテムを追加

menu1.add_command(label = "open", command = file_open)

#セパレーター

menu1.add_separator()

menu1.add_command(label = "save", command = file_save)

#4. メニューバーにメニューをカスケード

menubar.add_cascade(label = "file", menu = menu1)

menu2 = tk.Menu(menubar, tearoff = False)

menu2.add_command(label = "copy", command = edit_copy)

menu2.add_command(label = "paste", command = edit_paste)

menubar.add_cascade(label = "edit", menu = menu2)

#5. ウィンドウにメニューバーを追加

root["menu"] = menubar

label = tk.Label(root)

label.pack()

root.mainloop()

#メニューバーが出ない

'''

'''
    メニューを入れ子にする場合は、マスターを親メニューとしたメニューを作成し、親メニューにカスケードします。
    
'''

'''ex43

import tkinter as tk

def file_new():
    label["text"] = "File new"
    
def file_open():
    label["text"] = "File open"
    
def file_save():
    label["text"] = "File save"
    
root = tk.Tk()

root.geometry("300x100")

root.title("menu cascade")

menubar = tk.Menu(root)

menu1 = tk.Menu(menubar, tearoff = False)

menubar.add_cascade(label = "file", menu = menu1)

#メニューを作成(マスターは親メニュー)

menu11 = tk.Menu(menu1, tearoff = False)

#メニューにアイテムを追加

menu11.add_command(label = "new", command = file_new)

menu11.add_command(label = "open", command = file_open)

#親メニューにメニューをカスケード

menu1.add_cascade(label = "new/open", menu = menu11)

menu1.add_command(label = "save", command = file_save)

root["menu"] = menubar

label = tk.Label(root)

label.pack()

root.mainloop()

#メニューバーが出ない

#メニューバーのfileをクリック、親メニューのnew/openにカーソルを合わせると子メニュー(サブメニュー)が表示される<はずですが。>

'''

'''
    ファイルダイアログ
    
    ファイルダイアログはファイルを選択し、パスを取得するためのウィジェットです。
    
    ファイルパスを取得すれば、それをもとに単純な置換作業から更にはnumpy/pandasでデータ分析、matplotlibによるグラフ化、openpyxlによるエクセルの加工などなど、多くの事ができるようになります。
    
    filedialog.askopenfilename(filetypes = ファイルタイプのリスト, initialdir = 初期ディレクトリ)
    
    以下が簡単な手順です。
    
    
    1. tkinter内のfiledialogクラスをインポートします。
    
    2. initialdirを省略すると作業ディレクトリが初期ディレクトリ、filetypesを省略すると特にファイルタイプなしとなります。
    
    3. ファイルタイプは("ファイルタイプ名", "ファイルタイプ")のタプルとなり、これのリストとなります。
    
        (例).txt, .py, すべてのファイルの場合
        
        [("text file", "*.txt"), ("py file", "*.py"), ("all file", "*")]
        
'''

'''ex44

import tkinter as tk

#tkinter内のfiledialogクラスをインポート

from tkinter import filedialog

def get_filepath():
    #.txt, .py, すべてのファイルの場合
    
    filetype_list = [("text file", "*.txt"), ("py file", "*.py"), ("all file", "*")]
    
    #ファイルパスの取得
    
    filepath = filedialog.askopenfilename(initialdir = "/home/suteabl2", filetypes = filetype_list, title = "select file")
    
    message["text"] = filepath
    
root = tk.Tk()

root.geometry("650x100")

root.title("filedialog")

message = tk.Message(root,text = "file path", width = 600)

button = tk.Button(text = "get_filepath", command = get_filepath)

[widget.pack() for widget in(message, button)]

root.mainloop()

'''

'''
    ファイルダイアログの役目としては、.askopenfilename()でファイルのパスを取得すれば、あとはどうとでもなりますが、他にも関数が用意されていますので活用されて位はいかがでしょうか。

    特に.asksaveasfilename()と.asksaveasfile()は既存ファイルがある時には確認メッセージを出してくれます。
    
    .askopenfilename()          ファイルのパスを取得
    .askopenfilenenemes()         複数のファイルのパスをタプルで取得
    .askopenfile()              ファイルオブジェクト(読み込みモード)の取得
    .askopenfiles()             複数ファイルオブジェクト(読み込みモード)をリストで取得
    .asksaveasfilename()            書き込みファイルのパスを取得
    .asksaveasfile()            ファイルオブジェクト（書き込みモード）の取得
    .askdirectory()             ディレクトリのパスを取得（filetypesはないので、指定するとエラー）
'''

'''
    ※ファイルオブジェクトの取得において、ファイルの選択ができない場合はファイル権限を変えてみましょう。
    
'''

'''ex45

import tkinter as tk

import tkinter.scrolledtext as tksc

#tkinter内のfiledialogクラスをインポート

from tkinter import filedialog

def get_filepath():
    #.txt, .py, すべてのファイルの場合
    
    filetype_list = [("text file", ".txt"), ("py file", ".py"), ("all file", "*")]
    
    #ファイルオブジェクト（読み込みモード）
    #ファイルの選択ができない場合はファイル権限を変えてみましょう。
    
    fileobj = filedialog.askopenfile(initialdir = "/home/suteabl2", filetypes = filetype_list, title = "select file")
    
    if fileobj is not None:
        msessage["text"] = str(fileobj)
        
        content = fileobj.read()
        
        scrolledtext.insert(tk.END, content)
        
        fileobj.close()
        
root = tk.Tk()

root.geometry("550x250")

root.title("filedialog_read")

msessage = tk.Message(root, text = "file path", width = 550)

button = tk.Button(text = "get_filepath", command = get_filepath)

scrolledtext = tksc.ScrolledText(root, height = 10, width = 70)

[widget.pack() for widget in (msessage, button, scrolledtext)]

root.mainloop()

'''

'''
    ただ.askopenfile関数等は融通が効かないことに、なぜかencodingオプションがありません(python3.6.5ではbad optionエラーになります)
    
    したがって読み込むファイルのエンコードによっては余計な手間が増えるので、askopenfilename()でファイルパス取得しopen関数などで読み込んだほうがいいと思います。
    
'''

'''
    メッセージボックス
    
    メッセージボックスはメッセージダイアログを表示するウィジェットです。
    
    tkinter内のmessageboxクラスをインポートして使います。
    
    messagebox.showinfo("タイトル", "メッセージ")
    
    .showinfo()         情報メッセージ
    .showwarning()      警告メッセージ"ok"("ok")
    .showerror()        エラーメッセージ"ok"("ok")
    .askquestion()      questionメッセージ"yes"/"no"("no")
    .askyesno()         yes/noメッセージTrue/False(False)
    .askokcancel()      ok/cancelメッセージTrue/False(False)
    .askretrycancel()   retry/cancelメッセージTrue/False(False)
    
    説明欄の()内はメッセージダイアログ右上の[x]押下時の戻り値です。
    
'''

'''ex46

import tkinter as tk

from tkinter import messagebox

def msg_info():
    #情報メッセージ
    
    label["text"] = str(messagebox.showinfo("info", "info message"))
    
def msg_warning():
    #警告メッセージ
    
    label["text"] = str(messagebox.showwarning("warning", "warning message"))
    
def msg_error():
    #エラーメッセージ
    
    label["text"] = str(messagebox.showerror("error", "error message"))
    
def msg_question():
    #questionメッセージ
    
    label["text"] = str(messagebox.askquestion("question", "question message"))
    
def msg_yesno():
    #yes/noメッセージ
    
    label["text"] = "True(bool値)" if messagebox.askyesno("yes/no", "yes/no message") else "False(bool値)"
    
def msg_okcancel():
    #ok/cancelメッセージ
    
    label["text"] = "True(bool値)" if messagebox.askokcancel("ok/cancel", "ok/cancel message") else "False(bool値)"
    
def msg_retrycancel():
    #retry/cancelメッセージ
    
    label["text"] = "True(bool値)" if messagebox.askretrycancel("retyr/cancel", "retry/cancel message") else "False(bool値)"
    
root = tk.Tk()

root.geometry("650x100")

root.title("messagebox")

label = tk.Label(root, text = "message result")

button_info = tk.Button(root, text = "info", command = msg_info)

button_warning = tk.Button(root, text = "warning", command = msg_warning)

button_error = tk.Button(root, text = "error", command = msg_error)

button_question = tk.Button(root, text = "question", command = msg_question)

button_yesno = tk.Button(root, text = "yesno", command = msg_yesno)

button_okcancel = tk.Button(root, text = "okcancel", command = msg_okcancel)

button_retrycancel = tk.Button(root, text = "retrycancel", command = msg_retrycancel)

label.pack()

[widget.pack(side = tk.LEFT, padx = 5) for widget in (button_info, button_warning, button_error, button_question, button_yesno, button_okcancel, button_retrycancel)]

root.mainloop()

'''

'''
    タブを実装する
    
    タブを実装するにはtkinter.ttk.Notebook()を使います。
    
    仮想イベント
    
    <<NoteookTabChanged>>
    
    .tas()
    
    Notebookの持っているウィジェット名の一覧をタプルで返します。ここでいうウィジェット名はタブIDのことだと思ってください。
    
    .select()
    
    現在選択されているタブIDを返します。
    
    タブIDを渡すと、該当するタブが選択されます。
    
    基本的には以下の手順となります。
    
    1. tkinter内のttkクラスをインポート
        import tkinter.ttk as ttk
        
    2. Notebookオブジェクトを作成
        tkinter.ttk.Notebook()で作成します。
        
    3. タブとなるフレームを作成
        タブなのでマスターは基本的にNotebookにしておきましょう。
        
    4. Notebookにタブを追加
        .add()でNotebookにタブを追加
        
    なおウィンドウサイズが変わった時用にNotebookのレスポンシブを有効(expand = True)にしておくと良いでしょう。
    
'''

'''ex47

import tkinter as tk

#1. tkinter内のttkクラスをインポート

import tkinter.ttk as ttk

def press_button1():
    label["text"] = "pressed button1"
    
def press_button2():
    label["text"] = "pressed button2"
    
root = tk.Tk()

root.geometry("300x150")

root.title("Notebook")

#2. Notebookオブジェクトを作成

notebook = ttk.Notebook(root)

#3. タブとなるフレームを作成

tab1 = tk.Frame(notebook)

tab2 = tk.Frame(notebook)

#4. Notebookにタブを追加

notebook.add(tab1, text = "tab1")

notebook.add(tab2, text = "tab2")

#ウィンドウサイズが変わった時用にタブのレスポンシブを有効

notebook.pack(expand = True, fill = "both")

#tab1をマスターとしたウィジェット

label1 = tk.Label(tab1, text = "tab1 label")

button1 = tk.Button(tab1, text = "tab1 button1", command = press_button1)

#tab2をマスターとしたウィジェット

label2 = tk.Label(tab2, text = "tab2 label")

button2 = tk.Button(tab2, text = "tab2 button2", command = press_button2)

[widget.pack(pady = 10) for widget in (label1, button1, label2, button2)]

root.mainloop()

'''

'''
    タブの選択やバインドの実装例です
    
'''

import tkinter as tk

import tkinter.ttk as ttk

def press_button1():
    label["text"] = "pressed button1"
    
def press_button2():
    label["text"] = "pressed button2"
    
#タブ切り替え時のコールバック

def chg_tab(event):
    print(notebook.select())
    
root = tk.Tk()

root.geometry("300x150")

root.title("Notebook")

notebook = ttk.Notebook(root)

tab1 = tk.Frame(notebook)

tab2 = tk.Frame(notebook)

notebook.add(tab1, text = "tab1")

notebook.add(tab2, text = "tab2")

notebook.pack(expand = True, fill = "both")

label1 = tk.Label(tab1, text = "tab1 label1")

button1 = tk.Button(tab1 , text = "tab1 button1", command = press_button1)

label2 = tk.Label(tab2, text = "tab2 label2")

button2 = tk.Button(tab2, text = "tab2 button2", command = press_button2)

[widget.pack(pady = 10) for widget in(label1, button1, label2, button2)]

#Notebookの持っているタブID(ウィジェット名)

tabids = notebook.tabs()

print(tabids)

#現在選択されているタブID（ウィジェット名）

print(notebook.select())

#タブ切り替え時のコールバック

notebook.bind("<<NotebookTabChanged>>", chg_tab)

#２番目のタブを選択

notebook.select(tabids[1])

print(notebook.select())

root.mainloop()

'''
    5行の出力の内訳

    ・notebookの持っているタブIDをタプルで出力（print関数）
    ・作成直後に選択されているタブIDを.select()メソッドで出力（print関数）
    ・.select(tab2のタブID)メソッドでtab2を選択した際のタブIDを出力（バインドのコールバック）
    ・tab2選択後の.select()メソッドの出力（print関数）
    ・root.mainloop()でウィンドウ立ち上げ時のNotebookTabDhangedイベント発生におけるタブID出力（バインドのコールバック）

    ※つまりウィンドウを立ち上げ時にもNotebookTabChangedイベントが発生します。
    
'''

'''
    Message.pyはここの第3章まで
    
    第4章　レイアウトの基本からはlayout.pyに記載します
    
'''
