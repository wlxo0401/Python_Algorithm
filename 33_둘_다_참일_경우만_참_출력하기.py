a, b = input().split()
x = int(a)
y = int(b)
if x == 1 and y == 1:
    print(1)
else:
    print(0)


a, b = input().split()
x = int(a)
y = int(b)

b1 = bool(x)
b2 = bool(y)
z = int(b1 and b2)
print(z)