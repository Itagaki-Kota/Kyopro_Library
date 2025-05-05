def bit_allsearch(N):
    """ 自己流bit全探索用。 文字列が入ったリストを返す"""

    bin_list = []
    for i in range(2 ** N):
        tmp = bin(i)[2:]                              # bin()で2進数(文字列)に変換後, 0b以降だけ取る。
        bin_list.append("0" * (N - len(tmp)) + tmp)   # 先頭に0を追加して, 桁数をNに合わせる
    return bin_list

# bit_allsearch(3)
# ['000', '001', '010', '011', '100', '101', '110', '111']  2 ** 3 = 8通り