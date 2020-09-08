def fibonacci(n):
    if n < 0:
        print("에러")
    if n <= 1:
        return n
    f1 = 0
    f2 = 1
    for i in range(2, n + 1):
        fn = f1 + f2
        f1 = f2
        f2 = fn
    return fn



def Q1():
    qq = input()
    qqL = []
    for i in qq:
        qqL.append(i)
    qqL.reverse()
    print(''.join(qqL))

def Q2():
    Word = input()
    WordL = []
    for i in Word:
        WordL.append(i)
    WordL.reverse()
    for i in range(len(Word)):
        if Word[i] != WordL[i]:
            print("떙")
            break
        elif len(Word) == (i + 1):
            print("통과입니다~")
Q2()