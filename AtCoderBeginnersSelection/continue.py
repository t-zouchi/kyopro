l1 = [1, 2, 3]
l2 = [10, 20, 30]

for i in l1:
    for j in l2:
        print(i, j)
        if i == 2 and j == 20:
            print('BREAK')
            break
    else:
        continue
    break