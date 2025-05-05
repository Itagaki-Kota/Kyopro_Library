# 二次元累積和     ※PyPyよりもpure python(numpy無)の方が速い? 　※累積和を求める計算量がO(HW)でQ個のクエリに答えてO(HW + Q)。
# 鉄則本p63の図が分かりやすい。


def YokoRuiseki(nums):
    """一次元リストnumsの横方向累積和を計算したリストcum_sumを返す"""

    tmp_sum = 0
    cum_sum = [0]

    for i in nums:
        tmp_sum += i
        cum_sum.append(tmp_sum)

    return cum_sum


def TateRuiseki(field, H, W):    # H, W は横累積処理をする前の完全に元々の状態のH, W 
    """二次元リストfieldの縦方向累積和を計算した二次元リストfieldを返す"""

    field = [[0 for i in range(W + 1)]] + field

    for col in range(W + 1):
        tmp_cum = 0
        for row in range(H + 1):
            tmp_cum += field[row][col]
            field[row][col] = tmp_cum

    return field


def calc_area_sum(leftup, rightdown, R):    # leftup(左上座標), rightdown(右下座標)は,「完全に元々のpure_field」における「インデックス」
    """pure_field(元々の二次元数列)における, 左上座標のマスと右下座標のマスを(含んで)頂点(角)とする長方形内の,　書かれた数の総和を返す"""
    """pure_fieldの縦横累積後がR"""

    a, b = leftup
    c, d  = rightdown

    return R[c + 1][d + 1] - R[a][d + 1] - R[c + 1][b] + R[a][b]

    

    
H = 4
W = 6


field = [
[4,2,3,6,5,8],
[9,1,1,2,4,1],
[5,0,2,1,0,7],
[6,8,3,2,9,1]
]


field_after_yokorui = [YokoRuiseki(row) for row in field]
field_R =  TateRuiseki(field_after_yokorui, H, W)

leftup = (1,2)      #元の長方形の左上座標の(行, 列)の「index」
rightdown = (2, 4)  #元の長方形の右下座標の(行, 列)の「index」

ans = calc_area_sum(leftup, rightdown, field_R)
print(ans) 

#[1, 2, 4]
#[2, 1, 0] の部分。（元々のfieldの）
# 10


"""
# numpy を使えば

field = [
[0,0,0,0,0,0,0],
[0,4,2,3,6,5,8],
[0,9,1,1,2,4,1],
[0,5,0,2,1,0,7],
[0,6,8,3,2,9,1]
]

import numpy as np
field = np.array(field)
field_R = field.cumsum(axis = 1).cumsum(axis = 0)

"""


# 累積和の先頭に0を付ける感じがわかりずらいので, 先頭の0を辞めて, 以下の様にするのも吉？
# https://atcoder.jp/contests/joi2011ho/submissions/45076957
