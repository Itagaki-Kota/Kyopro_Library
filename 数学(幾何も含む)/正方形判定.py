from itertools import combinations

def is_square_shape(v1, v2, v3, v4):
    """4点 v1, v2, v3, v4 の座標から, その４点から成る図形が正方形であるか否か判定"""
    """4C2通りの辺の長さを算出し, 正方形ならば, 各二乗値の比が, 1:1:1:1:2:2"""

    dis = []   # 辺の長さの二乗値が入るリスト

    for a, b in combinations((v1, v2, v3, v4), 2):   # 4点から2点を選ぶ
        xa, ya = a
        xb, yb = b
        dis.append((xa - xb) ** 2 + (ya - yb) ** 2)

    dis.sort()
    
    if dis[0] == dis[-1] == 0:  # すべての距離がゼロ(四点が全て重なっている)
        return False

    elif dis[0] == dis[1] == dis[2] == dis[3] and dis[4] == dis[5] and dis[0] * 2 == dis[5]:
        return True
    else:
        return False


print(is_square_shape((2, 0), (2, 2), (0, 2), (0, 0)))  # True
