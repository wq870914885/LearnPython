# 导入模块

# import random
#
# for i in range(10):
#     print(random.randint(1, 100))

# 导入模块中的功能
# from random import  randint
# for i in range(10):
#     print(randint(1, 100))

# 起别名
# from random import randint as rand
# for i in range(10):
#     print(rand(1,100))

# 自定义模块
# 每个python文件都可以是一个模块

# 常量(不会发生变的数据,例如PI,常量的名称为全大写)
PI = 3.14
NAME = 'wq'

# __name__ 内置变量,表示当前模块的名字,当前值为__main__
# __name__ 是 Python 内置特殊变量，每个 .py 文件（模块）都自带这个变量。
# 它的值分两种情况：
# 文件直接运行：__name__ == '__main__'
# 文件被别的文件 import 导入：__name__ == 模块名（文件名，不带.py）
# 通俗理解：
# __name__ 用来回答一个问题：当前这个脚本是被直接执行，还是被别人导入使用？
print(__name__)

