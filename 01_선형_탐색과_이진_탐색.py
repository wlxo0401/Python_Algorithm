# 선형탐색
# import random
# numList = [1, 5, 7, 13, 50, 120, 300, 320, 400, 700]

# 선형탐색
# for k in range(10):
#     cntSum = 0
#     for i in range(10000):
#         rndNUM = numList[random.randint(0, 9)]
#         for n in numList:
#             cntSum += 1
#             if n == rndNUM:
#                 break
#     print(cntSum/10000)

# 이진탐색
# for k in range(10):
#     cntSum = 0
#     for i in range(10000):
#         Start = 0
#         End = len(numList) - 1
#         Key = int((Start+End) / 2)        
#         V = random.randint(Start, End)
#         while True:
#             cntSum += 1
#             if numList[V] == numList[Key] or Start == End:
#                 break
#             elif numList[Key] < numList[V]:
#                 Start = Key + 1
#                 Key = int((Start+End) / 2)
#             elif numList[Key] > numList[V]:
#                 End = Key - 1
#                 Key = int((Start + End) / 2)
#     print(cntSum/10000)

# 정수를 계속 입력 받아서 저장합니다.
# 1. 만약 0을 입력하면 프로그램을 종한다.
# 2. 입력값이 중복 된다면 "중복값이 있습니다."를 출력하고 다시 입력받는다.(선형탐색)
# 3. 중복값이 없다면, 오름차순 형태로 나열될 수 있도록 저장합니다.(정렬함수 사용 금지, 선형탐색)
# 4. 정상적으로 입력이 끝나면 "총 xx개의 정수가 저장되었습니다."를 출력합니다.
# 5. 음수를 입력하면, 해당 음수의 양수값(-10이라면 10을 검색)을 찾아서 위치를 알려줍니다.(이진탐색)
# 6. 찾는 값이 없다면, "찾는 값이 없습니다."를 출력하고 다시 입력 상태로 돌아옵니다.


numList = []

while True:
    tmp = int(input("값을 입력해주세요 : "))
    if tmp == 0:
        break

    if tmp > 0:
        if len(numList) == 0:
            numList.append(tmp)
        else:
            for i, v in enumerate(numList):
                if tmp == v:
                    print("중복값이 있습니다.")
                    break
                if tmp < v:
                    numList.insert(i, tmp)
                    break
                if i == len(numList)-1:
                    numList.append(tmp)
                    break
        print(numList)
        print("{}개의 정수가 저장되었습니다.".format(len(numList)))
    else:
        lookup = -tmp
        start = 0
        end = len(numList) - 1
        key = int((start+end) / 2)
        while True:
            if start > end:
                print("찾는 값이 없습니다.")
                break
            if numList[key] == lookup:
                print('{}(은)는 {}번째 위치에 있습니다.'.format(lookup, key))
                break
            elif numList[key] < lookup:
                start = key + 1
                key = int((start + end) / 2)
            else:
                end = key - 1
                key = int((start + end) / 2)
















