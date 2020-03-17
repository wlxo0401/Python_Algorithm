# 년월일이 '.'(닷)으로 구분되어 입력된다.

# 년월일을

# 일월년으로 바꾸어 '-'(대쉬, 마이너스)로 구분해 출력한다.



y, w, d = map(str, input().split('.'))
if len(y) < 4:
    y = '0' + y
if len(w) == 1:
    w = '0' + w
if len(d) == 1:
    d = '0' + d

print('%s-%s-%s'%(d,w,y))