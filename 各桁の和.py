"""
n桁の整数の, 『各桁の和』を計算する関数。　例) 4537 → 4 + 5 + 3 + 7 = 19
どちらの実装でも, そんなに速度は変わらない。
"""




def sum_each_digits(num):
    sum_digits = 0
    num = str(num)
    for i in num:
        sum_digits += int(i)
    return sum_digits



def sum_each_digits2(num):
    """ N進法展開の考え方"""

    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num = num // 10
    return sum_digits



def sum_each_digits3(num):
    """ mapのテクニカルな使い方(最もはやい？)"""

    return sum(map(int, str(num)))






import timeit
n = 1463496794354456895769807378258327573875984316486
loop = 100

result = timeit.timeit("sum_each_digits(n)", globals = globals(), number = loop)
print(result / loop)

result = timeit.timeit("sum_each_digits2(n)", globals = globals(), number = loop)
print(result / loop)

result = timeit.timeit("sum_each_digits3(n)", globals = globals(), number = loop)
print(result / loop)









