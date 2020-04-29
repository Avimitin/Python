print("Hello World")
print("你好")

x = 1
y = 'aBcDeF'
z = 'gHiJkL'
a, b, c = 3, 2, 1

print(x)
print(x+1)
print(x*3)
print(y)
print(y[0:1])
print(y*3)
print(y+"\n"+y)

input("按下回车以继续")

print(x, y, z)
print(x, end="")
print(y, end="")
print(z, end="")

print(a, b, c)

list1 = [123,123, 'abc', 'wtf']
print(list1[2])
print(list1)

abc = {'1': 'a', '2': 'b', '3': 'c'}
print('字典abc的第二位是', abc['2'])
diction = {}
input_dic = input('添加一个元素：\n')
diction['xz'] = input_dic
print('新增加的字典元素是：', diction['xz'])


# 列表堆栈
# 堆栈其实就是后进先出的概念，理解为堆箱子，最后放的箱子都
# 叠在最上面，搬运的时候也最先搬走
stack_list = [1, 2, 3, 4]
print(stack_list)
# 插入了5，堆在最上方
stack_list.append(5)
print(stack_list)
# 先删除最后加入的元素
stack_list.pop()
print(stack_list)
# 先删除最上方元素
stack_list.pop()
print(stack_list)
