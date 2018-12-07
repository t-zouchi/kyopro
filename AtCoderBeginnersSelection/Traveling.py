# 最短で目的地にたどり着くまでにかかる距離を求める
# 最短で辿りつける時間 = xの差の絶対値 + yの差の絶対値 が tiより少ない
    # 余る秒数が偶数 ー＞ その場にとどまれる
    # 余る秒数が奇数 ー＞ その場にとどまれない
# 最短で辿りつける時間 > ti 辿り着けないので終了
# これを全入力で繰り返す

n = int(input())
int_list=[]

for i in range(n):
    int_list.append(list(map(int,input().split())))
zero = (0, 0)
flag = False

for i in range(0,n):
    if i == 0:
        fast = int_list[i][1] + int_list[i][2]
        distance = int_list[i][0]
    else:
        fast = abs(int_list[i][1] - int_list[i-1][1]) + abs(int_list[i][2] - int_list[i-1][2])
        distance = int_list[i][0] - int_list[i-1][0]

    if fast - distance > 0:
        flag = False
        break
    else :
        if (distance - fast)%2 == 0:
            flag = True
        else :
            flag = False
            break

if flag:
    print("Yes")
else:
    print("No")


