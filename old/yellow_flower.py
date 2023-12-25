import turtle

wn = turtle.Screen()
tur = turtle.Turtle()

wn.bgcolor('white') #背景色を黒色にする
tur.pencolor('yellow') #ペン色を黄色にする
tur.speed(0) #描画速度を最速にする

for i in range(190):
    tur.circle(190-i,90) #回転半径190-iで90度の円弧を描く
    tur.left(90) #90度左に向きを変える
    tur.circle(190-i,90) #回転半径190-iで90度の円弧を描く
    tur.left(18) #18度左に向きを変える

wn.exitonclick()