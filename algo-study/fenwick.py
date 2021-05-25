"""
fenwick tree
구간곱 구하기 - 업데이트를 어떻게 해야할지 모르겠다..!

0의 개수를 저장하는 펜윅과, 곱셈 결과를 저장하는 펜윅 (즉, 2개의 트리)로 구성했구요

0을 입력받으면 값을 1로 수정하고 0을 카운팅해서 기록했습니다 (값이 수정될 때 마다, 0의 개수를 업데이트했습니다)

[a, b] 구간의 곱을 출력할때, [0, a)의 0의 개수와 [0, b]의 0의 개수가 다르다면, 결과값은 0을 출력합니다.

저는 오히려 나머지 연산자의 역원에서 어려웠어요.. (이 부분은 extended euclid 이용해서 해결했습니다)

최적화된 코드는 아니지만 시도에 의의를 두었습니다.
"""
import sys

n, m, k = map(int, sys.stdin.readline().split())

arr = [0] * (n + 1)
tree = [1] * (n + 1)
zero = [0] * (n + 1)


# i번째 수까지 누적합을 계산
def prefix_sum(i):
    result = 1
    while i > 0:
        if zero[i] > 0:
            return 0
        result *= tree[i]
        i -= (i & -i)
    return result


# i번째 수를 val로 업데이트
def update(i, val, org):
    while i <= n:
        if val != 0:
            if zero[i] > 0:
                tree[i] = val
            tree[i] *= val
            tree[i] //= org
        else:
            zero[i] = 1
        i += (i & -i)


# start 부터 end까지의 구간 합을 계산
def interval_sum(start, end):
    return prefix_sum(end) // prefix_sum(start - 1)


for i in range(1, n + 1):
    x = int(sys.stdin.readline())
    arr[i] = x
    update(i, x, 1)
    print(i, x, tree)

for i in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        update(b, c, arr[b])
        arr[b] = c
        print(tree)
    else:
        print(interval_sum(b, c))