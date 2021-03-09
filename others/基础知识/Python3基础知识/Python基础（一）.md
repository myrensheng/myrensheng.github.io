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

### int
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

### float
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

### str
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


```python
# 字符串切片
a = "你是我的太阳"
```


```python
# 取前两个字符
a[:2]
```


    '你是'


```python
# 取最后两个字符
a[-2:]
```


    '太阳'


```python
# 取中间的字符串
a[2:4]
```


    '我的'


```python
# format()，字符串内用{0}表示填充format()中的第一个字符串
"你是我的{0}".format("太阳")
```


    '你是我的太阳'


```python
# replace()，替换字符串中的内容
"你是我的太阳".replace("太阳","月亮")
```


    '你是我的月亮'


```python
# find()，查看字符中是否包含某个字符串，返回包含字符串的索引位置，不包含的时候返回-1
"你是我的太阳".find("太阳")
```


    4


```python
"你是我的太阳".find("月亮")
```


    -1


```python
# endswith()
a.endswith("太阳")
```


    True


```python
a.endswith("月亮")
```


    False


```python
# strip()
"你是我的太阳  ".strip()
```


    '你是我的太阳'


```python
# decode()
"你是我的太阳".encode("utf-8")
```


    b'\xe4\xbd\xa0\xe6\x98\xaf\xe6\x88\x91\xe7\x9a\x84\xe5\xa4\xaa\xe9\x98\xb3'


```python
# encode()
b'\xe4\xbd\xa0\xe6\x98\xaf\xe6\x88\x91\xe7\x9a\x84\xe5\xa4\xaa\xe9\x98\xb3'.decode("utf-8")
```


    '你是我的太阳'


```python
# count()
"aabbccdd".count("a")
```


    2


```python
# 字符串类型的数字，转为int或者float类型
int("2")
```


    2


```python
float("2.0")
```


    2.0


