【ABC282 D Make Bipartite2】(https://atcoder.jp/contests/abc282/submissions/38634327)

(この問題の定義だと, 全体として一つの連結になっていなくとも, 隣り合う頂点同士が同色でないならば「二部グラフ」と呼べる)




【二部グラフ判定】
def is_bipartite(N, M, G):
    """単純無向グラフG(連結とは限らない)が二部グラフであるか判定し, 
    二部グラフならば各連結成分ごとのグループ分けと色の個数 を返す"""

    from collections import deque
    
    #N,M = map(int,input().split())  # N頂点M辺 (頂点番号は1～)
    #G = [[] for _ in range(N + 1)]  # 先頭はダミー
    
    # 各頂点の色
    color = [0 for i in range(N + 1)]  # 0は未訪問(白)  # 先頭はダミー
    
    #for _ in range(M):
        #A,B = map(int,input().split())
        #G[A].append(B)
        #G[B].append(A)
    
    
    
    
    # 各連結成分(各グループ)における頂点の色の個数
    color_by_group = []
    
    
    # start_idを始点としてBFSを行い, 頂点に色を塗っていく。
    # start_idの番号でグループ分けする。
    #color[i] = (1, start_id) ならば, 頂点iは赤でstart_idを祖先とするグループ。 青ならば(-1, start_id)。
    
    for start_id in range(1, N + 1):
        if color[start_id] != 0:  # 既に訪問済みならばスキップ
            continue
        
        color[start_id] = (1, start_id)  # 始点は赤で塗っておく。
        
        # この連結成分(このグループ)における頂点の色の個数
        R = 1
        B = 0
        
        q = deque()
        q.append(start_id)  # 始点をキューに追加
    
        while q:
            now_id = q.popleft()
            for ne_id in G[now_id]:
                
                if color[ne_id] == 0: #塗られていない(未訪問、白色)なら, now_idとは別の色で塗る
                    color[ne_id] = (-color[now_id][0], start_id)
                    q.append(ne_id)
        
                    if color[ne_id][0] == 1:  #新しく塗った色が赤だった
                        R += 1
                    else:
                        B += 1
                        
                #既に塗られていて,now_idと同じ色だったら(同色で隣接してしまうので)二部グラフではない
                elif color[ne_id][0] == color[now_id][0]: 
                    return False
    
        
    
        color_by_group.append((start_id, R, B))   #グループ番号(BFSの祖先の頂点番号), 赤の個数, 青の個数
    
        
    return color_by_group

#G = [[], [3], [3,4,5], [1,2], [2], [2], [7], [6]]
#ans = is_bipartite(7, 5, G)
#print(ans)  [(1, 2, 3), (6, 1, 1)]  
#↑連結成分が2個あって, (祖先のid, 赤の個数, 青の個数)
