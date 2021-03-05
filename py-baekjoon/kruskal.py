# kruskal mst algorithm
v, e = input().split(" ")
v = int(v)
e = int(e)

g = dict()
edges = []
for i in range(e):
    v1, v2, w = input().split()
    edges.append([int(w), int(v1), int(v2)])

edges.sort(key=lambda x: x[0])

par = [i for i in range(v+1)]

def find(a):
    global par

    if par[a] == a:
        return a
    par[a] = find(par[a])
    return par[a]

def merge(x, y):
    global par

    px = find(x)
    py = find(y)

    if px == py:
        return
    par[py] = px

ans = 0
for i in range(len(edges)):
    cost = edges[i][0]
    u = edges[i][1]
    v = edges[i][2]
    if find(u) == find(v):
        continue
    merge(u, v)
    ans += cost

print(ans)




