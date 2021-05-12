'''
ㅇ카드가 N X N장 N행 N열로 있다.
ㅇ각 카드는 알파벳이 하나씩 써있다.
ㅇ단어가 주어지면, 카드를 적절히 선택해 해당 단어를 만드는 것이 게임의 목표이다.
ㅇ카드를 선택할때, 같은 행, 같은 열에 있는 카드는 최대 한 장만 고를 수 있다.

단어를 만들 수 있는 가지수는?

1 <= word <= 8
4 <= cards <= 8
'''
s = set()
def backtracking(n, visit, word, card, pick, picked):
    """
    1차원 배열로 접근
    pick = [0, 1, 2] -> card[0], card[1], card[2]를 뽑았다.
    """
    if pick == 0:
        s.add("".join(map(str, sorted(picked))))
        return

    for i in range(n):
        for j in range(n):
            if not visit[i][j] and card[i][j] == word[pick-1]:
                from copy import deepcopy
                v = deepcopy(visit)
                # v = visit[:] deepcopy 대신
                for k in range(n):
                    v[i][k] = True
                    v[k][j] = True
                picked.append(i * n + j)
                backtracking(n, v, word, card, pick-1, picked)
                picked.pop()
                for k in range(n):
                    v[i][k] = False
                    v[k][j] = False

"""
def solution(word, cards):
    answer = []
    
    def DFS( L, x, y, row, col, use ):
        if L == len( word ):
            use = sorted(use)
            if use not in answer:
                answer.append(use)
            return

 
        for i in range( N ):
            for j in range( N ):
                if ( i in row ) or ( j in col ): continue
                if word[L] == C[i][j]:
                    tmp_row, tmp_col = row + [i], col + [j]
                    use.append((i,j))
                    DFS(L+1, i, j, tmp_row, tmp_col, use)
                    use.pop()
    
    
    N = len(cards)
    C = [ list(card) for card in cards ]
    
    if len(word) > N: return 0
    
    for i in range( N ):
        for j in range( N ):
            if C[i][j] == word[0]:
                DFS( 1, i, j, [i], [j] , [(i,j)] )
    
    return len(answer)
"""


def solution(word, cards):
    global s
    n = len(cards)

    if len(cards) < n:  # 행의 길이
        return 0

    visit = [[False for _ in range(n)] for _ in range(n)]

    s = set()
    backtracking(n, visit, word, cards, len(word), [])

    return len(s)

if __name__ == '__main__':
    print(solution("APPLE", ["LLZKE", "LCXEA", "CVPPS", "EAVSR", "FXPFP"]))  # 3
    print(solution("BAB", ["ZZBZ", "BAZB", "XBXB", "XBAX"]))  # 4
    print(solution("BABXZ", ["ZZBZ", "BAZB", "XBXB", "XBAX"]))  # 0