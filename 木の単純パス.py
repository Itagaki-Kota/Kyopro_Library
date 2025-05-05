# 連結な木グラフ(閉路が無い)において,任意の頂点(S)から任意の頂点(Goal)までの単純パスを出力する 

from collections import deque
q = deque()  # FIFO

S = 1  # スタートの頂点番号 
goal_list = [8, 9, 6, 4]  # ゴールの頂点番号を列挙する

N = int(input()) # 頂点数  頂点番号は1～N
M = int(input()) # 辺の本数


G = [[] for i in range(N + 1)] # 先頭はダミー。 インデックスでそのまま頂点番号にアクセスできる

# 無向グラフの隣接リストを作成
for _ in range(M):
     U, V = map(int, input().split())  # 頂点番号で受け取る
     G[U].append(V)
     G[V].append(U)



### BFSで各頂点に, スタート頂点からの移動コストを記入していく###
def check_around(v_id, G, costs):
    
    global q
 
    for search_id in G[v_id]: 
        if costs[search_id] == None:
            costs[search_id] = costs[v_id] + 1 
            q.append(search_id)
            
costs = [None for i in range(N + 1)]
costs[S] = 0 
 
q.append(S) # 頂点番号で入れる     
 
while q:                            
    now_loc = q.popleft()                
 
    check_around(now_loc, G, costs)                 
                                                





# Sから, それぞれのGoalまでのパスを出力
for Goal in goal_list:
    # 復元
    path = [Goal]
    now_id = Goal
    now_cost = costs[Goal]
    while len(path) != costs[Goal] + 1:
        for ne_id in G[now_id]:
            if costs[ne_id] == now_cost - 1:
                now_id = ne_id
                now_cost -= 1
                path.append(now_id)
                break
        
    path.reverse()
    print(*path)



"""
# 根(root)の頂点番号を1として, 葉(leaf)の頂点番号を列挙する
leaf_list = []

for leaf in range(2, N + 1):
    if len(G[leaf]) == 1:
        leaf_list.append(leaf)


# 根から, それぞれの葉までのパスを出力
for Goal in leaf_list:
    # 復元
    path = [Goal]
    now_id = Goal
    now_cost = costs[Goal]
    while len(path) != costs[Goal] + 1:
        for ne_id in G[now_id]:
            if costs[ne_id] == now_cost - 1:
                now_id = ne_id
                now_cost -= 1
                path.append(now_id)
                break
        
    path.reverse()
    print(*path)
"""