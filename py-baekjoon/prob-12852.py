"""
반복문 -> 시간초과
"""
# 12852 : 1로 만들기 2
n = int(input())  # 1 ~ 1000000

ans = dict()
def solve(here, path):
    global ans

    if here == 1:
        if len(path) not in ans:
            ans[len(path)] = " ".join(map(str, path))
        return

    if len(path) in ans:
        return

    if here % 3 == 0:
        path.append(here//3)
        solve(here//3, path)
        path.pop()
    if here % 2 == 0:
        path.append(here//2)
        solve(here//2, path)
        path.pop()
    path.append(here-1)
    solve(here-1, path)
    path.pop()


p = [n]
solve(n, p)
ret = min(ans.keys())
print(ret-1)
print(ans[ret])

# 아래는 dp 반복문 풀이
# inf = 1000005
# dp = [[[inf, -1] for _ in range(1000005)] for _ in range(3)]
#
# # dp[i][j]
# # 연산 i 로 j를 만드는데 걸린 연산 횟수
# dp[0][1] = [0, 0]
# dp[1][1] = [0, 1]
# dp[2][1] = [0, 2]
#
#
# def min_three(n1, n2, n3):
#     if n1 > n2:
#         if n3 > n2:
#             return [n2, 1]
#         else:
#             return [n3, 2]
#     else:
#         if n3 > n1:
#             return [n1, 0]
#         else:
#             return [n3, 2]
#
#
# for i in range(2, n + 1):
#     if i % 3 == 0:
#         cnt, op = min_three(dp[0][i // 3][0], dp[1][i // 3][0], dp[2][i // 3][0])
#         dp[0][i] = [cnt+1, op]
#     if i % 2 == 0:
#         cnt, op = min_three(dp[0][i // 2][0], dp[1][i // 2][0], dp[2][i // 2][0])
#         dp[1][i] =[cnt+1, op]
#     cnt, op = min_three(dp[0][i - 1][0], dp[1][i - 1][0], dp[2][i - 1][0])
#     dp[2][i] = [cnt+1, op]
#
# ans, op = min_three(dp[0][n][0], dp[1][n][0], dp[2][n][0])
# ret = ""
# while n != 1:
#     ret += str(n) + " "
#     if op == 0:
#         _, op = min_three(dp[0][n//3][0], dp[1][n//3][0], dp[2][n//3][0])
#         n //= 3
#     elif op == 1:
#         _, op = min_three(dp[0][n//2][0], dp[1][n//2][0], dp[2][n//2][0])
#         n //= 2
#     else:
#         _, op = min_three(dp[0][n-1][0], dp[1][n-1][0], dp[2][n-1][0])
#         n -= 1
#
# print(ans)
# print(ret + "1")