list1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"] 
list2 = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]

Message = "APPLE"

def encryption(strr):
    MSG = strr
    encryption_str = ""    
    for strr in MSG:
        encryption_str += list1[list2.index(strr)]
    return encryption_str

def decryption(strr):
    MSG = strr
    decryption_str = ""    
    for strr in MSG:
        decryption_str += list2[list1.index(strr)]
    return decryption_str

encryptionn = encryption(Message)
decryptionn = decryption(encryptionn)

print("{}를 암호화 : {}".format(Message, encryptionn))
print("{}를 복호화 : {}".format(encryptionn, decryptionn))