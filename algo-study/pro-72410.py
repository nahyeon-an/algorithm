"""
신규 아이디 추천
"""
import re

def solution(new_id):
    st = new_id
    st = st.lower()
    st = re.sub('[^a-z0-9\-_.]', '', st)  # 소문자, 숫자, -, _, .을 제외한 모든 문자 제거
    st = re.sub('\.+', '.', st)  # .이 연속된 부분을 하나의 .으로 치환
    st = re.sub('^[.]|[.]$', '', st)  # .이 처음이나 끝에 위치하면 제거
    st = 'a' if len(st) == 0 else st[:15]  # 빈 문자열이라면 a 대입, 길이 15까지만 남기기
    st = re.sub('^[.]|[.]$', '', st)  # .이 처음이나 끝에 위치하면 제거
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
    return st

if __name__ == '__main__':
    ret = solution("...!@BaT#*..y.abcdefghijklm")
    print(ret)
    ret = solution("z-+.^.")
    print(ret)
    ret = solution("=.=")
    print(ret)
    ret = solution("123_.def")
    print(ret)
    ret = solution("abcdefghijklmn.p")
    print(ret)
