def func(t):
    li = [ 'dream','dreamer', 'erase', 'eraser' ]
    for i in range(0, len(li)):
        _t = t + li[i]
        if _t == s:
            return _t
        if s.find(_t) == 0:
            return func(_t)
    


s = input()

t = s.replace("eraser", "").replace("erase", "").replace("dreamer", "").replace("dream", "")

if t == "":
    print('YES')
else:
    print('NO')


