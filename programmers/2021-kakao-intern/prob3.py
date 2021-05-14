"""

"""
def solution(n, k, cmd):
    answer = ['O'] * n

    # 이동가능한 번호를 정렬해서 들고 있는다고 하자
    # -> 리스트일 때 삭제하면서 remove하는게 더 오래 걸릴거 같은데..?
    # move = list(range(n))
    # print(move)
    # 복구 되었을 때 -> 이진탐색으로 해당 위치에 삽입
    #

    st = []
    cur = k
    last = n - 1
    for c in cmd:
        if c[0] == 'C':
            st.append(cur)
            answer[cur] = 'X'
            if cur == last:
                for i in range(last-1, -1, -1):
                    if answer[i] == 'O':
                        last = i
                        break
                cur = i
            else:
                i = 0
                while i < 1:
                    cur = cur + 1
                    if answer[cur] != 'X':
                        i += 1
        elif c[0] == 'Z':
            rm = st.pop()
            answer[rm] = 'O'
            if rm > last:
                last = rm
        else:
            command, num = c.split()
            num = int(num)
            if command == 'D':
                i = 0
                while i < num:
                    cur += 1
                    if answer[cur] != 'X':
                        i += 1
            else:
                i = 0
                while i < num:
                    cur -= 1
                    if answer[cur] != 'X':
                        i += 1
    return ''.join(answer)

if __name__ == "__main__":
    ret = solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z"])
    print(ret)
    print()
    ret = solution(8, 2, ["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"])
    print(ret)