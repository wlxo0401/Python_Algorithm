list = [5, 4, 14, 10, 1, 3, 2, 9, 7, 8, 6, 13, 15, 11, 12]




def bubble(x):
    for size in reversed(range(len(x))):
        for i in range(size):
            if x[i] > x[i + 1]:
                x[i], x[i + 1] = x[i + 1], x[i]
        print(x)



def select(x):
    for size in reversed(range(len(x))):
        print(x)
        max_i = 0
        for i in range(1, 1 + size):
            print("i = {}({}) max_i = {}({})".format(i, x[i], max_i, x[max_i]))
            if x[i] > x[max_i]:
                max_i = i
            x[max_i], x[size] = x[size], x[max_i]
            print(x)
            print()
            
        print("끝이 큰 수가 됐어요.")
select(list)


