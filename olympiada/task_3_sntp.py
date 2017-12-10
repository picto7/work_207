# задача 3 SNTP 9-11 класс

A = input()
B = input()
C = input()
a1, a2, a3 = A.split(':')
a1, a2, a3 = int(a1), int(a2), int(a3)
b1, b2, b3 = B.split(':')
b1, b2, b3 = int(b1), int(b2), int(b3)
c1, c2, c3 = C.split(':')
c1, c2, c3 = int(c1), int(c2), int(c3)
Data_1 = a1 * 3600 + a2 * 60 + a3
Data_2 = b1 * 3600 + b2 * 60 + b3
Data_3 = c1 * 3600 + c2 * 60 + c3
T_rez = round((Data_3 - Data_1) / 2)  # математическое округление числа
result = Data_2 + T_rez
hh = result // 3600
mm = (result % 3600) // 60
ss = (result % 3600) % 60
print('%02d' % hh, '%02d' % mm, '%02d' % ss, sep=':')  # дополнение числа ведущими нулями и раздел :(sep)
