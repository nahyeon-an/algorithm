"""
순위 검색
시간초과...
"""
def binary_search(st, end, target, arr):
    while st <= end:
        mid = (st + end) // 2
        if arr[mid] >= target:
            end = mid -1
        else:
            st = mid + 1
    return st

def solution(info, query):
    from itertools import combinations

    answer = []

    # info의 가능한 조합을 모두 만듦
    info_dict = dict()
    for i in info:
        i = i.split()
        for j in range(5):
            temp = combinations(i[:-1], j)
            for c in temp:
                key = "".join(c)

                if key not in info_dict:
                    info_dict[key] = []
                info_dict[key].append(int(i[-1]))

    for k in info_dict:
        info_dict[k] = sorted(info_dict[k])

    for q in query:
        q = q.split()
        target = int(q[-1])
        search = ''
        for item in q[:-1]:
            if item != 'and' and item != '-':
                search += item
        if search not in info_dict:
            answer.append(0)
            continue
        l = len(info_dict[search])
        idx = binary_search(0, l - 1, int(target), info_dict[search])
        answer.append(l - idx)  # 효율성의 핵심...;;

    return answer

if __name__ == '__main__':
    ret = solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],\
                   ["java and backend and junior and pizza 100",
                    "python and frontend and senior and chicken 200",
                    "cpp and - and senior and pizza 250",
                    "- and backend and senior and - 150",
                    "- and - and - and chicken 100",
                    "- and - and - and - 150",
                    "cpp and - and - and - 150",
                    "- and - and - and - 0",
                    "- and - and - and - 1000",
                    "cpp and - and senior and pizza 0",
                    "cpp and - and senior and pizza 1000"])
    print(ret)
