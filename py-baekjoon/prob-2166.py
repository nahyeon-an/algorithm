# 2166 : 다각형의 면적

n = int(input()) # 3 ~ 10,000
x = []
y = []
for i in range(n):
    a, b = input().split(" ")
    x.append(int(a))
    y.append(int(b))


def ccw(idx1, idx2, idx3):
    cross_product = (x[idx2] - x[idx1]) * (y[idx3] - y[idx1]) - (x[idx3] - x[idx1]) * (y[idx2] - y[idx1])
    return cross_product


s = 0
for i in range(1, n-1):
    s += ccw(0, i, i+1)

if s < 0:
    s *= -1.0

print("{}".format(s / 2, ".1f"))

x.append(x[0])
y.append(y[0])

sum1 = sum([x[i-1] * y[i] for i in range(1, len(x))])
sum2 = sum([y[i-1] * x[i] for i in range(1, len(y))])

print((sum1-sum2)/2)
