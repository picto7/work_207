n = int(input())  # количество танцоров
p = int(input())  # номер танцора
k = int(input())  # количество шагов
Arr = []
for i in range(n):
    Arr.append(i + 1)
k_pos = k % n
for i in range(k_pos):
    if i % 2 == 0:
        for m in range(0, n, 2):
            Arr[m], Arr[m + 1] = Arr[m + 1], Arr[m]
    else:
        Arr[0], Arr[n - 1] = Arr[n - 1], Arr[0]
        for g in range(1, n - 2, 2):
            Arr[g], Arr[g + 1] = Arr[g + 1], Arr[g]
    print(Arr)
for i in range(n):
    if Arr[i] == p:
        if Arr[i] == Arr[0]:
            if Arr[-1] > Arr[1]:
                print(Arr[1], Arr[-1])
                break
            else:
                print(Arr[-1], Arr[1])
                break
        if Arr[i] == Arr[-1]:
            if Arr[-2] > Arr[0]:
                print(Arr[0], Arr[-2])
                break
            else:
                print(Arr[-2], Arr[0])
                break
        print(Arr[i - 1], Arr[i + 1])