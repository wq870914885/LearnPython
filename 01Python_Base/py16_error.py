# 异常(也称为Bug)就是程序运行过程中出现的错误,它会中断程序的正常执行流程。
# 作用:
# 保证数据、逻辑的正确性,避免程序执行混乱
# 在开发阶段,尽量发现更多的问题,尽早解决问题,保障程序正常执行

# 程序运行过程中出现异常,有两种处理方案:
# 1.不做处理:整个程序因为一个Bug,中断执行。(之前编程的呈序)
# 2.捕获异常:按照我们自己的处理方式,处理完异常,程序继续执行。

# try:
#     print('=====================')
#     print(my_name)  #NameError: name 'my_name' is not defined
#     print('=====================')
# except NameError as e:
#     print('程序运行出错请联系管理员\n',e)
#

try:
    print('=====================')
    print(my_name)  #NameError: name 'my_name' is not defined
    print('=====================')
except Exception as e:  #捕获所有的异常
    print('程序运行出错',e)
finally: #无论程序是否正常运行，finally中的代码都会运行
    print('释放资源~')