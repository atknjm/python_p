import turtle as Tu

t = Tu.Turtle()
s = Tu.Screen()

s.bgcolor('black') #背景色を黒にする
t.speed(0) #描画速度を最速にする

#ペン色のカラーコードを指定する条件分岐
def what_is_color(button):
    if button == '青':
        return '#000099','#003399','#006699','#009999','#00cc99','#00ff99'
    elif button == '紫':
        return '#99ff99','#99cc99','#999999','#996699','#993399','#990099'
    elif button == 'ピンク':
        return '#ff0099','#ff3399','#ff6699','#ff9999','#ffcc99','#ffff99'
    elif button == '黄':
        return '#ffff00','#ffcc00','#ff9900','#ff6600','#ff3300','#ff0000'
    else:
        return '#33ff00','#33cc00','#339900','#336600','#333300','#330000'

#★★好きなペンの色を''の中に記載★★
result = what_is_color('緑')
color = (result)

for i in range(120):
    t.pencolor(color[i%6]) #ペン色数を6にする
    t.circle(190-i/2,90) #反時計回りに半径190-i/2、90度の円を描く
    t.lt(90) #左に90度回転する
    t.circle(190-i/3,90)
    t.lt(60)

s.exitonclick() #クリックすると描画スクリーンが閉じる