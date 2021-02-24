from collections import deque


def dfs(start, n, mat):
    st = list()
    visited = [False for _ in range(1001)]
    st.append(start)

    ret = []
    while len(st) != 0:
        v1 = st.pop()
        if visited[v1]:
            continue
        visited[v1] = True
        ret.append(v1)
        for v2 in range(1000, 0, -1):
            if mat[v1][v2] == -1:
                continue
            if visited[v2]:
                continue
            st.append(v2)

    return ret


def bfs(start, n, mat):
    q = deque()
    visited = [False for _ in range(1001)]
    q.append(start)
    visited[start] = True

    ret = []
    while len(q) != 0:
        v1 = q.popleft()
        ret.append(v1)
        for v2 in range(1, 1001):
            if mat[v1][v2] == -1:
                continue
            if visited[v2]:
                continue
            visited[v2] = True
            q.append(v2)

    return ret


s = input().split(" ")
n, m, v = int(s[0]), int(s[1]), int(s[2])
mat = [[-1 for _ in range(1001)] for _ in range(1001)]

for i in range(m):
    v1, v2 = input().split(" ")
    mat[int(v1)][int(v2)] = 1
    mat[int(v2)][int(v1)] = 1

print(" ".join(map(str,dfs(v, n, mat)))) # 출력 형식을 리스트로 하다가 30분 날렸다..
print(" ".join(map(str,bfs(v, n, mat))))
