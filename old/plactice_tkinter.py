import tkinter as tk

base = tk.Tk()
base.geometry('400x200') #ウィンドウのサイズ（幅×高さ）
base.title('色選択') #ウィンドウのタイトル

label = tk.Label(base, text='好きな色のボタンを押して').pack()
button1 = tk.Button(base, text='青').place(x=60,y=100) #左から1番目のボタン名と位置
button2 = tk.Button(base, text='紫').place(x=120,y=100) #左から2番目のボタン名と位置
button3 = tk.Button(base, text='ピンク').place(x=180,y=100) #左から3番目のボタン名と位置
button4 = tk.Button(base, text='黄').place(x=240,y=100) #左から4番目のボタン名と位置
button5 = tk.Button(base, text='緑').place(x=300,y=100) #左から5番目のボタン名と位置

base.quit()