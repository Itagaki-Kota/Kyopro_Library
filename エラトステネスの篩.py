# エラトステネスの篩による, N以下の素数列挙 (https://atcoder.jp/contests/tessoku-book/submissions/37616440)

def Sieve_of_Eratosthenes(N):
    """ N以下(N <= 2)の素数を列挙したリストを返す(鉄則本p158)"""
    
    # 2以上N以下の整数を全て書いてみる (先頭の0と1はダミー的存在)
    field = [True for i in range(N + 1)]
    
    # baseにマルを付け, 「それ以外の」baseの倍数を消す (base自身は消さないように注意)
    for base in range(2, int(N ** 0.5) + 1): # baseは√Nまででよい
        if not field[base]: # baseが既に消されていたらcontinue
            continue
        for del_num in range(base * 2, N + 1, base):  # baseの倍数を消す (base自身は消さないように注意)
            field[del_num] = False
    
    # Trueなら対応する数字を入れる
    prime_nums = [i for i in range(2, N + 1) if field[i]]
        
    return prime_nums


N = int(input())
prime_nums = Sieve_of_Eratosthenes(N)

for ans in prime_nums:
    print(ans)
            
    
    


"""
import math

def eratosthenes(N):
    prime = [True for i in range(N + 1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(N))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2 * i, N + 1, i):
                prime[j] = False

    return prime



N = 30 

# N以下の素数列挙 (リスト)
prime = eratosthenes(N)
prime_numlist = [p for p in range(2, N + 1) if prime[p]]

print(prime_numlist)
"""