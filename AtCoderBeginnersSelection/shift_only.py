n = input()
li = input().split()
li = [int(s) for s in li]
counter = 0

while (len([i for i in li if i % 2 == 1]) < 1):
    counter = counter + 1
    li = list(map(lambda x: x/2, li))

print(counter)

