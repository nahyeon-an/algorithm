'''
6각형으로 이루어진 벌집 모양의 구조가 있다.

  1
6   2
5 7 3
  4

n = 2

     1
   12 2
11   13   3
   18  14
10   19   4
   17   15
  9  16  5
    8  6
     7
  n = 3

1 <= n <= 500


ex1)
n = 2
result = [1,6,2,7,5,3,4]

ex2)
n = 3
result = [1, 12, 2, 11, 13, 3, 18, 14, 10, 19, 4, 17, 15, 9, 16, 5, 8 ,6, 7]
'''
def draw(n, st, board):
    # n레벨 껍질을 그림
    r = len(board) // 2
    c = len(board[0]) // 2
    if n == 1:
        board[r][c] = st
        return

    r_st = r - 2 * (n-1)
    c_st = c

    board[r_st][c_st] = st
    st += 1
    for i in range(n-1):
        r_st += 1
        c_st += 1
        board[r_st][c_st] = st
        st += 1

    for i in range(n-1):
        r_st += 2
        board[r_st][c_st] = st
        st += 1

    for i in range(n-1):
        r_st += 1
        c_st -= 1
        board[r_st][c_st] = st
        st += 1

    for i in range(n-1):
        r_st -= 1
        c_st -= 1
        board[r_st][c_st] = st
        st += 1

    for i in range(n-1):
        r_st -= 2
        board[r_st][c_st] = st
        st += 1

    for i in range(n-2):
        r_st -= 1
        c_st += 1
        board[r_st][c_st] = st
        st += 1

    draw(n-1, st, board)


def solution(n):
    rows = 1 + 4 * (n-1)
    cols = 1 + 2 * (n-1)

    board = [[0 for _ in range(cols)] for _ in range(rows)]

    draw(n, 1, board)

    ret = []
    for b in board:
        # print(b)
        for num in b:
            if num != 0:
                ret.append(num)

    return ret

if __name__ == '__main__':
    print(solution(2))
    print(solution(3))
    print(solution(4))
    # print(solution(500))  # 그려지기는 함 너무 길어서 그렇지..