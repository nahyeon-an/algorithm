'''
0에서 255의 값을 원소로 갖는 배열 arr가 주어진다.
특정 임계값 이상의 개수를 a
임계값 미만의 개수를 b라고 할때,
a, b 차이를 최소로 하는 임계값을 return하는 solution 함수를 완성하시오

단, 조건을 만족하는 임계값이 여러개일 경우 가장 작은 수를 return 한다.

ㅇarr 길이는
1 <= arr <= 1000


ex1)
[0, 0, 255, 255, 0, 0, 255, 255, 255]
result = 1

ex2)
[1, 52, 125, 10, 25, 201, 244, 192, 128, 23, 203, 98, 154, 255]
result = 126

ex3)
[100, 50, 100, 200]
result = 51
'''


def solution(arr):
    arr.sort()
    mid = (len(arr) - 1) // 2

    for i in range(mid - 1, -1, -1):
        if arr[i] < arr[mid]:
            break

    for j in range(mid + 1, len(arr)):
        if arr[j] > arr[mid]:
            break

    if len(arr[:i+1]) < len(arr[j:]):
        th = arr[mid] + 1
    elif len(arr[:i+1]) == len(arr[j:]):
        if arr[i] == arr[j]:
            th = 0
        else:
            th = arr[i] + 1
    else:
        th = arr[i] + 1

    return th


if __name__ == '__main__':
    ret = solution([0, 0, 255, 255, 0, 0, 255, 255, 255])
    print(ret)

    ret = solution([1, 52, 125, 10, 25, 201, 244, 192, 128, 23, 203, 98, 154, 255])
    print(ret)

    ret = solution([100, 50, 100, 200])
    print(ret)

    ret = solution([1, 2, 3, 4, 5])
    print(ret)

    ret = solution([1, 1, 1, 2, 3])
    print(ret)

    ret = solution([1, 2, 3, 3, 3])
    print(ret)

    ret = solution([0, 1, 2, 2, 3])
    print(ret)

    ret = solution([100, 100, 100, 200])
    print(ret)

    ret = solution([100, 100, 100, 100])
    print(ret)
