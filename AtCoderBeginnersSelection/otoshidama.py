import sys

N, Y = map(int,input().split(" "))
x,y,z = 0,0,0

for x in range(N, -1, -1):
    if (10000*x) > Y:
        continue
    for y in range(N-x, -1, -1):
        if (10000*x+5000*y) > Y:
            continue
        z = N-x-y
        if (10000*x+5000*y+1000*z) > Y:
            continue
        if (10000*x+5000*y+1000*z) == Y:
            if(x+y+z==N):
                print('{0} {1} {2}'.format(x, y, z))
                sys.exit()
            continue
            
print('{0} {1} {2}'.format(-1, -1, -1))

