### 頂点, 辺 すべて0-index。
### 始点0からの単一始点最短経路長 ベルマンフォード法。
### O(NM)
### アルゴ式 > アルゴリズム上級 > 最短経路問題

import copy

INF = 10**20 # 十分大きな数

N, M = map(int, input().split())
graph_edges = [[] for _ in range(M)]  # graph_edges[i]：= i 番目の辺情報
for i in range(M):
    u, v, w = map(int, input().split())  #(有向辺) u->v コストw
    graph_edges[i] = [u, v, w]

# dist_step[k][i]：k 回のステップ終了時点における 始点から頂点iへの最短経路長。
dist_step = [[INF for _ in range(N)] for _ in range(2*N+1)]
dist_step[0][0] = 0  # 始点は頂点0とした。

# k = 1, 2, …, N 回目のステップについて、
for k in range(1, N+1):
    # 前のステップの dist_step を初期値として使う
    dist_step[k] = copy.deepcopy(dist_step[k-1])

    # i = 0, 1, …, M-1 の順に、辺 i への操作を行う
    for i in range(M):
        u, v, w = graph_edges[i]  # u -> v へ コストwの辺。
        # dist_step[k][v] を置き換える (dist[k][u] が INF であれば、更新する必要はない)
        if dist_step[k][u] != INF:
            dist_step[k][v] = min(dist_step[k][v], dist_step[k][u] + w)

# N ステップ目で更新があった頂点をマークする (-INF を代入する)
# ここで、「Nステップ目に更新があった頂点」が存在しない場合、「始点が属する連結成分内には」負閉路は存在しない。
for v in range(N):
    if dist_step[N][v] != dist_step[N-1][v]:
        dist_step[N][v] = -INF

# k = N+1, N+2, …, 2N 回目のステップについて、
for k in range(N+1, 2*N+1):
    # 前のステップの dist_step を初期値として使う
    dist_step[k] = dist_step[k-1]

    # i = 0, 1, …, M-1 の順に、辺 i への操作を行う
    for i in range(M):
        u, v, w = graph_edges[i]
        # u が負閉路経由で到達可能ならば、頂点 v も負閉路経由で到達可能とする
        if dist_step[k][u] == -INF:
            dist_step[k][v] = -INF


# 終点が頂点N-1
ans = dist_step[2*N][N-1]

if ans == INF:  # 経路が存在しない
    print("impossible")
elif ans == -INF:  # いくらでも最短経路長を小さくできる。
    print("-inf")
else:
    print(ans)