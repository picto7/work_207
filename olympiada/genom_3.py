A = input()
B = input()
n = len(A)
k = len (B)
count = 0
for i in range (n-1):
    for j in range (k-1):
        if A[i]+A[i+1] == B[j]+B[j+1]:
            count += 1
print(count)