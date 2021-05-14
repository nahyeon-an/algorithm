"""
실패 4개 존재
"""
def solution(places):
    answer = []

    for p in places:
        people = []
        for i in range(len(p)):
            for j in range(len(p[i])):
                if p[i][j] == 'P':
                    people.append([i, j])
        # 사람들 사이에 거리 구하기
        # 사람수 n, 0 ~ n-1번 사람
        n = len(people)
        dist = [[25 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(i+1, n):
                dist[i][j] = abs(people[i][0] - people[j][0]) + abs(people[i][1] - people[j][1])
        # print(dist)
        # print(people)
        flag = True
        for i in range(len(dist)):
            for j in range(len(dist[i])):
                if dist[i][j] == 1:
                    flag = False
                    break
                if dist[i][j] == 2:
                    p1, p2 = people[i], people[j]
                    if p1[0] > p2[0]: maxr, minr = p1[0], p2[0]
                    else: maxr, minr = p2[0], p1[0]

                    if p1[1] > p2[1]: maxc, minc = p1[1], p2[1]
                    else: maxc, minc = p2[1], p1[1]

                    if p1[0] == p2[0] and p[p1[0]][minc+1] == 'O':
                        flag = False
                        break
                    elif p1[1] == p2[1] and p[minr+1][p1[1]] == 'O':
                        flag = False
                        break
                    else:
                        if p[maxr][minc] == 'O' or p[minr][maxc] == 'O' \
                                or p[maxr][maxc] == 'O' or p[minr][minc] == 'O':
                            flag = False
                            break
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer

if __name__ == "__main__":
    ret = solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                    ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
                    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
                    ["OOOOO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"],
                    ["POOOO", "OPOOO", "OOOOO", "OOOOO", "OOOOO"],
                    ])
    print(ret)