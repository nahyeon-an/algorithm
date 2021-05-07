"""
동영상 재생 시간 : play time = 파란선
공익 광고 시간 : adv time =
동영상 재생 구간 정보 : logs = 검은선

공익광고 => 누적 재생시간이 가장 많이 나오는 곳에 삽입
=> 여러 곳이면 가장 빠른 시작 시각을 리턴

공익광고가 들어갈 시작 시간을 리턴
"""
def to_second(time):
    # 01:34:67
    return (int(time[:2]) * 60 * 60) + (int(time[3:5]) * 60) + int(time[6:])


def to_time(s):
    hour = s // 3600
    hour = "{0:02d}".format(hour)
    s %= 3600

    minute = s // 60
    minute = "{0:02d}".format(minute)

    sec = s % 60
    sec = "{0:02d}".format(sec)

    return hour + ":" + minute + ":" + sec


def solution(play_time, adv_time, logs):
    # 시간 초과
    play = to_second(play_time)
    time = [0 for _ in range(to_second('99:59:59')+1)]

    if play_time == adv_time:
        return '00:00:00'

    for log in logs:
        st, end = log.split("-")
        st = to_second(st)
        end = to_second(end)
        for i in range(st, end):
            time[i] += 1

    ad = to_second(adv_time)

    tot = 0
    idx = 0

    from collections import deque
    dq = deque()

    for i in range(ad):
        tot += time[i]
        dq.append(time[i])

    maxTot = tot

    for i in range(ad, play):
        tot -= dq.popleft()
        tot += time[i]
        dq.append(time[i])

        if maxTot < tot:
            maxTot = tot
            idx = i - ad + 1

    return to_time(idx)

def solve(play_time, adv_time, logs):
    time = [0 for _ in range(to_second('99:59:59')+1)]

    for log in logs:
        st, end = log.split("-")
        time[to_second(st)] += 1  # 시작점은 +1 표시
        time[to_second((end))] -= 1  # 끝점은 -1 표시

    for i in range(1, to_second(play_time)):
        time[i] = time[i] + time[i-1]
    for i in range(1, to_second(play_time)):
        time[i] = time[i] + time[i - 1]

    maxTot = -1
    idx = 0
    ad = to_second(adv_time)
    play = to_second(play_time)
    for i in range(ad-1, play):
        tot = time[i] - time[i - ad]
        if tot > maxTot:
            maxTot = tot
            idx = i - ad + 1

    return to_time(idx)

if __name__ == '__main__':
    ret = solution("02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"])
    print(ret)
    ret = solution("99:59:59", "25:00:00", ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"])
    print(ret)
