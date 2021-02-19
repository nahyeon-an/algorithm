# 1786 : 찾기 (KMP)
t = input()
p = input()

# n = len(t) # 1 ~ 1,000,000
# m = len(p) # 1 ~ 1,000,000

def get_partial_match(s):
    m = len(s)
    pi = [0 for _ in range(m)]
    begin = 1
    matched = 0

    while begin+matched < m:
        if s[begin+matched] == s[matched]:
            matched += 1
            pi[begin + matched - 1] = matched
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]
    return pi

def kmp(str1, str2):
    n = len(str1)
    m = len(str2)

    ret = []
    pi = get_partial_match(str2)
    begin = matched = 0

    while begin <= n-m:
        if matched < m and str1[begin+matched] == str2[matched]:
            matched += 1
            if matched == m:
                ret.append(str(begin+1))
        else:
            if matched == 0:
                begin += 1
            else:
                begin += matched - pi[matched-1]
                matched = pi[matched-1]

    return ret

result = kmp(t, p)
print(len(result))
print(" ".join(result))