# 2920 : 음계
l = list(map(int,input().split(" ")))

asc = True
desc = True

for i in range(len(l)-1):
    if l[i] >= l[i+1]:
        asc = False
    elif l[i] <= l[i+1]:
        desc = False

if asc:
    print("ascending")
elif desc:
    print("descending")
else:
    print("mixed")