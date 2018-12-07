a = int(input())
b = int(input())
c = int(input())
x = int(input())
counter = 0

for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            total = 500*i + 100*j + 50*k
            if total == x:
                counter = counter + 1
            elif total > x:
                break
        if total > x:
            continue
    if 500 * i > x:
        break
    if total > x:
        continue

print(counter)