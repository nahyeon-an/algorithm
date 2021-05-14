"""
f(x) := x보다 크고 && x와 비트가 1개 또는 2개 다른 수들 중 가장 작은 수
x에서 가장 낮은 자리의 비트를 변화시키자

0010 -> 0011
0111 (7) -> 1011 (11)
"""

def solution(numbers):
    answer = []
    for num in numbers:
        bitstr = "{0:b}".format(num)
        bitarr = list(bitstr)
        for i in range(len(bitstr)-1, -1, -1):
            if bitarr[i] == '0':
                bitarr[i] = '1'
                for j in range(i+1, len(bitstr)):
                    if bitarr[j] == '1':
                        bitarr[j] = '0'
                        break
                break
        if int("".join(bitarr), 2) > num:
            answer.append(int("".join(bitarr), 2))
            continue
        for i in range(len(bitstr)):
            if bitarr[i] == '1':
                bitarr[i] = '0'
                break
        answer.append(int("1" + "".join(bitarr), 2))
    return answer

if __name__ == '__main__':
    for i in range(1, 101):
        ret = solution([i])
        print(i, solution([i]))
        print("{0:b}".format(i), "{0:b}".format(ret[0]))