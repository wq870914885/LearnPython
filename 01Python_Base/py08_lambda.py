# 适用于简单函数的编写、单行的
# lambda 参数列表 : 函数体

def ou_line():
    print('-----------------------')
# 等效于
lambda : print('---------------------')

out__line = lambda : print('++++++++++++++++++')
out__line()

def add(x , y ):
    return x + y
# 等效于
addd = lambda x,y : x + y

print(add(5,6))
print(addd(5,6))

# 需求3:完成如下列表的排序操作,按照每一个元素的字符个数,从小到大排序
data_list = ["C++" , "C" , "Python" , "Java" , "JavaScript" , "Go" , "Javascript" , "Rust"]
print(data_list)

data_list.sort(key=lambda item : len(item))
print(data_list)