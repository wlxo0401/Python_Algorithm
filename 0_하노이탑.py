def hanoi(num, Start, End, Sub):
    if num == 1:
        print('시작에서 보조')
        return
    hanoi(num-1, Start, Sub, End)
    print('시작에서 보조')
    hanoi(num-1, Sub, End, Start)

hanoi(3, 1, 3, 2)

