"""
# 行列累乗ライブラリ

import numpy as np

def mat_pow_mod(mat, n, mod):
    # bingAIにより生成
    size = len(mat)
    res = np.eye(size, dtype=int)
    while n > 0:
        if n & 1:
            res = np.dot(res, mat) % mod
        mat = np.dot(mat, mat) % mod
        n >>= 1
    return res

# 行列Aと累乗する数nを定義
A = [[1, 1, 0], 
     [0, 0, 1],
     [1, 1, 0]]
n = 10**18

MOD = 998244353
# 行列の累乗を計算し、各要素をMODで割った余りを取得します
result = mat_pow_mod(A, n, MOD)


for row in result:
    print(row)
"""



# 自作問題 Twin one を行列累乗 で非常に巨大な 入力 N <= 10^18で解くと,

