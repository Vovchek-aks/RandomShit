a = int(input())
b = int(input())
x = int(input())
y = int(input())

slo = {x: 1}

for i in range(x + 1, y + 1):
    slo[i] = 0
    if i - a in slo:
        slo[i] += slo[i - a]
    if i / b in slo:
        slo[i] += slo[i / b]

print(slo[y])

