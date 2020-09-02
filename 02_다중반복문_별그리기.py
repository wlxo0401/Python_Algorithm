N = 5

for i in range(N):
    print('*',end='')

print('')

for i in range(N):
    print('')
    for j in range(N):
        print('*',end='')

print('')

for i in range(N):
    print('')
    for j in range(i+1):
        print('*',end='')

print('')

for i in range(N):
    print('')
    for j in range((i+1)*2-1):
        print('*',end='')

print('')

for i in range(N):
    print('')
    for j in range(N-i):
        print('*',end='')

print('')

for i in range(N):
    print('')
    for j in range((N)-1):
        print('*',end='')

print('')

for i in range(5,0,-1):
   print('0'*(2*i - 1))


print('')


for i in range(N):
    print('')
    for j in range(2*(N-i)-1):
        print('*',end='')



print('')

N = 5
answer = ""
for i in range(N,0,-1):
    for j in range((2*i)-1):
        answer += "0"
    print(answer)
    answer = ""


for i in range(5,0,-1):
    print('*'*(i*2-1))

print('')

for i in range(N+1):
    print('')
    print(' '*(N-i),end='')
    print('*'*((i*2)-1),end='')
