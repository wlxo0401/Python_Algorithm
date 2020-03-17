class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        return len(self.data) == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]
        
priority = {'*': 3, '/': 3,
            '+': 2, '-': 2,
            '(': 1}
expr = []
operator = Stack()
result = []
tmp = input("식을 입력하세요: ")

for i in tmp:
    if i == ' ':
        continue
    expr.append(i)

for i in expr:
    if i == '(':
        operator.push(i)

    elif i in '+-*/':
        if operator.is_empty():
            operator.push(i)
        else:
            if priority[operator.peek()] >= priority[i]:
                result.append(operator.pop())
                operator.push(i)
            else:
                operator.push(i)

    elif i == ')':
        while True:
            tmp = operator.pop()
            if tmp == '(':
                break
            result.append(tmp)
    else:
        result.append(i)

while not (operator.is_empty()):
    result.append(operator.pop())

print(''.join(result))