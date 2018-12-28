n=int(input())
string_list=[input() for i in range(n)]

l = []
for s in string_list:
    s = s.split("-")
    for i in range(0,len(s)):
        if int(s[i][3]) <= 4:
            s[i] = int(s[i])-int(s[i][3])
        elif int(s[i][3]) > 4:
            s[i] = int(s[i])-(int(s[i][3]))+ 5

    l.append(s)

print(l)