'''
ㅇ카드가 N X N장 N행 N열로 있다.
ㅇ각 카드는 알파벳이 하나씩 써있다.
ㅇ단어가 주어지면, 카드를 적절히 선택해 해당 단어를 만드는 것이 게임의 목표이다.
ㅇ카드를 선택할때, 같은 행, 같은 열에 있는 카드는 최대 한 장만 고를 수 있다.

단어를 만들 수 있는 가지수는?

1 <= word <= 8
4 <= cards <= 8

ex1)
"APPLE" ["LLZKE", "LCXEA", "CVPPS", "EAVSR", "FXPFP"]


result = 3

ex2)
"BAB" ["ZZBZ", "BAZB", "XBXB", "XBAX"]


result = 4

ex3)
"BABXZ" ["ZZBZ", "BAZB", "XBXB", "XBAX"]
result = 0
'''

def solution(word, cards):
    answer = 0
    return answer