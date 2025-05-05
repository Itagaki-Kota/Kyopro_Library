# これとは別に上下「反転」, 左右反転, 転置, の ぞれぞれのindexの対応は次の問題に詳しい (https://mojacoder.app/users/kusirakusira/problems/25GBC_D)


def Turn_90(A):
    """二次元配列A(H行W列)を時計回りに90度回転させる"""

    H = len(A)
    W = len(A[0])
    
    after_H = W  # 回転後の配列の高さ
    after_W = H  # 回転後の配列の横幅

    A_after_turn = [["" for col in range(after_W)] for row in range(after_H)]
    
    for row in range(H):
        for col in range(W):
            A_after_turn[col][H - row - 1] = A[row][col]
 
    return A_after_turn



def Turn_180(A):
    """二次元配列A(H行W列)を180度回転させる(点対称移動)(上下回転(逆さま))"""

    H = len(A)
    W = len(A[0])
    
    A_after_turn = [["" for col in range(W)] for row in range(H)]
    
    for row in range(H):
        for col in range(W):
            A_after_turn[H - 1 - row][W - 1 - col] = A[row][col]
 
    return A_after_turn



def Turn_270(A):
    """二次元配列A(H行W列)を時計回りに270度(反時計回りに90度)回転させる"""

    H = len(A)
    W = len(A[0])

    after_H = W  #回転後の配列の高さ
    after_W = H  #回転後の配列の横幅
    
    A_after_turn = [["" for col in range(after_W)] for row in range(after_H)]
    
    for row in range(H):
        for col in range(W):
            A_after_turn[W - 1 - col][row] = A[row][col]
 
    return A_after_turn
    


A = [[0,0,0,1,1],
     [1,1,0,0,0],
     [3,5,1,1,0]]
    
B = Turn_270(A)
print(B)

print()

for row in B:
    print(row)




### 以下, 周辺の削除など, ABC322 D Polyomino(https://atcoder.jp/contests/abc322/submissions/46246681) ###########

def cut_around(A):
    # 二次元配列Aの周辺を切り落とす (# が少なくとも1個はある前提)
    
    H = len(A)
    W = len(A[0])
    
    min_row = H
    max_row = -1
    min_col = W
    max_col = -1
    
    for row in range(H):
        for col in range(W):
            
            if A[row][col] == "#":
                min_row = min(min_row, row)
                min_col = min(min_col, col)
                max_row = max(max_row, row)
                max_col = max(max_col, col)
    
    cut_A = []
    
    for row in range(min_row, max_row + 1):
        now_row = []
        for col in range(min_col, max_col + 1):
            
            now_row.append(A[row][col])
        
        cut_A.append(now_row)
    
    
    return cut_A


def Turn_90(A):
    """二次元配列A(H行W列)を時計回りに90度回転させる"""

    H = len(A)
    W = len(A[0])
    
    after_H = W  # 回転後の配列の高さ
    after_W = H  # 回転後の配列の横幅

    A_after_turn = [["" for col in range(after_W)] for row in range(after_H)]
    
    for row in range(H):
        for col in range(W):
            A_after_turn[col][H - row - 1] = A[row][col]
 
    return A_after_turn



def Turn_180(A):
    """二次元配列A(H行W列)を180度回転させる(点対称移動)(上下回転(逆さま))"""

    H = len(A)
    W = len(A[0])
    
    A_after_turn = [["" for col in range(W)] for row in range(H)]
    
    for row in range(H):
        for col in range(W):
            A_after_turn[H - 1 - row][W - 1 - col] = A[row][col]
 
    return A_after_turn



def Turn_270(A):
    """二次元配列A(H行W列)を時計回りに270度(反時計回りに90度)回転させる"""

    H = len(A)
    W = len(A[0])

    after_H = W  #回転後の配列の高さ
    after_W = H  #回転後の配列の横幅
    
    A_after_turn = [["" for col in range(after_W)] for row in range(after_H)]
    
    for row in range(H):
        for col in range(W):
            A_after_turn[W - 1 - col][row] = A[row][col]
 
    return A_after_turn


def inter_board(place_row, place_col, piece_H, piece_W):
    # 盤面上のplace_row, place_colの座標に タテpiece_H, ヨコpiece_W のサイズのピースを置いてはみ出なければTrue
    if 0 <= place_row + (piece_H - 1) <= board_H - 1:
        if 0 <= place_col + (piece_W - 1) <= board_W - 1:
            return True
    return False

def achieve_puzzle(A, B, C):
    # ポリオミノA, B, C が board_H × board_W の盤面にキレイにはまるかチェックする
    N = board_H * board_W
    
    A_H, A_W = len(A), len(A[0])
    B_H, B_W = len(B), len(B[0])
    C_H, C_W = len(C), len(C[0])
    
    # A, B, C の左上の座標 (A, B, C の配置)を全探索
    for A_vid in range(N):
        for B_vid in range(N):
            for C_vid in range(N):
                
                A_row, A_col = A_vid // board_W, A_vid % board_W  # Aの左上を配置する座標
                B_row, B_col = B_vid // board_W, B_vid % board_W
                C_row, C_col = C_vid // board_W, C_vid % board_W
    
                # はみ出ないかの確認
                if not inter_board(A_row, A_col, A_H, A_W):
                    continue
                if not inter_board(B_row, B_col, B_H, B_W):
                    continue
                if not inter_board(C_row, C_col, C_H, C_W):
                    continue
    
                
                board = [[0 for col in range(board_W)] for row in range(board_H)]  # 1:そのマスが既に埋まっている

                cnt = 0  # 盤面の内, なんマス埋まったか？

                Flg = True # マスの被りが無ければTrue

                # Aを配置 
                if Flg:
                    for row in range(A_H):
                        if Flg:
                            for col in range(A_W):
                                
                                if A[row][col] == "#":
                                    
                                    # 既にそのマスが埋まっていたら
                                    if board[A_row + row][A_col + col] == 1:
                                        Flg = False
                                        break
                                    
                                    board[A_row + row][A_col + col] = 1
                                    cnt += 1
                        else:
                            break

                # Bを配置 
                if Flg:
                    for row in range(B_H):
                        if Flg:
                            for col in range(B_W):
                                
                                if B[row][col] == "#":
                                    
                                    # 既にそのマスが埋まっていたら
                                    if board[B_row + row][B_col + col] == 1:
                                        Flg = False
                                        break
                                    
                                    board[B_row + row][B_col + col] = 1
                                    cnt += 1
                        else:
                            break


                # Cを配置 
                if Flg:
                    for row in range(C_H):
                        if Flg:
                            for col in range(C_W):
                                
                                if C[row][col] == "#":
                                    
                                    # 既にそのマスが埋まっていたら
                                    if board[C_row + row][C_col + col] == 1:
                                        Flg = False
                                        break
                                    
                                    board[C_row + row][C_col + col] = 1
                                    cnt += 1
                        else:
                            break
                                
                
                if Flg and cnt == N:
                    return True
    
    
    
    



# 盤面のサイズ
board_H = 4
board_W = 4

# 各ポリオミノの入力
A = []
B = []
C = []

for _ in range(board_H):
    A.append(list(input()))
for _ in range(board_H):
    B.append(list(input()))
for _ in range(board_H):
    C.append(list(input()))
    
# 周辺のカット
A = cut_around(A)
B = cut_around(B)
C = cut_around(C)

# 回転
A_turn_list = [A, Turn_90(A), Turn_180(A), Turn_270(A)]
B_turn_list = [B, Turn_90(B), Turn_180(B), Turn_270(B)]
C_turn_list = [C, Turn_90(C), Turn_180(C), Turn_270(C)]


# パズル達成の確認
for i in range(4):
    for j in range(4):
        for k in range(4):
            
            if achieve_puzzle(A_turn_list[i], B_turn_list[j], C_turn_list[k]):
                print("Yes")
                exit()


print("No")


    