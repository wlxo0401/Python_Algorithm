
def first():
    list = [12, 30, 6, 7, 13, 8, 11, 50, 24, 2, 5, 10]
    list.sort(reverse=True)
    print("라이브러리 사용 : ",list)

def second():
    list = [12, 30, 6, 7, 13, 8, 11, 50, 24, 2, 5, 10]
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] < list[j]:
                temp = list[j]
                list[j] = list[i]
                list[i] = temp
    print("라이브러리 사용 안함 : ", list)
first()
second()
