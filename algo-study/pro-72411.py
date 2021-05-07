"""
메뉴 리뉴얼
"""
from itertools import combinations
from collections import Counter
def solution(orders, course):
    answer = []

    for c in course:
        temp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            temp += combi
        count = Counter(temp)
        if len(count) != 0:
            m = max(count.values())
            for key, val in count.items():
                if val < 2:
                    continue
                else:
                    if val == m:
                        answer.append("".join(key))
    answer = sorted(answer)
    return answer

if __name__ == '__main__':
    ret = solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4])
    print(ret)
    ret = solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2,3,5])
    print(ret)
    ret = solution(["XYZ", "XWY", "WXA"], [2,3,4])
    print(ret)