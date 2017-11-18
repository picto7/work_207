# http://codeforces.com/problemset/problem/892/B
n=int(input())
A=list(map(int, input().split()))
A.reverse()
right = A[0]
ans = 1
for i in range(1,n):
    if i > right:
        ans += 1
    right = max(right, A[i] + i)
print(ans)
