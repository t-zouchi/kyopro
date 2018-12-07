n = int(input())
li = [input() for i in range(n)]

l_unique_order = sorted(set(li), key=li.index)

print(len(l_unique_order))