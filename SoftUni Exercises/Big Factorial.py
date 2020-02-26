fac = int(input('Factorial: '))
n = fac
f = 1
while n > 1:
    f = f * n
    n -= 1
print(f'{fac}! is equal to {f}')
