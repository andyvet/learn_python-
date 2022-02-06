x = int(input())
answer = input().split()
flag, flag1 = True, False
res, res1 = 0, 0

for i in range(x):             #First is True
    if i != x - 1:
        if flag:
            if answer[i] == '0':
                res += 1
                flag = False
            else:
                res += 1
        else:
            if answer[i] == '0':
                flag = True

    else:
        if flag:
            if answer[i] == '1':
                res += 1
            else:
                flag = False

for i in range(x):             #First is False
    if i != x - 1:
        if not flag1:
            if answer[i] == '0':
                flag1 = True
        else:
            if answer[i] == '0':
                flag1 = False
                res1 += 1
            else:
                res1 += 1
    else:
        if flag1:
            res1 += 1

print(res if res <= res1 else res1)