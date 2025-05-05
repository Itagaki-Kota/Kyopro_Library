# ランレングス圧縮(連長圧縮)  何の文字が何回連続しているか

#ABC259 C  XXtoXXX    https://atcoder.jp/contests/abc259/submissions/33113614


def RunLength(S):
    """文字列S(またはリストS)についてランレングス圧縮"""

    RL = []
    count = 1
    for i in range(1, len(S)):
    
        if S[i] == S[i - 1]:
            count += 1
        else:
            RL.append((S[i - 1], count))
            count = 1
 
    RL.append((S[-1], count))  
    return RL

# RunLength("AAAADDDDDEEFGGGGH")
# [('A', 4), ('D', 5), ('E', 2), ('F', 1), ('G', 4), ('H', 1)]


# RunLength(["3", "5", "5", "5", "19", "19"])
# [('3', 1), ('5', 3), ('19', 2)]