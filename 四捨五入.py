def ceil_floor(list_num, k, below_dot):
    """非負数numのlist_numに対して, 10のk乗の位で四捨五入を行う"""
    
    index = -(below_dot + 1) - k
    
    if index < -len(list_num):
        return ["0" for i in range(len(list_num))]
    if 0 <= index:
        return list_num

    
    ceil = False  # 切り上げフラグ
    
    if int(list_num[index]) >= 5:  # 5以上で切り上げ
        ceil = True

    # 切り上げ切り捨てに関わらず, 10のk乗の位以下は全て0になる
    for i in range(index, 0):
        list_num[i] = "0"
    
    
    if ceil and index == -len(list_num): # 最高位(一番左の桁)にて, 繰り上がりが起こる
        return ["1"] + ["0" for i in range(len(list_num))]
    elif ceil:
        if int(list_num[index - 1]) <= 8:
            list_num[index - 1] = str(int(list_num[index - 1]) + 1)
            return list_num
        else:  # 繰り上がる先が 9だったら, さらにその次の(左の)桁へ
            return ceil_floor(list_num, k + 1, below_dot)
    else: # 切り捨て
        return list_num
           
    
    
    



def ceil_floor_pre(num, k):
    """numの10のk乗の位で四捨五入を行う前処理と後処理"""
    
    Flag_float = False
    Flag_minus = False
    
    list_num = list(str(num))
    
    if "." in list_num:
        Flag_float = True
    if list_num[0] == "-":
        Flag_minus = True
        del list_num[0]

    
    if not Flag_float:
        below_dot = 0
        list_num = ceil_floor(list_num, k, below_dot)
        result = int("".join(list_num))
    
    else:
        below_dot = len(list_num) - list_num.index(".") - 1  # 小数点以下何桁あるか 
        list_num.remove(".")
        list_num = ceil_floor(list_num, k, below_dot)
        list_num.insert(len(list_num) - below_dot, ".")
        result = float("".join(list_num))
        
        
    

    if Flag_minus:
        return -result
    else:
        return result


# ceil_floor_pre(num, k)
# numはint型かfloat型かstr型
# numの「10のk乗の位で四捨五入」を行った結果を, int型かfloat型で返す。(最初のnumに.が含まれていれば戻り値はfloat)
# 負数はその絶対値で四捨五入してから, マイナスを付与する

# ceil_floor_pre(567, 0) -> 570
# ceil_floor_pre(34.896, -3) -> 34.9
# ceil_floor_pre(-950, 1) -> -1000

# ceil_floor_pre(342, 3) -> 0
# ceil_floor_pre(89.77, -3) -> 89.77


ans = ceil_floor_pre(99.792007, -3)
print(ans)

# ceil_floor()関数のceilフラグをいじれば, 切り上げ・切り下げ関数にもカスタマイズ可能！