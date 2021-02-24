# 1167 : 트리의 지름

v = int(input()) # 2 ~ 100000
graph = {}
for i in range(v):
    s = input().split(" ")
    n = int(s[0])
    graph[n] = []
    for j in range(1, len(s)-1, 2):
        graph[n].append([int(s[j]), int(s[j+1])])

maxW = -1
idx = 0
def dfs(start, w, visit):
    global maxW, idx

    if maxW < w:
        maxW = w
        idx = start

    for pair in graph[start]:
        if not visit[pair[0]]:
            visit[pair[0]] = True
            dfs(pair[0], w + pair[1], visit)
            visit[pair[0]] = False


visited = [False for _ in range(v+1)]
visited[1] = True
dfs(1, 0, visited)

visited = [False for _ in range(v+1)]
visited[idx] = True
dfs(idx, 0, visited)

print(maxW)