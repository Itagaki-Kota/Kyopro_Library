def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        gcd, x, y = extended_gcd(b % a, a)
        return gcd, y - (b // a) * x, x

def find_solution(a, b, c):
    gcd, x, y = extended_gcd(a, b)
    if c % gcd != 0:
        return None
    else:
        return x * (c // gcd), y * (c // gcd)



# ax + by = c の二元一次不定方程式の整数解(x, y)が存在するなら一組見つけたい。

# 5x -2y = 3 ならば...

a = 5   # ここにaの値を入力してください
b = -2  # ここにbの値を入力してください
c = 3   # ここにcの値を入力してください


solution = find_solution(a, b, c)

if solution is None:  # 整数解なし
    print(-1)
else:
    print(*solution)  # 整数解(x, y)  -> (3, 6)など。


    # 一般解も知りたい？
    x0, y0 = solution
    
    from math import gcd
    print(f"x = {x0} + k × {b // gcd(a, b)}")
    print(f"y = {y0} - k × {a // gcd(a, b)}")
