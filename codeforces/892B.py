n=int(input())
A=list(map(int, input().split()))
count = 1
for j in range (n-1):
    F = False
    for i in range(j+1,n):
        if j >= i - A[i]:
            F = True
    if F == False:
        count += 1
print(count)
