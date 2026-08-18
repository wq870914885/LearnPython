# 具身智能仿真 · 学习笔记

> 对应路线：`LearnStep.md`  
> 本文件持续追加：先 Python 基础 → NumPy → 后续数学 / 仿真等  
> 每条尽量包含：**含义 · 例子 · 输出**

---

# 第 0 章 · Python 工程基础

---

## 一、变量与基本类型

### 1. 变量

**含义**：名字绑定到一个对象。`=` 不是「数学相等」，是「让左边这个名字指向右边」。

```python
x = 10
y = x
print(x, y)
x = 20
print(x, y)   # y 仍是 10，因为 x 改成指向新对象 20
```

**输出示例**：

```text
10 10
20 10
```

---

### 2. 数字（int / float）

**含义**：整数、浮点数。常用运算 `+ - * / // % **`。

```python
print(3 + 2)
print(3 / 2)    # 真除法，结果是 float
print(3 // 2)   # 整除
print(3 % 2)    # 余数
print(2 ** 3)   # 幂
print(type(3), type(3.0))
```

**输出示例**：

```text
5
1.5
1
1
8
<class 'int'> <class 'float'>
```

---

### 3. 字符串 str

**含义**：文本。可用 `'` / `"`；常用拼接、切片、f-string。

```python
name = '张三'
print(name)
print(name[0])
print(name + '你好')
print(f'姓名：{name}，长度：{len(name)}')
```

**输出示例**：

```text
张三
张
张三你好
姓名：张三，长度：2
```

---

## 二、容器：list / tuple / dict / set

### 1. list 列表 —— 有序、可变

**含义**：`[]`，可增删改，元素可重复。仿真里常存一批物体、一批轨迹点。

```python
li = [10, 20, 30]
print(li)
print(li[1])
li.append(40)
li[0] = 99
print(li)
print(li[0:2])
```

**输出示例**：

```text
[10, 20, 30]
20
[99, 20, 30, 40]
[99, 20]
```

---

### 2. tuple 元组 —— 有序、不可变

**含义**：`()`，只能查，不能改。适合「一组固定返回值」、当字典键的一部分。

```python
t = (10, 20, 30)
print(t)
print(t[1])
print(type(t))
# t[1] = 99   # 会报错：TypeError
```

**输出示例**：

```text
(10, 20, 30)
20
<class 'tuple'>
```

**和 list 对比**：list 能改；tuple 改不了，更「安全」当地图坐标、RGB 等固定组合。

---

### 3. dict 字典 —— 键值对

**含义**：`{键: 值}`，用键查找。描述一个物体的多种属性最合适。

```python
student = {'name': '小明', 'age': 18, 'score': 90}
print(student['name'])
print(student.get('tel', '暂无'))
student['score'] = 95
student['city'] = '上海'
print(student)
print(student.keys())
print(student.values())
```

**输出示例**：

```text
小明
暂无
{'name': '小明', 'age': 18, 'score': 95, 'city': '上海'}
dict_keys(['name', 'age', 'score', 'city'])
dict_values(['小明', 18, 95, '上海'])
```

遍历键值：

```python
for k, v in student.items():
    print(f'{k}:{v}')
```

**输出示例**：

```text
name:小明
age:18
score:95
city:上海
```

---

### 4. set 集合 —— 去重、无序

**含义**：`{}` 装一堆元素（空集合必须用 `set()`）。自动去重；支持交并集。

```python
s = {1, 2, 2, 3, 3, 3}
print(s)
s.add(4)
print(s)
print({1, 2, 3} & {2, 3, 4})  # 交集
print({1, 2, 3} | {2, 3, 4})  # 并集
```

**输出示例**（集合无序，打印顺序可能不同）：

```text
{1, 2, 3}
{1, 2, 3, 4}
{2, 3}
{1, 2, 3, 4}
```

---

## 三、控制流与推导式

### 1. if / elif / else

**含义**：按条件分支执行。

```python
score = 85
if score >= 90:
    print('优秀')
elif score >= 60:
    print('及格')
else:
    print('不及格')
```

**输出示例**：

```text
及格
```

---

### 2. for 循环

**含义**：按顺序取出可迭代对象里的每一项。

```python
for x in [10, 20, 30]:
    print(x)

for i in range(3):
    print(i)
```

**输出示例**：

```text
10
20
30
0
1
2
```

---

### 3. while 循环

**含义**：条件为真就一直循环；记得改条件，避免死循环。

```python
i = 1
s = 0
while i <= 3:
    s = s + i
    i = i + 1
print(s)
```

**输出示例**：

```text
6
```

---

### 4. 推导式

**含义**：用一行生成新列表/字典等，等价于短 for。

```python
squares = [i * i for i in range(1, 6)]
print(squares)

evens = [i for i in range(1, 11) if i % 2 == 0]
print(evens)
```

**输出示例**：

```text
[1, 4, 9, 16, 25]
[2, 4, 6, 8, 10]
```

**习惯**：写 `新列表 = [表达式 for ...]`，不要写 `[旧列表.append(x) for ...]`。

---

## 四、函数

### 1. 定义与返回值

**含义**：把一段逻辑打包，传入参数，`return` 结果。项目里「算钱 / 算变换」都应是函数。

```python
def add(a, b):
    return a + b

print(add(3, 5))
```

**输出示例**：

```text
8
```

---

### 2. 默认参数

**含义**：调用时可省略，用默认值。

```python
def greet(name, msg='你好'):
    print(f'{msg}, {name}')

greet('小明')
greet('小明', '早上好')
```

**输出示例**：

```text
你好, 小明
早上好, 小明
```

注意：默认参数不要用可变对象（如 `def f(li=[])`），容易踩坑。

---

### 3. 可变对象引用：`b = a` 不是复印

**含义**：对 list/dict 等，`b = a` 让两个名字指向**同一对象**；改 `b` 会反映到 `a`。

```python
a = [1, 2]
b = a
b.append(3)
print(a)
print(b)
print(a is b)   # True，同一个对象
```

**输出示例**：

```text
[1, 2, 3]
[1, 2, 3]
True
```

需要独立副本：

```python
a = [1, 2]
b = a.copy()    # 或 a[:]
b.append(3)
print(a)
print(b)
```

**输出示例**：

```text
[1, 2]
[1, 2, 3]
```

函数传 list 时同理：函数内部 `append` 可能改到外面的列表。

---

## 五、类与对象

### 1. 类、`__init__`、方法

**含义**：用类描述「一类东西」；对象是具体实例。仿真里机器人、环境、传感器都适合做成类。

```python
class Robot:
    def __init__(self, name):
        self.name = name
        self.joint = 0.0

    def move(self, delta):
        self.joint = self.joint + delta
        print(f'{self.name} joint={self.joint}')

r = Robot('arm1')
r.move(0.5)
r.move(0.2)
```

**输出示例**：

```text
arm1 joint=0.5
arm1 joint=0.7
```

- `__init__`：创建对象时自动调用，做初始化  
- `self`：当前这个对象自己  

---

### 2. 简单继承

**含义**：子类复用父类，再扩展。

```python
class Sensor:
    def __init__(self, name):
        self.name = name

    def read(self):
        return None

class Camera(Sensor):
    def read(self):
        return f'{self.name}: RGB frame'

cam = Camera('front')
print(cam.read())
```

**输出示例**：

```text
front: RGB frame
```

---

## 六、模块与导入

### 1. `import` / `from ... import`

**含义**：复用别人或自己文件里的函数/类，避免一个文件写爆。

```python
import math
print(math.sqrt(9))

from math import factorial
print(factorial(5))
```

**输出示例**：

```text
3.0
120
```

自己拆文件示例（概念）：

```text
my_project/
  utils.py      # def normalize(...): ...
  main.py       # from utils import normalize
```

---

## 七、工程习惯

### 1. 虚拟环境与依赖

**含义**：每个项目独立一套包，避免版本互相污染。

```bash
# venv 示例（Windows PowerShell）
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install numpy
pip freeze > requirements.txt
pip install -r requirements.txt
```

`conda` 同理：创建环境 → `conda activate` → `conda/pip install`。

---

### 2. 会读报错栈

**含义**：报错最后一行是类型和原因；上面 traceback 指出出错文件与行号。

常见类型：

| 类型 | 常见原因 |
|------|----------|
| `TypeError` | 类型不对，如数字和字符串乱加 |
| `ValueError` | 类型对但值不合法 |
| `IndexError` | 下标越界 |
| `KeyError` | 字典没有这个键 |
| `NameError` | 变量名未定义 |
| `AttributeError` | 对象没有这个属性/方法 |

```python
li = [1, 2, 3]
# print(li[10])
# IndexError: list index out of range
```

---

### 3. 读开源 README 并跑通示例

**习惯步骤**：

1. 看 README 的 Install / Quickstart  
2. 建虚拟环境，按文档装依赖  
3. 先跑官方最小示例，再改自己的路径/参数  
4. 报错先搜完整报错信息  

仿真岗位大量时间花在「按文档把别人仓库跑起来」。

---

### 4. 文件读写、JSON、`pathlib`

**文本**：

```python
from pathlib import Path

p = Path('demo.txt')
p.write_text('hello\n', encoding='utf-8')
print(p.read_text(encoding='utf-8'))
```

**输出示例**：

```text
hello
```

**JSON**（配置、标注常用）：

```python
import json
from pathlib import Path

data = {'name': 'demo', 'joint': [0.1, 0.2]}
Path('demo.json').write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
loaded = json.loads(Path('demo.json').read_text(encoding='utf-8'))
print(loaded)
```

**输出示例**：

```text
{'name': 'demo', 'joint': [0.1, 0.2]}
```

`pathlib.Path` 比字符串拼路径更清晰：`Path('data') / 'images' / '0.png'`。

---

## 八、Python 基础自测

1. `b = a` 之后 `b.append(1)`，`a` 会变吗？（a 是 list）  
2. 字典没有的键，用 `[]` 和用 `get` 有什么差别？  
3. 为什么函数默认参数不要写 `def f(x=[])`？  
4. `(3,)` 这种写法是 list 还是 tuple？  

**简答**：1. 会变  2. `[]` 抛 `KeyError`，`get` 可返回默认值  3. 默认列表会被多次调用共享  4. tuple  

**完成标准（对照 LearnStep）**：能把程序拆成「输入 → 计算函数 → 打印/保存」，而不是全写在一起。

---

# 第 1 章 · NumPy（数组基本功 · 到变形）

运行前：

```python
import numpy as np
```

---

## 一、创建数组

### 1. `np.array` —— 把列表等变成数组

**含义**：用 Python 的 list / tuple 等生成 NumPy 数组，后续才能用向量化运算。

```python
a = np.array([10, 20, 30])
print(a)
print(type(a))
```

**输出示例**：

```text
[10 20 30]
<class 'numpy.ndarray'>
```

二维：

```python
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
```

**输出示例**：

```text
[[1 2 3]
 [4 5 6]]
```

---

### 2. `np.zeros` —— 全 0 数组

**含义**：按给定形状创建，元素全是 `0`。仿真里常用来初始化状态、占位。

```python
z = np.zeros((2, 3))
print(z)
print(z.dtype)   # 默认一般是 float64
```

**输出示例**：

```text
[[0. 0. 0.]
 [0. 0. 0.]]
float64
```

指定整数类型：

```python
z2 = np.zeros((2, 2), dtype=int)
print(z2)
```

**输出示例**：

```text
[[0 0]
 [0 0]]
```

---

### 3. `np.ones` —— 全 1 数组

**含义**：形状自定，元素全是 `1`。

```python
o = np.ones((2, 2))
print(o)
```

**输出示例**：

```text
[[1. 1.]
 [1. 1.]]
```

---

### 4. `np.eye` —— 单位矩阵

**含义**：对角线为 `1`、其余为 `0` 的方阵。旋转/变换里经常出现单位阵 `I`。

```python
e = np.eye(3)
print(e)
```

**输出示例**：

```text
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
```

---

### 5. `np.arange` —— 等差序列（类似 `range`）

**含义**：`np.arange(起点, 终点, 步长)`，**不含终点**。步长可以是小数。

```python
print(np.arange(5))           # 0~4
print(np.arange(0, 10, 2))    # 0,2,4,6,8
print(np.arange(0, 1, 0.3))
```

**输出示例**：

```text
[0 1 2 3 4]
[0 2 4 6 8]
[0.  0.3 0.6 0.9]
```

---

### 6. `np.linspace` —— 等分区间

**含义**：`np.linspace(起点, 终点, 个数)`，在区间内均匀取点，**默认包含终点**。适合采样、画曲线。

```python
print(np.linspace(0, 1, 5))
```

**输出示例**：

```text
[0.   0.25 0.5  0.75 1.  ]
```

**和 `arange` 对比**：

| | `arange` | `linspace` |
|--|----------|------------|
| 控制方式 | 步长 | 个数 |
| 终点 | 一般不含 | 默认含 |
| 典型用途 | 整数索引、周期 | 均匀采样 |

---

## 二、数组属性

先准备一个二维数组：

```python
b = np.array([[1, 2, 3],
              [4, 5, 6]])
print(b)
```

```text
[[1 2 3]
 [4 5 6]]
```

---

### 1. `shape` —— 形状（各维长度）

**含义**：元组，表示每一维有多少个元素。  
- 一维 `(3,)`：长度为 3 的向量  
- 二维 `(2, 3)`：2 行 3 列  
- 三维 `(N, H, W)`：常见图像/批次数据  

仿真里看 `obs.shape`、矩阵是不是 `4×4`，全靠它。

```python
a = np.array([10, 20, 30])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape)
print(b.shape)
```

**输出示例**：

```text
(3,)
(2, 3)
```

注意：`(3,)` 和 `(3, 1)` 不是一回事——前者是一维向量，后者是 3 行 1 列的二维列向量。

---

### 2. `dtype` —— 元素数据类型

**含义**：数组里每个数的类型，如 `int32` / `int64` / `float32` / `float64`。  
同一数组元素类型统一；和 list 混装不同类型不同。

```python
a = np.array([10, 20, 30])
z = np.zeros((2, 3))
print(a.dtype)
print(z.dtype)
```

**输出示例**（具体整数位宽可能因系统略有差异）：

```text
int64
float64
```

强制类型：

```python
x = np.array([1, 2, 3], dtype=np.float32)
print(x)
print(x.dtype)
```

**输出示例**：

```text
[1. 2. 3.]
float32
```

---

### 3. `ndim` —— 维度个数

**含义**：有几个轴。`shape` 元组有多长，`ndim` 就是多少。

```python
a = np.array([10, 20, 30])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(a.ndim)  # 1
print(b.ndim)  # 2
```

**输出示例**：

```text
1
2
```

---

### 4. `size` —— 元素总个数

**含义**：所有维长度相乘。`(2, 3)` → `size = 6`。

```python
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.size)
print(2 * 3)   # 等价理解
```

**输出示例**：

```text
6
6
```

**四属性速记**：

| 属性 | 问的是什么 | 例子 `(2,3)` |
|------|------------|--------------|
| `shape` | 每维多长 | `(2, 3)` |
| `dtype` | 什么类型 | `int64` 等 |
| `ndim` | 几维 | `2` |
| `size` | 总共几个数 | `6` |

---

## 三、变形

### 1. `reshape` —— 改形状（不改数据内容顺序）

**含义**：把同一批元素重新排成新形状。元素总数必须一致：`2×3` 可以变成 `3×2`、`6`、`(6,1)`，不能变成 `2×4`。

```python
c = np.arange(6)
print(c)
print(c.reshape(2, 3))
print(c.reshape(3, 2))
print(c.reshape(-1, 2))  # -1 表示这一维自动推断
```

**输出示例**：

```text
[0 1 2 3 4 5]
[[0 1 2]
 [3 4 5]]
[[0 1]
 [2 3]
 [4 5]]
[[0 1]
 [2 3]
 [4 5]]
```

默认按 **行优先（C order）** 填：先填第一行 `0 1 2`，再第二行 `3 4 5`。

---

### 2. `ravel` / `flatten` —— 拉成一维

**含义**：多维 → 一维。

| | `ravel` | `flatten` |
|--|---------|-----------|
| 常见行为 | 尽量返回**视图**（和原数组共享数据） | 一定返回**拷贝** |
| 改原数组 | 可能影响 `ravel` 结果 | 一般不影响 `flatten` 结果 |
| 记忆 | 轻量、可能联动 | 更安全、独立一份 |

```python
d = np.arange(6).reshape(2, 3)
print('原数组 d:')
print(d)

r = d.ravel()
f = d.flatten()
print('ravel:', r)
print('flatten:', f)

d[0, 0] = 99
print('改 d[0,0]=99 后:')
print('ravel:', r)      # 常会跟着变
print('flatten:', f)    # 仍是旧数据
```

**输出示例**：

```text
原数组 d:
[[0 1 2]
 [3 4 5]]
ravel: [0 1 2 3 4 5]
flatten: [0 1 2 3 4 5]
改 d[0,0]=99 后:
ravel: [99  1  2  3  4  5]
flatten: [0 1 2 3 4 5]
```

---

### 3. `T` —— 转置（二维最常用）

**含义**：行列互换。`(2, 3)` → `(3, 2)`。旋转矩阵、矩阵乘法前常要用。

```python
m = np.arange(6).reshape(2, 3)
print(m)
print(m.shape)
print(m.T)
print(m.T.shape)
```

**输出示例**：

```text
[[0 1 2]
 [3 4 5]]
(2, 3)
[[0 3]
 [1 4]
 [2 5]]
(3, 2)
```

一维数组的 `.T` **形状不变**（仍是 `(n,)`），需要列向量时用 `reshape(-1, 1)`。

```python
v = np.array([1, 2, 3])
print(v.shape)
print(v.T.shape)
print(v.reshape(-1, 1).shape)
```

**输出示例**：

```text
(3,)
(3,)
(3, 1)
```

---

### 4. `transpose` —— 更通用的轴交换

**含义**：任意维上交换轴；二维时等价于 `.T`。

```python
m = np.arange(6).reshape(2, 3)
print(np.transpose(m))           # 同 m.T
print(np.transpose(m, (1, 0)))   # 明确：原轴1放到前面，轴0放到后面
```

**输出示例**：

```text
[[0 3]
 [1 4]
 [2 5]]
[[0 3]
 [1 4]
 [2 5]]
```

三维时（了解即可）：`img.shape == (H, W, C)`，有时要换成 `(C, H, W)`：

```python
img = np.zeros((4, 5, 3))
print(img.shape)
print(np.transpose(img, (2, 0, 1)).shape)
```

**输出示例**：

```text
(4, 5, 3)
(3, 4, 5)
```

---

## 四、NumPy 本节自测

1. `(3,)` 和 `(3, 1)` 的 `ndim` 各是多少？  
2. `np.arange(6).reshape(2, 4)` 会怎样？  
3. `a * b` 和后面要学的 `a @ b` 是一回事吗？（先留个印象：不是）  
4. 改原数组后，为什么 `ravel` 可能变、`flatten` 不变？  

**简答**：1.`1` 和 `2`  2.报错（6≠8）  3.不是  4.视图 vs 拷贝  

---

## 五、下文待写（学到再往本文件追加）

- NumPy：拼接拆分、索引、广播、`@`、聚合、`linalg`
- 再往后：机器人数学、MuJoCo、Isaac……按 `LearnStep.md` 顺序追加新章即可
