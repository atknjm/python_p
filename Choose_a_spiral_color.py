import tkinter as tk #ボタン作成のためにtkinterをインポート
import turtle as Tu #図形描画のためにturtleをインポート

#Step1：ボタン選択のウィンドウを表示
base = tk.Tk()
base.geometry('400x200') #ウィンドウのサイズ（幅×高さ）
base.title('色選択') #ウィンドウのタイトル

#ボタン押下時の処理(ペン色のカラーコードを指定)
 #青
def btn1():
    global the_color
    the_color = ('#000099','#003399','#006699','#009999','#00cc99','#00ff99')
    base.quit()

 #紫
def btn2():
    global the_color
    the_color = ('#99ff99','#99cc99','#999999','#996699','#993399','#990099')
    base.quit()

 #ピンク
def btn3():
    global the_color
    the_color = ('#ff0099','#ff3399','#ff6699','#ff9999','#ffcc99','#ffff99')
    base.quit()

 #黄
def btn4():
    global the_color
    the_color = ('#ffff00','#ffcc00','#ff9900','#ff6600','#ff3300','#ff0000')
    base.quit()

 #緑
def btn5():
    global the_color
    the_color = ('#33ff00','#33cc00','#339900','#336600','#333300','#330000')
    base.quit()

#ボタンの作成・位置指定
 #ウィンドウ内のメッセージ
label = tk.Label(base, text='好きな色のボタンを押して')
label.pack()

 #青
btn1 = tk.Button(base, text='青',command=btn1)
btn1.place(x=60,y=100)

 #紫
btn2 = tk.Button(base, text='紫',command=btn2)
btn2.place(x=120,y=100)

 #ピンク
btn3 = tk.Button(base, text='ピンク',command=btn3)
btn3.place(x=180,y=100)

 #黄
btn4 = tk.Button(base, text='黄',command=btn4)
btn4.place(x=240,y=100)

 #緑
btn5 = tk.Button(base, text='緑',command=btn5)
btn5.place(x=300,y=100)

#ウィンドウを保持
base.mainloop()

#Step2：螺旋状の図形を描画
t = Tu.Turtle()
s = Tu.Screen()

s.bgcolor('black') #背景色を黒
t.speed(0) #描画速度を最速

for i in range(90):
    t.pencolor(the_color[i%6]) #ペン色数を6
    t.circle(90-i/2,90) #反時計回りに半径90-i/2、90度の円を描く
    t.lt(90) #左に90度回転
    t.circle(90-i/3,90)
    t.lt(60)

#クリックすると描画スクリーンが閉じる
s.exitonclick()