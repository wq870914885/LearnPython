# 1定义类 动态的为对象添加属性，不推荐
# class Car :
#     pass

# 创建对象
# c1 = Car()
# 动态的为对象添加属性
# c1.color = 'red'
# c1.brand = "BMW"
# c1.name = "X5"
# c1.price = 500000
#
# print(c1) # <__main__.Car object at 0x760848a0cfa0> 这个对象的内存地址
# print(c1.__dict__) # 会将这个对象中的所有属性按照字典的形式输出出来
# print(c1.color)

# 2定义类
# class Car2() :
#     # __init__ 方法是初始化的方法，会在对象创建时自动调用，可以在该方法中为对象设置对应的属性
#     # self 当前所创建出来的实例对象
#     def __init__(self , c_color , c_brand , c_name , c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car类型的对象初始化完毕，对象属性应添加")
#
# c1 = Car2('red','AITO','M7',288888)
# print(c1)
# print(c1.__dict__)
# print(c1.color)


# 实例方法
# class Car3:
#     def __init__(self , color , name , price):
#         self.color = color
#         self.name = name
#         self.price = price
#
#     def running(self):
#         print(f'{self.name}正在高速行驶......')
#     def total_cost(self,discount,rate):
#         return self.price * discount + self.price * rate
#
# c1 = Car3('黑色','问界M7',288888)
# total_cost = c1.total_cost(0.9,0.1)
# print(f'总价为{total_cost}')
# c1.running()


# 魔法方法
# 以双下划线开头和结尾的特殊方法，用于定义类的特殊行为，例如__init__
# Python会在合适的时机自动调用魔法方法
# __init__  初始化方法
# __str__   字符串表示的方法
# __eq__    比较两个对象是否相等
# __lt__,__le__ , __ge__ , __ge__   两个对象小于、小于等于、大于、大于等于

# 实例属性，类属性
# 实例属性：属于每个具体对象的属性，每个对象都是独立的（各个对象特有的数据）
# 类属性：属于类本身的属性（所有对象共享的数据）
# class Car3:
#     wheel =4          #类属性
#     tax_rate = 0.1    #类属性
#     def __init__(self , color , name , price):
#         self.color = color        #实例属性
#         self.name = name          #实例属性
#         self.price = price        #实例属性