# задача 4 Лифт в бизнес-центре ВСОШ (2017-18)
# муниципальный этап

K = int(input())
N = int(input())
time = 0
ost = 0
for i in range(1, N + 1):
    a = int(input())
    if a > 0:
        a += ost
        if a // K > 0:
            time += i * 2 * (a // K)
        ost = a % K
        index = i
if ost > 0:
    time += index * 2
print(time)
