# с клавиатуры вводится число N, а затем – N целых чисел.
# Определить минимальное и максимальное среди двузначных чисел,
# которые делятся на 3. Если таких чисел не было, вывести "нет".
M=-1000000
m=1000000
n=int(input())
for i in range(1,n+1):
    x=int(input())
    z=str(x)
    if x<m and x!=0 and x%3==0 and len(z)==2:
        m=x
    if x>M and x!=0 and x%3==0 and len(z)==2:
        M=x
if m==1000000:
    print("нет")
else:
    print(m)
if M==-1000000:
    print("нет")
else:
    print(M)
