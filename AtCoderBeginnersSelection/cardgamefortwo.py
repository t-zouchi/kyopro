n = int(input())
li = list(map(int,input().split()))

sorted_li =  sorted(li, reverse=True)

alice = 0
bob = 0

for i in range(0, len(sorted_li)):
    if i % 2 == 0:
        alice = sorted_li[i] + alice
    else:
        bob = sorted_li[i] + bob

print(alice - bob)

