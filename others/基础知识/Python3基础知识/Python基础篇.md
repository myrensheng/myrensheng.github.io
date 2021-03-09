## 入门仪式

print：中文解释“打印”  
主要作用：将代码运行的结果显示出来，方便调试代码
主要参数：
value：任何的Python类型
sep：value之间的连接符号，默认为空格
end：结尾符号，默认为‘\n’（换行符结尾）
file：输出位置，默认为当前工作区位置


```python
print("欢迎来到Python的世界！")
```

    欢迎来到Python的世界！


```python
# value的使用
print("hello","world")

print("欢迎","来到","python的世界")
```

    hello world
    欢迎 来到 python的世界

```python
# sep的使用
print("hello","world",sep="/")

print("欢迎","来到","python的世界",sep="/")
```

    hello/world
    欢迎/来到/python的世界

```python
# end的使用
print("hello","world",end=">_<")

print("欢迎","来到","python的世界",end=">_<")
```

    hello world>_<欢迎 来到 python的世界>_<

## 变量与常量
- a=1，a为变量，1为常量


```python
a = 1
b = "hello"
print(a,b)
```

    1 hello


## 数据类型

### int()
- 整数，例如：-2，-1，0，1，2


```python
# Python可以直接计算数学表达式
1+1

2
```


```python
1+(-1)

0
```

### float()
- 小数，例如：-2.1，-1.1， 0.0 ，1.1，2.2
- 小数与整数运算，结果为小数


```python
1.1+2.2

3.3000000000000003
```


```python
1.1+(-1.1)

0.0
```


```python
# 保留小数点位数，用round()函数
round(1/3,2)

0.33
```


```python
# 小数转整数，用int()函数
int(10/3)

3
```

### str()
- 字符串，用英文引号包含数据都是str类型
- 例如："hello",'world',"""1""" 
- input()函数输出的都是str类型

Python对str类型的数据内置了许多方法
- "+"，字符串拼接
- 字符串切片
- format()，格式化输出字符串
- replace()，替换字符串
- find()，查找某个字符串的位置，没有输出为-1
- endswith()，判断字符串是以什么结尾的，返回Ture或者False
- strip()，删除字符串前后的字符串，默认为空格
- decode()，按照某种编码格式解码字符串
- encode()，按照某种编码格式编码字符串
- count()，统计某个字符在字符串中出现的次数


```python
"hello"+"||"+"world"
```


    'hello||world'

字符串切片


```python
a = "你是我的太阳"
```

取前两个字符


```python
a[:2]

'你是'
```

取最后两个字符


```python
a[-2:]
'太阳'
```

取中间的字符串


```python
a[2:4]

'我的'
```

format()，字符串内用{0}表示填充format()中的第一个字符串


```python
"你是我的{0}".format("太阳")

'你是我的太阳'
```

replace()，替换字符串中的内容


```python
"你是我的太阳".replace("太阳","月亮")

'你是我的月亮'
```

find()，查看字符中是否包含某个字符串，返回包含字符串的索引位置，不包含的时候返回-1


```python
"你是我的太阳".find("太阳")

4
```


```python
"你是我的太阳".find("月亮")

-1
```


```python
# endswith()
a.endswith("太阳")

True
```


```python
a.endswith("月亮")

False
```


```python
# strip()
"你是我的太阳  ".strip()

'你是我的太阳'
```


```python
# decode()
"你是我的太阳".encode("utf-8")

b'\xe4\xbd\xa0\xe6\x98\xaf\xe6\x88\x91\xe7\x9a\x84\xe5\xa4\xaa\xe9\x98\xb3'
```


```python
# encode()
b'\xe4\xbd\xa0\xe6\x98\xaf\xe6\x88\x91\xe7\x9a\x84\xe5\xa4\xaa\xe9\x98\xb3'.decode("utf-8")

'你是我的太阳'
```


```python
# count()
"aabbccdd".count("a")

2
```


```python
# 字符串类型的数字，转为int或者float类型
int("2")

2
```


```python
float("2.0")

2.0
```

### list()

python中最常用的数据存储方式，可以存储python中的所有数据类型。  

既然能存储，自然也可以获取：

- 可以切片获取list中的数据，
- 也可以用for...in...循环遍历数据，
- 还可以用列表表达式获取数据。  

python内置的对list的操作方法：

- “+”，将两个list合并（生成一个新的list）
- append()，“追加”，将元素一个一个的放到list的后面（操作原list）
- extend()，“延伸”，效果与“+”一样（操作原list）
- len()，获取列表的长度
- max()，列表中的最大值
- min(),列表中的最小值
- sorted()，列表排序

#### 获取list中的数据

```python
# 存储str，int，float，list，dict，tuple，set
first_list = ["A",1,2.0,["hello","world"],{"name":"zs"},("age",24),{23,21,12}]
print(first_list)

# 运行结果
['A', 1, 2.0, ['hello', 'world'], {'name': 'zs'}, ('age', 24), {12, 21, 23}]
```

索引获取list中的元素，python中的索引都是以0开始，即0表示第一个元素

```python
a = first_list[0]
print("a:",a)
b = first_list[1]
print("b:",b)
c = first_list[-1]
print("c",c)
d = first_list[2:4]
print("d:",d)
```

```python
# 运行结果
a: A
b: 1
c {12, 21, 23}
d: [2.0, ['hello', 'world']]
```

还可以用for循环遍历list

```python
# for循环遍历list中的元素值
for v in first_list:
    print(v)
```

```python
# 运行结果
A
1
2.0
['hello', 'world']
{'name': 'zs'}
('age', 24)
{12, 21, 23}
```

```python
# for循环遍历list中的索引和元素值
for i,v in enumerate(first_list):
    print(i,":",v)
```

```python
# 运行结果
0 : A
1 : 1
2 : 2.0
3 : ['hello', 'world']
4 : {'name': 'zs'}
5 : ('age', 24)
6 : {12, 21, 23}
```

python中独有的列表表达式（**常用的操作**）

```python
# 一个人名列表
name_list = ["AAA","BBB","CCC","DDD","EEE","FFF"]
# 一个坏人的人名列表
bad_people_name_list = ["DDD","FFF","EEE","GGG"]
# 在name_list中找出在bad_people_name_list中的数据
```

**常规操作**

```python
for bad in bad_people_name_list:
    if bad in name_list:
        print("bad_people:",bad)

```

```
bad_people: DDD
bad_people: FFF
bad_people: EEE

```

**骚操作**

```python
bad_people = ["bad_people:{0}".format(bad) for bad in bad_people_name_list if bad in name_list]
print(bad_people)

```

```
['bad_people:DDD', 'bad_people:FFF', 'bad_people:EEE']

```

**更骚的操作**

```python
# 集合的并集
print(set(name_list)&set(bad_people_name_list))

```

```
{'DDD', 'FFF', 'EEE'}

```

#### 内置的list方法

```python
# “+”
list1 = ["hello"]
list2 = ["world"]
list3 = list1+list2
print(list3)

```

```
['hello', 'world']

```

append()，将list2整个放到list1的后面

```python
list1 = ["hello"]
list2 = ["world"]
list1.append(list2)
print(list1)

```

```
['hello', ['world']]

```

extend()，将list2中的元素放到list1后面

```python
list1 = ["hello"]
list2 = ["world"]
list1.extend(list2)
print(list1)

```

```
['hello', 'world']

```

```python
list4 = [12,13,14,15,17,18]
print("列表长度：",len(list4))
print("列表中最大值：",max(list4))
print("列表中最小值：",min(list4))
print("列表升序排列：",sorted(list4,reverse=False))
print("列表降序排列：",sorted(list4,reverse=True))

```

```
列表长度： 6
列表中最大值： 18
列表中最小值： 12
列表升序排列： [12, 13, 14, 15, 17, 18]
列表降序排列： [18, 17, 15, 14, 13, 12]

```

### dict()

字典，数据存储类型：{key:value}。key是唯一的，value可以是任何python类型的数据  
例如：{"name":"zs","age":24,"hobby":\["basketball","music"\]}  

获取字典中的数据：

- 根据key获取value数据
- **get()获取数据（推荐）**
- dict.keys()获取所有的key数据
- dict.values() 获取所有的value数据
- dict.items() 获取dict中的key，value数据
- for ... in ...循环遍历字典  

在后端项目中，经常与json数据联用：

- json.loads()和json.dumps()

获取字典数据

```python
info_dict = {"name":"zs","age":24,"hobby":["basketball","music"]}  
print(info_dict["name"])
print(info_dict.get("name"))

```

```
zs
zs

```



```python
# 推荐get，主要是因为当查找的key不存在时,返回None，程序不会报异常
info_dict["sex"]

```

```python
---------------------------------------------------------------------------

KeyError                                  Traceback (most recent call last)

<ipython-input-15-64cabd6363a0> in <module>()
      1 # 推荐get，主要是因为当查找的key不存在时,返回None，程序不会报异常
----> 2 info_dict["sex"]
KeyError: 'sex'

```



```python
print(info_dict.get("sex"))
None

```

```python
print(info_dict.keys())
print(info_dict.values())

dict_keys(['name', 'age', 'hobby'])
dict_values(['zs', 24, ['basketball', 'music']])

```

```python
# for in 获取字典的key和value
for k,v in info_dict.items():
    print(k,":",v)
    
name : zs
age : 24
hobby : ['basketball', 'music']

```

```python
# 获取字典的index和key数据
for i,k in enumerate(info_dict):
    print(i,";",k)

0 ; name
1 ; age
2 ; hobby

```

#### dict与json转换

- json.dumps()，将dict转为json
- json.loads()，将json转为dict

------

- json.dump()和json.load()，将转化的是文件对象

```python
import json
# dict转化为json
json_data = json.dumps(info_dict)
print(json_data)
print(type(json_data))

```

```
{"name": "zs", "age": 24, "hobby": ["basketball", "music"]}
<class 'str'>

```

```python
# json转为dict
dict_data = json.loads(json_data)
print(dict_data)
print(type(dict_data))

```

```
{'name': 'zs', 'age': 24, 'hobby': ['basketball', 'music']}
<class 'dict'>

```

### tuple()

元组，元组内的数据不能更改。函数的多个返回结果，是元组形式。

```python
t1 = ("hello","world")
print(t1[0])
print(t1[1])

```

```
hello
world

```

### set()

集合，无序不重复。空集合用set()创建

- 用集合对list数据去重
- 用集合的交集操作，查找多个list中相交的部分
- 用集合操作对list去重并排序

```python
list1 = [12,12,12,12,13,13,14,15]
list2 = [12,14,14,16,17,19]
print("列表去重：",set(list1))
print("列表并集：",set(list1)|set(list2))
print("列表交集：",set(list1)&set(list2))
print("列表去重排序：",sorted(list(set(list2)),reverse=True))

```

```
列表去重： {12, 13, 14, 15}
列表并集： {12, 13, 14, 15, 16, 17, 19}
列表交集： {12, 14}
列表去重排序： [19, 17, 16, 14, 12]

```

## 循环与条件空值

循环语句

- for..in...循环，经常作用于list,dict数据，还有与range()结合使用
- while循环，不怎么用，也不建议用，死循环就很尴尬啦，还是for...in...香  

条件语句

- if..else...
- if...elif....elif...else...

### 循环

for in 循环

```python
# for..in...
for v in ["你","好","世界","!"]:
    print(v)
```

```
你
好
世界
!
```

```python
# 打印1，3,5,7,9,11,13,15,17,19
list_ = [i for i in range(1,20,2)]
print(list_)

```

```
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

```

while循环

```python
# while
status = True
while status:
    input_str = input("输入q退出：")
    if input_str == 'q':
        print("退出")
        status = False

```

```
输入q退出：a
输入q退出：q
退出

```

### 条件控制

```python
age = int(input("年龄："))
sex = input("性别：")
if 0<age<=10:
    if age<=1:
        print("襁褓")
    elif age <=3:
        print("孩提")
    elif age==7and sex=="女":
        print("髫年")
    elif age==8 and sex=="男":
        print("龆年")
    else:
        print("总角")
elif 10<age<=15:
    if age==12 and sex=="女":
        print("金钗之年")
    elif age==12 and sex=="女":
        print("豆蔻年华")
    elif age==15 and sex=="女":
        print("及笄之年")
    elif age==15 and sex=="男":
        print("志学之年")
    else:
        print("舞勺之年")
elif 15<age<=20:
    if age==16 and sex=="女":
        print("破瓜年华、碧玉年华,二八年华")
    if age ==20 and sex=="女":
        print("桃李年华")
    if age ==20 and sex=="男":
        print("弱冠")
    else:
        print("舞象之年")
elif 20<age<50:
    if age==24 and sex=="女":
        print("花信年华")
    if age==30 and sex=="男":
        print("而立之年")
    if age==40 and sex=="男":
        print("不惑之年、强壮之年")
    if sex=="女":
        print("半老徐娘")
    else:
        print("春秋鼎盛")
elif 50<=age<60:
    print("年逾半百、知非之年、知命之年、艾服之年、大衍之年")
elif 60<=age<70:
    print("花甲、平头甲子、耳顺之年、杖乡之年、还历之年")
elif 70<=age<80:
    print("古稀、杖国之年、致事之年、致政之年，从心之年、悬车之年")
elif 80<=age<=100:
    if age<90:
        print("耄耋之年")
    if age==90:
        print("鲐背之年")
    else:
        print("期颐,又可称为“人瑞”")
else:
    print("没有对应的称谓")

```

```
年龄：24
性别：男
春秋鼎盛

```

