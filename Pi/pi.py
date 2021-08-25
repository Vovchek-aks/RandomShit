from sys import stdout

n = int(input())

b = n**2
c = 0

for x in range(n):
    for y in range(n):
        if (x**2 + y**2)**0.5 <= n:
            c += 1
    stdout.write(f'{x * 100 / n}%\n')

k = c / b

print(4 * k)


input()
input()



