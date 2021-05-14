"""

"""
def solution(n, start, end, roads, traps):
    g1 = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
    g2 = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    for road in roads:
        g1[road[0]][road[1]] = road[2]
        g2[road[1]][road[0]] = road[2]

    from collections import deque
    dq = deque()

    dq.append([start, True, 0])
    use = g1
    dist = [0 for _ in range(n + 1)]
    visit = [False for _ in range(n + 1)]
    visit[start] = True
    flags = {t: -1 for t in traps}

    while len(dq) > 0:
        # flag : 현재 상태 플래그
        cur, flag, prev = dq.popleft()

        if cur == end:
            break

        if cur in traps:
            if flags[cur] != -1:
                flag = not flags[cur]
            else:
                flags[cur] = not flag
                flag = not flag

            if flag:
                use = g1
            else:
                use = g2

        for i in range(1, len(use[cur])):
            if use[cur][i] != -1:
                if i == end:
                    dist[i] = use[cur][i] + prev
                    dq.appendleft([i, flag, dist[i]])
                    visit[i] = True
                    break
                if not visit[i] or i in traps:
                    dist[i] = use[cur][i] + prev
                    dq.append([i, flag, dist[i]])
                    visit[i] = True
    return dist[end]


if __name__ == "__main__":
    ret = solution(3, 1, 3, [[1, 2, 2], [3, 2, 3]], [2])
    print(ret)
    ret = solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3])
    print(ret)
