

### 独自の比較関数(比較基準)を, sort()関数に組み込みたい場合
ABC308 C Standings (https://atcoder.jp/contests/abc308/submissions/43178170)
###




# バブルソート (基本交換法)  O(N**2) 内部ソート 安定ソート

def bubble_sort(A, reverse = False):
    
    N = len(A)
    
    if not reverse:
        for i in range(N - 1, 0, -1):
            for j in range(i):
                if A[j] > A[j + 1]:
                    A[j + 1], A[j] = A[j], A[j + 1]
    
    else:
        for i in range(N - 1, 0, -1):
            for j in range(i):
                if A[j] < A[j + 1]:
                    A[j + 1], A[j] = A[j], A[j + 1]










# 選択ソート (基本選択法)  O(N**2) 内部ソート 安定ソート

def selection_sort(A, reverse = False):
    
    N = len(A)

    if not reverse:  # 昇順 未確定配列中の最大値を, 未確定配列の末尾と交換する
        for replace_end_id in range(N - 1, 0, -1):
            tmp_max = None
            for i in range(replace_end_id + 1):
                if tmp_max == None:
                    tmp_max = A[i]
                    tmp_id = i
                else:
                    if A[i] >= tmp_max:
                        tmp_max = A[i]
                        tmp_id = i

            A[replace_end_id], A[tmp_id] = tmp_max, A[replace_end_id] 
    
    
    else:   # 降順 未確定配列中の最小値を, 未確定配列の末尾と交換する
        for replace_end_id in range(N - 1, 0, -1):
            tmp_min = None
            for i in range(replace_end_id + 1):
                if tmp_min == None:
                    tmp_min = A[i]
                    tmp_id = i
                else:
                    if A[i] <= tmp_min:
                        tmp_min = A[i]
                        tmp_id = i

            A[replace_end_id], A[tmp_id] = tmp_min, A[replace_end_id]  




# クイックソート O(NlogN) (https://qiita.com/suecharo/items/30f5d817da4c948c3be6)
これを自分で書く必要があった問題
東大UTPC2022 -D Balance(https://atcoder.jp/contests/utpc2022/submissions/40077117)

def quick_sort(arr):
    
    left = []
    right = []
    if len(arr) <= 1:
        return arr

    # データの状態に左右されないためにrandom.choice()を用いることもある。
    # ref = random.choice(arr)
    ref = arr[0]  # ピボット(基準値)
    ref_count = 0

    for ele in arr:
        if ele < ref:
            left.append(ele)
        elif ele > ref:
            right.append(ele)
        else:
            ref_count += 1
    left = quick_sort(left)
    right = quick_sort(right)
    return left + [ref] * ref_count + right



A = [3, 5, 6, 1, 2, 3, 7, 5, 4, 3]
print(A)
sorted_A = quick_sort(A)
print(sorted_A)




# アルゴ式のクイックソート
N = int(input())
A = list(map(int, input().split()))

def quick_sort(A):
    N = len(A)
    X = N // 2

    pivot = A[X]

    L = []
    R = []

    for i in range(N):
        if i == X:
            continue
        
        if A[i] < pivot:
            L.append(A[i])
        else:
            R.append(A[i])
    
    if len(L) != 0:
        L = quick_sort(L)
    if len(R) != 0:
        R = quick_sort(R)
    
    return L + [pivot] + R

A = quick_sort(A)
print(*A)




# アルゴ式の乱択クイックソート
from random import randint

N = int(input())
A = list(map(int, input().split()))

def quick_sort(A):
    N = len(A)
    X = randint(0, N - 1)

    pivot = A[X]

    L = []
    R = []

    for i in range(N):
        if i == X:
            continue
        
        if A[i] < pivot:
            L.append(A[i])
        elif A[i] > pivot:
            R.append(A[i])
        else:
            if randint(1, 100) <= 50:
                L.append(A[i])
            else:
                R.append(A[i])
    
    if len(L) != 0:
        L = quick_sort(L)
    if len(R) != 0:
        R = quick_sort(R)
    
    return L + [pivot] + R

A = quick_sort(A)
print(*A)