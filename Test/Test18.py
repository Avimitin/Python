import Stack

s = Stack.Stack()

t = input("输入一串数字，-号弹出")

c = t.split(" ")

for char in c:
    if char == '-':
        print(s.pop())
    else:
        s.push(char)

print("\n还有%s个元素" % s.size())