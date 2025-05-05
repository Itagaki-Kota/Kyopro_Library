### モジュラ逆数を利用して, 割り算を含む 余りの計算 ###
"""
鉄則本p174
「Mを素数とし, bをMで割り切れない整数であるとする。
このとき, Mで割った余りを求める問題では, 「÷ b」を「× b**(M - 2)」に書き換えても計算結果は変わらない。」
"""

N, K = map(int, input().split())
MOD = 1000000007

# fact[i] := i!をMODで割った余り (N!まで)
fact = [1 for _ in range(N + 1)]
for i in range(1, N + 1):
    fact[i] = fact[i - 1] * i % MOD


def nCk(N, K, MOD): # 鉄則本p173-参考
    # nCkをMODで割った余りを返す
    # MODが素数であることが条件
    
    top = fact[N]
    bottom = fact[K] * fact[N - K] % MOD
    
    return top * pow(bottom, MOD - 2, MOD) % MOD


print(nCk(N, K, MOD))




### Mが素数とは限らない, bとMが互いに素とは限らない、などモジュラ逆数を利用できない条件下 ####
https://atcoder.jp/contests/abc293/editorial/5966 
???????
