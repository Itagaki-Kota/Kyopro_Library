# ☆LIS, LDS (Longest Increasing Subsequence)(Longest Decreasing Subsequence)(最長増加部分列)(最長減少部分列)
# 一次元dpだが,計算量はO(N)より大きく,O(N^2)よりは小さいはず。結構時間食うので,PyPyで。(-> O(N^2)だそう。)

◎ 鉄則本p146-147と添字が合うように、1-index化した -> (https://atcoder.jp/contests/tessoku-book/submissions/62836116)


def LIS(nums, N):
    """リストnumsから,最長増加部分列の長さを返す (広義単調増加)
       Nはlen(nums)
       dp[i]はnumsのi番目の数が最後になるときの最長増加部分列の長さ
       自分以前の要素の中から, 自分の高さ以下の要素の内, dp[i]が最大のもの+1""" 
    

    dp = [0 for i in range(N + 1)]                     # 先頭はダミー
    dp[1] = 1                                          # numsの先頭要素を末尾としたLISの長さは1
    for now in range(2, N + 1):
        dp[now] = 1                                    # 少なくとも, 長さ1のLISは出来る
        for before in range(1, now):                   # 自分以前の要素を走査
            if nums[before - 1] <= nums[now - 1]:      # numsに対応するとインデックスが一個ずれる
                dp[now] = max(dp[now], dp[before] + 1)
    
    return max(dp)


#nums = [100, 1000, 102, 101, 91, 199, 199]
#print(LIS(nums, 7))
# → 4
# dp = [0, 1, 2, 2, 2, 1, 3, 4]




def LDS(nums, N):
    """リストnumsから,最長減少部分列の長さを返す (広義単調減少)
       Nはlen(nums)
       dp[i]はnumsのi番目の数が最後になるときの最長減少部分列の長さ
       自分以前の要素の中から, 自分の高さ以上の要素の内, dp[i]が最大のもの+1""" 
    

    dp = [0 for i in range(N + 1)]
    dp[1] = 1
    for now in range(2, N + 1):
        dp[now] = 1
        for before in range(1, now):
            if nums[before - 1] >= nums[now - 1]:      # numsはインデックスが一個ずれる
                dp[now] = max(dp[now], dp[before] + 1)
    
    return max(dp)


#nums = [100, 1000, 102, 101, 91, 199, 199]
#print(LDS(nums, 7))
# → 4
# dp = [0, 1, 1, 2, 3, 4, 2, 3]











◎ 広義or狭義 に注意      # bisect_rightなら広義, bisect_leftなら狭義
◎ Lの初期値に注意

from bisect import bisect_right, bisect_left

def LIS_new(nums, N):
    """鉄則本p146-147を模倣。 計算量O(NlogN)
       「自分以前の要素の中から, 自分の高さ以下(←広義なら)の要素の内, dp[i]が最大のもの」を
        配列Lを利用して二分探索でO(logN)で求める""" 

    L = [0]                             # 先頭はダミー(制約を見て, 配列Lの中で必ず最小値になるダミーを入れる)

    dp = [None for i in range(N)]        
    dp[0] = 1                           # numsの先頭要素を末尾としたLISの長さは1
    L.append(nums[0])

    for i in range(1, N):

        dp[i] = bisect_left(L, nums[i])

        if len(L) == dp[i]:
            L.append(nums[i])
        else:
            L[dp[i]] = nums[i]

    return max(dp)







from bisect import bisect_right, bisect_left

def LDS_new(nums, N):
    """計算量O(NlogN)
       numsリスト内の要素をすべて符号反転して, LISを行う""" 
        
    nums = [-n for n in nums]

    L = [-10**10]                       # 先頭はダミー(制約を見て, 配列Lの中で必ず最小値になるダミーを入れる)

    dp = [None for i in range(N)]        
    dp[0] = 1                           # numsの先頭要素を末尾としたLISの長さは1
    L.append(nums[0])

    for i in range(1, N):

        dp[i] = bisect_left(L, nums[i])

        if len(L) == dp[i]:
            L.append(nums[i])
        else:
            L[dp[i]] = nums[i]

    return max(dp)










    