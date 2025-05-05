# AGC046 A問題 Takahashikun, The Strider の実験
# Xの値をループさせ続けると誤差が蓄積するので注意

from turtle import *


X = 64 # 半時計まわりに何度回転させたいか

ans = 0  # 前に進んだ回数

while True:
    forward(100)  # 100cm進む
    ans += 1

    left(X)  # 半時計まわりにX度回転

    x, y = pos()  # 現在の座標を取得
    x = int(x)
    y = int(y)

    if x == 0 and y == 0:  # スタート位置まで戻ってきたら
        print(f"{X=}{ans=}")
        break

mainloop()  # 描画されたものが残ってくれる。これを書かないと描画したウィンドウが勝手に消える