# с клавиатуры вводятся числа, ввод завершается числом 0.
# Определить, сколько было введено двузначных натуральных чисел,
# и сколько других.

n = int(input())
a = 0
b = 0
while n != 0:
    if n > 9 and n < 100:
        a += 1
    if n > 0 and (n < 10 or n > 99):
        b += 1
    n = int(input())
print(a, b)
