import random

input_no = []

for i in range(8):
    ran_num = random.randint(0, 9)
    input_no.append(ran_num)

print(input_no)
max_index = 0

while(len(input_no) > 0):
    if (len(input_no) > 1):
        max_h = 0
        for i in range(0, len(input_no)):
            if max_h < input_no[i]:
                max_h = input_no[i]
                max_index = i
    else:
        max_h = input_no[0]
        max_index = 0
    input_no.pop(max_index)
    print(max_h)
print(input_no)