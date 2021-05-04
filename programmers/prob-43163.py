"""
단어변환 (위상정렬 같다..)
변환불가능 => 0 리턴
words 길이 : 3 ~ 50

hit - hot - dot, lot - .. - cog
"""
def solution(begin, target, words):
    answer = 0
    length = len(begin)  # 단어의 길이

    # target이 words에 들어있어야 함
    if target not in words:
        return 0

    from collections import deque

    dq = deque()
    dq.append(begin)

    wlen = len(words)
    visit = [False for _ in range(wlen)]

    while len(dq) > 0:
        now = dq.popleft()
        print(now)
        answer += 1
        if now == target:
            break
        for j in range(wlen):
            diff = 0
            for i in range(length):
                if now[i] != words[j][i]:
                    diff += 1

            if diff == 1 and not visit[j]:
                dq.appendleft(words[j])
                visit[j] = True

    return answer-1

if __name__ == '__main__':
    # print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4 ok
    # print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", ]))  # 0 ok
    # print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # 4 ok
    # print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))  # 0 ok
    # print(solution("hit", "hot", ["hot", "dot", "dog", "lot", "log"]))  # 1 ok
    # print(solution("1234567000", "1234567899", ["1234567800", "1234567890", "1234567899"]))  # 3 ok

    print(solution("hit", "cog", ["cog", "log", "lot", "dog", "hot"]))  # 4 -> 5 같은데...?