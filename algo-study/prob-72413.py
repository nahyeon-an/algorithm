def solution(n, s, a, b, fares):
    inf = 50000000
    # graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dist = [[inf for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n+1):
        dist[i][i] = 0

    # 노드 : 1~n
    for f in fares:
        dist[f[0]][f[1]] = f[2]
        dist[f[1]][f[0]] = f[2]

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # print(dist)
    for d in dist:
        print(d)
    # print(dist[s][a])
    # print(dist[s][b])
    m = inf
    for k in range(1, n + 1):
        if m > dist[s][k] + dist[k][a] + dist[k][b]:
            m = dist[s][k] + dist[k][a] + dist[k][b]

    return m

if __name__ == '__main__':
    ret = solution(7, 3, 4, 1, 	[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]])
    print(ret)
    ret = solution(6, 4, 5, 6, [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]])
    print(ret)