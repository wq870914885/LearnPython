from py11_circle import circle_area

print('=======计算披萨成本========')

# 披萨尺寸
s_radius = 10
m_radius = 20
l_radius = 30

# 计算面积
small_area = circle_area(s_radius)
medium_area = circle_area(m_radius)
large_area = circle_area(l_radius)

#计算成本
small_cost = small_area * 2
medium_cost = medium_area * 2
large_cost = large_area * 2

print(f'小披萨面积:{small_area}cm²,成本{small_cost}元')
print(f'中披萨面积:{medium_area}cm²,成本{medium_area}元')
print(f'大披萨面积:{large_area}cm²,成本{large_cost}元')

