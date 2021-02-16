# 15654 : N과 M (5)
n, m = input().split(" ")
n = int(n)
m = int(m)
nums = list(map(int, input().split(" ")))

nums.sort()

def solve(ans, start, picked):
    if picked == m:
        print(" ".join(map(str,ans)))
        return

    for i in range(0, len(nums)):
        if ans is not None and nums[i] in ans:
            continue
        ans.append(nums[i])
        solve(ans, i+1, picked+1)
        ans.pop()

answer = list()
solve(answer, 0, 0)
