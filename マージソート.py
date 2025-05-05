from random import randint
from typing import List
import time
import numpy as np
import matplotlib.pyplot as plt

def merge_sort(A : List[int]) -> List[int]:
    N = len(A)

    if N == 1:
        return A
    
    center_index = N // 2

    # 左右に分割
    L_list = []
    R_list = []

    for i in range(center_index):
        L_list.append(A[i])
    for i in range(center_index, N):
        R_list.append(A[i])
    
    L_list_sorted = merge_sort(L_list)
    R_list_sorted = merge_sort(R_list)

    # マージ
    A_sorted = []

    i_L = 0
    i_R = 0
    while i_L < len(L_list_sorted) or i_R < len(R_list_sorted):
    
        if i_L < len(L_list_sorted) and i_R < len(R_list_sorted):
            if L_list_sorted[i_L] <= R_list_sorted[i_R]:
                A_sorted.append(L_list_sorted[i_L])
                i_L += 1
            else:
                A_sorted.append(R_list_sorted[i_R])
                i_R += 1

        elif i_L < len(L_list_sorted):
            A_sorted.append(L_list_sorted[i_L])
            i_L += 1

        else:
            A_sorted.append(R_list_sorted[i_R])
            i_R += 1           

    return A_sorted


def bubble_sort(A : List[int]) -> List[int]:
    N = len(A)

    A_sorted = []
    for i in range(N):
        A_sorted.append(A[i])

    for _ in range(N):
        for i in range(N - 1):
            if A_sorted[i] > A_sorted[i + 1]:
                A_sorted[i], A_sorted[i + 1] = A_sorted[i + 1], A_sorted[i]

    return A_sorted


def depict_bar(A:List[int], A_name:str, B:List[int], B_name:str) -> None:

    # 平均値と標準偏差の計算
    mean_a = np.mean(A)
    std_a = np.std(A)

    mean_b = np.mean(B)
    std_b = np.std(B)

    # 棒グラフの描画
    labels = [A_name, B_name]
    means = [mean_a, mean_b]
    stds = [std_a, std_b]

    # 棒グラフを作成
    x = np.arange(len(labels))  # ラベルの位置
    width = 0.35  # 棒の幅

    fig, ax = plt.subplots()
    bars = ax.bar(x, means, width, yerr=stds, capsize=5, color=['blue', 'orange'])

    # グラフの装飾
    ax.set_ylabel('Time')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.axhline(0, color='grey', linewidth=0.8)

    plt.show()


if __name__ == '__main__':
    N = 1000
    max_value = 100
    min_value =  -100

    N_sim = 100

    times_merge_sort = []
    times_bubble_sort = []

    for _ in range(N_sim):
        A = [randint(min_value, max_value) for _ in range(N)]

        merge_start = time.time()
        A_merge_sorted = merge_sort(A)
        merge_end = time.time()
        times_merge_sort.append(merge_end - merge_start)

        bubble_start = time.time()
        A_bubble_sorted = bubble_sort(A)
        bubble_end = time.time()
        times_bubble_sort.append(bubble_end - bubble_start)

        # if sorted(A) != A_merge_sorted:
        #     print("Failed merge sort...!")
        #     exit()
        # if sorted(A) != A_bubble_sorted:
        #     print("Failed bubble sort...!")
        #     exit()

        #print(A)
        #print(A_merge_sorted)
        #print(A_bubble_sorted)
    
    
    depict_bar(times_merge_sort, "Merge", times_bubble_sort, "Bubble")


