# 自然数Nの約数列挙は, 約数の候補を√N くらいまで調べればよい


# 約数列挙
def div_enu(N):
    """自然数Nの約数を列挙した集合を返す"""

    div_set = set()
    for div in range(1, int(N ** (0.5) + 1)):
        if N % div == 0:
            div_set.add(div)
            div_set.add(N // div)

    return div_set



# 最大公約数 (Greatest Common Divisor)  (公約数列挙にも)
def my_gcd(A, B):
    """自然数Aと自然数Bの最大公約数を返す (試し割り法 O(√N))"""
    """ 公約数の列挙や, 互いに素(公約数が1のみ)の確認にも有効"""
    
    N = min(A, B)
    M = max(A, B)
    
    cd_set = set()  # common divisor
    for div in range(1, int(N ** (0.5) + 1)):
        if N % div == 0:
            
            if M % div == 0:
                cd_set.add(div)
            
            if M % (N // div) == 0:
                cd_set.add(N // div)
    
    return max(cd_set)


import math
print(math.gcd(A, B))




# ユークリッドの互除法 (最大公約数)(鉄則本p162)  O(log(A + B))

def Euclid_GCD(A, B):
    """自然数AとBの最大公約数を返す"""
    """大きい方を, 小さい方で割った余りに置換することを繰り返し, 片方が0になったら終了"""
    
    while True:
        if A >= B:
            A %= B
        else:
            B %= A
        
        if A == 0 or B == 0:
            break
    
    return max(A, B)  # 0ではない方がGCD


    




# 素数判定 (試し割り法で, √Nまでの数で割っていき, 1以外の約数が無ければ素数)
def is_prime(n):
    """自然数nが素数ならTrue"""

    if n == 1:
        return False
    
    for div in range(2, int(n ** (0.5)) + 1):
        if n % div == 0:
            return False
    else:
        return True



# 素数列挙【エラトステネスの篩】 (https://atcoder.jp/contests/tessoku-book/submissions/37616440)

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




# 素因数分解
def  factorization(N):
    """ 自然数N(>=2)を素因数分解した結果の, 素因子が入ったリストを返す O(√N)"""
    
    factor = []
    for div in range(2, int(N ** (0.5)) + 1):
        while N % div == 0:
            N //= div
            factor.append(div)
            
    if N != 1:      
        factor.append(N)

    # factor.sort()
    
    return factor
 
 
#print(factorization(12))
# [2, 2, 3]





### 素因数分解(ポラードのロー法) ###  (https://qiita.com/t_fuki/items/7cd50de54d3c5d063b4a#%E3%83%9D%E3%83%A9%E3%83%BC%E3%83%89%E3%83%AD%E3%83%BC%E7%B4%A0%E5%9B%A0%E6%95%B0%E5%88%86%E8%A7%A3%E6%B3%95%E3%81%AE%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0)
「とんでもなく大きい数」を高速に素因数分解する！
しかし, 10**7くらいまでの数の素因数分解はむしろO(√N)のやり方の方が速い...

def gcd(a, b):
    while a:
        a, b = b%a, a
    return b


def is_prime(n):
    if n == 2:
        return 1
    if n == 1 or n%2 == 0:
        return 0

    m = n - 1
    lsb = m & -m
    s = lsb.bit_length()-1
    d = m // lsb

    test_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]

    for a in test_numbers:
        if a == n:
            continue
        x = pow(a,d,n)
        r = 0
        if x == 1:
            continue
        while x != m:
            x = pow(x,2,n)
            r += 1
            if x == 1 or r == s:
                return 0
    return 1


def find_prime_factor(n):
    if n%2 == 0:
        return 2

    m = int(n**0.125)+1

    for c in range(1,n):
        f = lambda a: (pow(a,2,n)+c)%n
        y = 0
        g = q = r = 1
        k = 0
        while g == 1:
            x = y
            while k < 3*r//4:
                y = f(y)
                k += 1
            while k < r and g == 1:
                ys = y
                for _ in range(min(m, r-k)):
                    y = f(y)
                    q = q*abs(x-y)%n
                g = gcd(q,n)
                k += m
            k = r
            r *= 2
        if g == n:
            g = 1
            y = ys
            while g == 1:
                y = f(y)
                g = gcd(abs(x-y),n)
        if g == n:
            continue
        if is_prime(g):
            return g
        elif is_prime(n//g):
            return n//g
        else:
            return find_prime_factor(g)


def factorize(n):
    res = {}
    while not is_prime(n) and n > 1:  # nが合成数である間nの素因数の探索を繰り返す
        p = find_prime_factor(n)
        s = 0
        while n%p == 0:  # nが素因数pで割れる間割り続け、出力に追加
            n //= p
            s += 1
        res[p] = s
    if n > 1:  # n>1であればnは素数なので出力に追加
        res[n] = 1
    return res


ans = factorize(100)
print(ans)
# {2: 2, 5: 2}  キーの値(素因子)は昇順