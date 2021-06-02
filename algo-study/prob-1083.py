"""
1083 : 소트
"""
import sys

N = int(sys.stdin.readline().strip())  # 50
A = list(map(int, sys.stdin.readline().strip().split()))
S = int(sys.stdin.readline().strip())  # 10 ^ 6

for i in range(N):
    m = A[i]
    idx = i
    for j in range(i+1, N):
        if j > i + S:
            break
        if m < A[j]:
            m = A[j]
            idx = j
    S -= (idx - i)
    for k in range(idx, i, -1):
        A[k], A[k-1] = A[k-1], A[k]

print(" ".join(map(str, A)))