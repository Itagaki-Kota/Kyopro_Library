alphabet_id_upper = dict(zip(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"), [i for i in range(26)]))
id_alphabet_upper = dict(zip([i for i in range(26)], list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")))

alphabet_id_lower = dict(zip(list("abcdefghijklmnopqrstuvwxyz"), [i for i in range(26)]))
id_alphabet_lower = dict(zip([i for i in range(26)], list("abcdefghijklmnopqrstuvwxyz")))


Cipher = input()  # 暗号文


for dif in range(26):  # 各文字をdif文字分だけずらす  (例: difが3なら, D -> G)

    for s in Cipher:
        if s not in alphabet_id_upper and s not in alphabet_id_lower:  # コンマやピリオドやスペースなど, アルファベット以外はそのまま表示
            print(s, end = "")
        
        else:
            if s.isupper():  # 大文字
                num = alphabet_id_upper[s]
                num += dif
                num %= 26
                print(id_alphabet_upper[num], end = "")
            
            else:  # 小文字
                num = alphabet_id_lower[s]
                num += dif
                num %= 26
                print(id_alphabet_lower[num], end = "")
    
    print()
    print()
                   