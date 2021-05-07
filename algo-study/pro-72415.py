"""
카드짝 맞추기
"""
def solution(board, r, c):
    answer = 0

    # [r][c]에서 시작
    # 이동 조작
    # 1. 4방향으로 1칸씩
    # 2. ctrl + 방향키 = 누른 방향에서 가장 가까운 카드 = 카드 없으면 가장 마지막 칸
    # = 이동 할 수 없으면 움직이지 않음
    # 3. 카드 뒤집기 = enter (앞면이 2개이고 그림이 같으면 사라짐)
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    from collections import deque
    dq = deque()
    dq.append([r, c])

    visit = [[-1 for _ in range(4)] for _ in range(4)]
    visit[r][c] = 0
    card = board[r][c]
    c = [r, c]  # 카드 위치

    while len(dq) > 0:
        cur = dq.popleft()

        posr = cur[0]
        posc = cur[1]

        if card != -1 and card == board[posr][posc]:
            board[c[0]][c[1]] = 0
            board[posr][posc] = 0
            c = [-1, -1]
            card = -1
        if card == -1 and board[posr][posc] != 0:
            c = [posr, posc]
            card = board[posr][posc]

        # 4방향
        for i in range(4):
            if 0 <= posr + dr[i] < 4 and 0 <= posc + dc[i] < 4 \
                    and visit[posr+dr[i]][posc+dc[i]] == -1:
                visit[posr+dr[i]][posc+dc[i]] = visit[posr][posc]+1
                dq.append([posr+dr[i], posc+dc[i]])
        # ctrl + 방향키
        for i in range(4):
            posr, posc = cur[0], cur[1]
            while True:
                posr += dr[i]
                posc += dc[i]
                if posr < 0 or posr >= 4 or posc < 0 or posc >= 4\
                        or board[posr][posc] != 0:
                    posr -= dr[i]
                    posc -= dc[i]
                    break
            if visit[posr][posc] == -1:
                visit[posr][posc] = visit[cur[0]][cur[1]] + 1
                dq.append([posr, posc])

    return answer

if __name__ == '__main__':
    ret = solution([[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]], 1, 0)
    print(ret)
    ret = solution([[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]], 0, 1)
    print(ret)