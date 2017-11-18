# http://codeforces.com/problemset/problem/892/B
# решение не проходит тест 9 превышено время выпоннеия
n=int(input())
A=list(map(int, input().split()))
count = 1
for j in range (n-1):
    F = 0
    for i in range(j+1,n):
        if j >= i - A[i]:
            F = 1
    if F == 0:
        count += 1
print(count)
