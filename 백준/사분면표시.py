# 점 (x, y)의 사분면 번호(1, 2, 3, 4 중 하나)를 출력한다.

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print("1")
elif x < 0 and y > 0:
    print("2")
elif x < 0 and y < 0:
    print("3")
elif x > 0 and y < 0:
    print("4")