import sys
sys.setrecursionlimit(10 ** 9)

def solve(s):
    if len(s) < 3:
        return s

    ret = ''

    idx = s.find('110')
    if idx == -1:
        return s
    chunk = s[idx:idx + 3]
    sub = s[:idx] + s[idx + 3:]

    i = sub.find('111')
    print(i)
    if i == -1:
        i = sub.find('110')
        pass
    if i == 0:
        ret += chunk
        i = 1
    else:
        ret += sub[:i-1] + chunk
    ret += solve(sub[i-1:])

    return ret


def solution(s):
    answer = []
    for string in s:
        # print(solve(string))
        answer.append(solve(string))

    return answer

if __name__ == '__main__':
    # ["1101","100110110","0110110111"]
    print(solution(['1110']))
    print(solution(["100111100"]))
    print(solution(["0111111010"]))
    print(solution(['111110']))