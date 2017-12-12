# алгоритм определения простого числа
m = int(input())
k = 0
for i in range(1, m):
    if m % i == 0:
        print(i)
        k += 1
if k == 1:
    print("число является простым")
