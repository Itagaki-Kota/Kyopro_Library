# パスカルの三角形 (PAST本p325の方がいいかもしれない)

def Pascal(N):

    if N == 1:
        return [[1]]
    elif N == 2:
        return [[1], [1,1]]


    triangle = [[1], [1,1]] + [[] for i in range(N - 2)]


    for pre_row in range(1, 1 + N - 2):
        now_row = pre_row + 1

        triangle[now_row].append(1)

        for i in range(pre_row):
            triangle[now_row].append(triangle[pre_row][i] + triangle[pre_row][i + 1])

        triangle[now_row].append(1)

    return triangle



N = int(input())
triangle = Pascal(N)

for row in triangle:
    print(*row)

