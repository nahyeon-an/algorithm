"""
2482 : 색상환
"""
import sys

n = int(sys.stdin.readline())  # 4 ~ 1000
k = int(sys.stdin.readline())  # 1 ~ n

mod = 1000000003

if k >= (n // 2 + 1):
    # 불가능한 경우
    print(0)
    sys.exit(0)

# dp1[i][j] : 1을 반드시 포함하지 X
dp1 = [[0 for _ in range(k+1)] for _ in range(n+1)]
# dp2[i][j] : 1을 포함 or 포함 X
dp2 = [[0 for _ in range(k+1)] for _ in range(n+1)]

dp1[1][1] = 0
dp2[1][1] = 1
for i in range(2, n+1):
    dp1[i][1] = (dp1[i-1][1] + 1) % mod
    dp2[i][1] = (dp2[i-1][1] + 1) % mod

for i in range(3, n+1):
    for j in range(2, k+1):
        dp1[i][j] = (dp1[i-2][j-1] + dp1[i-1][j]) % mod
        dp2[i][j] = (dp2[i-2][j-1] + dp2[i-1][j]) % mod

# 1번 카드 선택 x -> n까지 중 k 개 뽑기
# 1번 카드 선택 -> n-1까지 중 k 개 뽑기 (여집합의 개념으로 정의를 바꿈)

# ans = dp[n-3][k-1] + dp[n-1][k]
# 처음에 풀었던 방식에서 다른 점 : 나는 dp[n-2][k-1] 로 생각하고 1이 카운트 된다고 생각
# 1 ~ n-2 카드 중 1을 제외하고 k-1개를 뽑는 경우 = 2 ~ n-2 카드 중 k-1개를 뽑는 경우 = n-3개의 카드 중 k-1개를 뽑음
# 내가 정의를 1 ~ i번 카드 까지라고 해서 n-3에서 뽑는 경우와 같다는걸 생각하지 못했음
ans = dp1[n][k] + (dp2[n-1][k] - dp1[n-1][k])

print(ans % mod)

"""
for i in k:
    for j in (2 * i, n+1):
        dp[][]
"""