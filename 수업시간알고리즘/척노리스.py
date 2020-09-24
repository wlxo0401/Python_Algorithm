


def to_binary(decimal):
    binary = ""
    while decimal > 0:
        reamainder = decimal % 2
        binary += str(reamainder)
        decimal = decimal//2
    return binary[::-1]



message = input()

binary_string = ""

for ch in message:
    binary_string += to_binary(ord(ch))
    
codes = binary_string
previous_bit = ""
count = 0
answer = ""

for bit in codes:
    if bit != previous_bit and count > 0:
        if previous_bit == "1":
            answer += "0 "
        else:
            answer += "00 "
        answer += "0" * count + " "
        count = 0

    count += 1
    previous_bit = bit
if previous_bit == "1":
    answer += "0 "
else:
    answer += "00 "

answer += "0" * count
print(answer)