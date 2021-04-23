"""
9177 : 단어 섞기
틀린 버전
"""
from collections import deque
import sys

n = int(sys.stdin.readline())

for i in range(n):
    words = sys.stdin.readline().split(" ")

    dq = deque()
    idx1 = 0  # 첫번째 단어에서 꺼내는 인덱스
    idx2 = 0  # 두번째 단어

    #
    # dq.append([words[1][idx2], 2])
    dq.append([words[0][idx1], 1])
    dq.append( [words[1][idx2], 2] )
    idx1 += 1
    idx2 += 1

    len1 = len(words[0])
    len2 = len(words[1])
    length = len1 + len2

    dp1 = [-1 for _ in range(len1)]
    dp2 = [-1 for _ in range(len2)]
    dp = [False for _ in range(length)]

    flag = True
    while len(dq) > 0:
        cur = dq.popleft()

        for j in range(length):
            if words[2][j] == cur[0]:
                if cur[1] == 1:
                    if idx1 > 0 and j > dp1[idx1-2] and (not dp[j]):
                        dp1[idx1-1] = j
                        dp[j] = True
                        break
                elif cur[1] == 2:
                    if idx2 > 0 and j > dp2[idx2-2] and (not dp[j]):
                        dp2[idx2-1] = j
                        dp[j] = True
                        break
            if j == length - 1:
                flag = False

        if not flag:
            break

        if cur[1] == 1:
            # 첫번째 단어
            if idx1 < len(words[0]):
                dq.append([words[0][idx1], 1])
                idx1 += 1
        elif cur[1] == 2:
            # 두번째 단어 집합
            if idx2 < len(words[1]):
                dq.append([words[1][idx2], 2])
                idx2 += 1

    print(dp1)
    print(dp2)

    if not flag:
        print("Data set {}: no".format(i+1))
    else:
        print("Data set {}: yes".format(i+1))
