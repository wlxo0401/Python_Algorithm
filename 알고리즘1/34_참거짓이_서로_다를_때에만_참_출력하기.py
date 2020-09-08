a, b = input().split()
x = int(a)
y = int(b)
if x != y:
    print(1)
else:
    print(0)



a, b = input().split()
x = int(a)
y = int(b)

b1 = bool(x)
b2 = bool(y)
z = int(b1 != b2)
print(z)