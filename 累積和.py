# 累積和を用いて, 区間の和をO(1)で計算する。区間和のクエリQ個に対し,愚直だとO(NQ)なのに, 累積和用いるとO(N + Q)。

def Ruiseki(nums):
    """リストnumsの累積和を計算したリストcum_sumを返す"""

    tmp_sum = 0
    cum_sum = [0]

    for i in nums:
        tmp_sum += i
        cum_sum.append(tmp_sum)

    return cum_sum

nums = [2,3,41,6,0,-2,7,0]
cum_sum = Ruiseki(nums)
# [0, 2, 5, 46, 52, 52, 50, 57, 57]

# numsの3番目から7番目までの区間[41, 6, 0, -2, 7]の和は
# cum_sum[7] - cum_sum[2]




def max_in_width(width, cum_sum, N):
    """長さがwidthの区間における最大値を返す"""

    tmp_max = 0 
    for i in range(width, N + 1):
        tmp = cum_sum[i] - cum_sum[i - width]
        tmp_max = max(tmp, tmp_max)
    
    return tmp_max


N = len(nums)

for width in range(1, N + 1):
    print( max_in_width(width, cum_sum, N) )

"""
nums = [2,3,41,6,0,-2,7,0]

41 長さが1の区間の最大値
47 長さが2の区間の最大値
50
52
52
55
57
57 長さが8の区間の最大値
"""