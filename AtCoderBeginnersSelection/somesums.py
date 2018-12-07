n, a, b =map(int, input().split(" "))
counter = 0

for i in range(0,n+1):
    li = map(int,list(str(i)))
    s = sum(li)
    if a <= s and s <= b:
        counter = counter + i

print(counter)