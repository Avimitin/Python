import collections

'''
nametuple是个用来创建自定义tuple对象的函数，
可以很方便的定义一个带有tuple不变性的数据类型
通过访问类属性来获取值
'''

# 创建一个phone类，有属性price和storage，
Phone = collections.namedtuple('phone', ['price', 'storage'])

# 创建Phone的两个实例
XiaoMi = Phone('2999', '64G')
Apple = Phone('5999', '256G')

# 可以通过属性来调取tuple中的值
print(XiaoMi.price)
print(Apple.storage)

# 同时类属性也是被自定义的
print(isinstance(XiaoMi, Phone))
print(isinstance(Apple, tuple))
print(type(Phone))
print(type(Apple))
