import sys


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())  # 고장난 버튼 개수, 0 ~ 10

nums = set(n for n in range(10))
if M > 0:
    broken_buttons = set(map(int, sys.stdin.readline().split(" ")))
    nums -= broken_buttons

ans = ""
if N == 100:
    sys.stdout.write("0")
else:
    flag_idx = -1
    big_flag = None
    for i, c in enumerate(str(N)):
        if int(c) in nums:
            continue
        else:
            # int(c) 가 가장 가까운 숫자를 찾아냄
            mini = 10
            near = -1
            for n in nums:
                if abs(n - int(c)) < mini:
                    mini = abs(n - int(c))
                    near = n

            # c > 그 숫자 인지 역인지 판별
            # c < 그 숫자 -> flag_idx 부터는 가장 큰 수 선택
            # c > 그 숫자 -> flag_idx 부터는 가장 작은 수 선택
            if int(c) > near:
                big_flag = True
            else:
                big_flag = False

            flag_idx = i
            break

    nearest = ""
    if big_flag is None:
        nearest = str(N)
    else:
        add = max(nums) if big_flag else min(nums)

        for i in range(len(str(N))):
            if i < flag_idx:
                nearest += str(N)[i]
            else:
                nearest += str(add)

    ans = abs(N - int(nearest)) + len(nearest)
    sys.stdout.write(str(ans))
