n = int(input('Num: '))
f = 1
for i in range(0, n):
    f = f * n
    n -= 1
print(f)
