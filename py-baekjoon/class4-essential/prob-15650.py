n, m = input().split(" ")
n = int(n)
m = int(m)

def backtracking(start, pick, ret):
    if pick == 0:
        print(ret)
        return

    for i in range(start, n+1):
        ret += str(i) + " "
        backtracking(i+1, pick-1, ret)
        ret = ret[:-2]

backtracking(1, m, "")