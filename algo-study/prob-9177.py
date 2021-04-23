"""
9177 : 단어 섞기
PyPy 로는 통과, Python 으로는 50%에서 시간초과
"""
import sys

n = int(sys.stdin.readline())

for i in range(n):
    words = sys.stdin.readline().split(" ")

    len1 = len(words[0])
    len2 = len(words[1])
    mini = min(len1, len2)
    length = len1 + len2

    # dp[i][j] : word1의 i개까지, word2의 j개까지 => word3의 i+j까지 들어있는가
    dp = [[False for _ in range(len2 + 1)] for _ in range(len1 + 1)]

    if words[2][0] == words[0][0]:
        dp[1][0] = True
    elif words[2][0] == words[1][0]:
        dp[0][1] = True

    for j in range(2, length + 1):
        if j > mini:
            k = mini
        else:
            k = j
        while k >= 0:
            if k > len1 or j-k > len2:
                k -= 1
                continue
            if k != 0 and dp[k-1][j-k] and words[0][k-1] == words[2][j-1]:
                dp[k][j-k] = True
            if k != j and dp[k][j-k-1] and words[1][j-k-1] == words[2][j-1]:
                dp[k][j-k] = True
            k -= 1

    # for d in dp:
    #     print(d)

    if dp[len1][len2]:
        print("Data set {}: yes".format(i + 1))
    else:
        print("Data set {}: no".format(i + 1))
