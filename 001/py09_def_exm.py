# 定义一个函数,根据传入的数字,计算该数字阶乘的结果。
# def fac(num):
#     sum1= 1
#     i = 1
#     while i <= num:
#         sum1= sum1* i
#         i = i + 1
#     return sum1
#
# num = int(input('输入数字计算阶乘：'))
# print(f'数字{num}的阶乘为{fac(num)}')

# 递归调用
# def jc(n):
#     if n == 1:
#         return 1
#     else:
#         return n * jc(n-1)
#
# res = int(input())
# print(jc(res))

# 定义一个函数,用于根据传入的一批商品信息(商品名、价格、数量)、优惠(优惠券、积分抵扣)、运费信息计算订单的总金额。
# 具体规则如下:
# 优惠券需要商品金额满5000才可以使用,且优惠券金额不能起超过商品总价。
# 积分抵扣需要商品总金额满5000才可以使用,100积分抵扣1元(且抵扣金额不能超过商品总价,积分只能整百抵扣)。
def cal1(n):
    pr = 0
    for i in range(len(n)):
        pr = n[i]['price']*n[i]['num1']+pr
    return pr
li = []
while True:
    dic1 = {'name':input('商品名'),'price':int(input('价格')),'num1':int(input('数量')),}
    li.append(dic1)
    exist = input('是否继续输入商品信息?Y/N:')
    if exist == 'N':
        break
prr = cal1(li)
print(f'当前总额为：{prr}')
yhq = int(input('请输入优惠券：'))
if prr >= 5000 :
    prr = prr - yhq
    if prr < 0 :
        prr = 0
print(f'当前总额为：{prr}')
jfdk = int(input('请输入积分：'))
if jfdk >= 100 and prr >= 5000:
    prr = prr-(jfdk // 100)
    if prr < 0 :
        prr = 0
print(f'当前总额为：{prr}')
yunfei = int(input('请输入运费：'))
prr = prr + yunfei
print(f'该订单的总金额为:{prr}\n使用优惠券:{yhq}\n使用积分:{jfdk}')
