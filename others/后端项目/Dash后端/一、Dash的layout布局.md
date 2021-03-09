## Dash介绍

Dash官网教程地址：https://dash.plotly.com/introduction

数据分析工作的结果，通常是数据表格、图表，分析报告。这些东西office的三件套基本都能满足。

但是要将图表，报告，分析结果组合到一块就比较麻烦，而且自动化的成本较高，当数据更新时，操作更麻烦。

可以用Power BI、Tebleau、FineReport等，这些都是多数公司常用的工具。

我之所以选择Dash，主要是因为Dash是基于Flask开发的一套组件，对于python爱好者很友好，不需要太多的代码就能实现数据、图表的展示。也可以很方便的共享数据。

官网优秀案例地址：https://dash-gallery.plotly.host/Portal/

## 1、Dash安装

```shell
pip install dash==1.17.0
```

本篇介绍的是Dash官网关于布局的案例，案例地址：https://dash.plotly.com/layout

## 2、导包

```python
import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# 导入自定义的css样式
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]
```

dash包：用来实例化app的包

pandas：用来读取数据

dash_core_components：Dash自定义了一些前端框架，比如：下拉框，滑动条等一些交互组件

dash_html_components：dash用来构建前端基础代码标签，比如：Div，H1，Tr等前端标签

plotly：用来画图

## 3、实例化app

1、自定义的css样式在实例化的时候，传给external_stylesheets参数

```python
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
```

## 4、获取数据

1、Dash用的数据为DataFrame类型数据

2、用pandas作为读取数据工具，所以pandas支持的数据存储格式，都可以用来当做数据源

3、**当数据改变，网页对应的数据也会自动改变。**不需要重启应用

```python
df = pd.DataFrame(data={
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 3, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
```

## 5、画图

官网画图地址：https://plotly.com/python/

需要画什么图，就去官网的案例上找就行

```python
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
```

## 6、DataFrame转网页表格

```python
def generate_table(dataframe, max_rows=10):
    table_layout = html.Table(children=[
        # 表格头部信息
        html.Thead(children=html.Tr(children=[html.Th(col) for col in dataframe.columns])),
        # 表格数据信息
        html.Tbody(children=[
            html.Tr(children=[
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
    return table_layout
```

这个函数，可以将DataFrame类型数据转换为前端表格的形式，比如将上面的df数据装为网页表格的样子如下：

![dash_layout01](D:\learn\hello_python\数据与编程之美\后端项目\Dash后端\图片\dash_layout01.png)

## 7、布局

### 简单的页面布局

1、布局与前端HTML代码类似的树形结构

2、HTML标签的首字母大写

3、每一个标签都有id，children，style属性

4、将被嵌套的标签放到children中，如果有多个，就用放到list中

```python
app.layout = html.Div(
    children=[
        # H1标签
        html.H1(children="Hello Dash", style={'textAlign': 'center'}),
         # Div标签
        html.Div(children="Dash: A web application framework for Python", style={'textAlign': 'center'}),
        # 数据表格
        html.H4(children="原始数据"),
        html.Div(children=generate_table(df), style={'textAlign': 'center'}),
    ]
)
```

### 交互框布局

1、交互框位于dash_core_components包中

2、支持MarkDown语法，调用dcc.Markdown方法

3、有下拉框、单选框、复选框、输入框、文本框、滑动条等组件

```python
markdown_text = "### Dash支持Markdown语法。[MarkDown教程地址](http://commonmark.org/)"
app.layout = html.Div(
    children=[
        dcc.Markdown(children=markdown_text),
        html.Br(),
        html.H1(children="Dash内置的组件："),
        html.Label("下拉框（单选）："),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'},
            ],
            value='MTL',
        ),
        html.Label("下拉框（多选）："),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'},
            ],
            value=['MTL', 'SF'],
            multi=True,
        ),
        html.Label('单选框：'),
        dcc.RadioItems(options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'},
        ],
            value='MTL',
        ),
        html.Label("复选框："),
        dcc.Checklist(options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'},
        ],
            value=['MTL',"SF"]
        ),
        html.Label("输入框："),
        dcc.Input(value='MTL', type='text'),
        html.Label("文本框："),
        dcc.Textarea(),
        html.Label('滑动线：'),
        dcc.Slider(
            min=0,max=9,
            marks={i:'Label {}'.format(i) if i == 1 else str(i) for i in range(1,6)},
            value=5,
        )
    ]
)
```

### 图表布局

1、图表标签位于dash_core_components包中

2、将plotly绘制的图像对象传给figure参数

```python
app.layout = html.Div(
    children=[
        dcc.Graph(id='example-graph',figure=fig),
    ]
)
```

## 完整代码

```python
#!/usr/bin/env python
# coding: utf-8
import dash
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

# 官方案例地址：https://dash.plotly.com/layout
# 导入css样式
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# 实例化一个应用对象，类似于flask的操作
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# 构造数据
df = pd.DataFrame(data={
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 3, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})
# 画图，官网画图地址：https://plotly.com/python/
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


def generate_table(dataframe, max_rows=10):
    table_layout = html.Table(children=[
        # 表格头部信息
        html.Thead(children=html.Tr(children=[html.Th(col) for col in dataframe.columns])),
        # 表格数据信息
        html.Tbody(children=[
            html.Tr(children=[
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe), max_rows))
        ])
    ])
    return table_layout


markdown_text = "### Dash支持Markdown语法。[MarkDown教程地址](http://commonmark.org/)"
# 布局，用dash设计网页
# 每个标签都有id、children、style属性
# id为了定位到标签，children为了添加元素,style为了美化页面
app.layout = html.Div(
    children=[
        # H1标签
        html.H1(children="Hello Dash", style={'textAlign': 'center'}),
        # Div标签
        html.Div(children="Dash: A web application framework for Python", style={'textAlign': 'center'}),
        # 数据表格
        html.H4(children="原始数据"),
        html.Div(children=generate_table(df), style={'textAlign': 'center'}),
        # 绘图需要用到dash_core_components中的Graph组件，将图片对象传给figure参数
        dcc.Graph(id="example-graph", figure=fig),
        # 支持MarkDown语法
        dcc.Markdown(children=markdown_text),
        html.Br(),
        html.H1(children="Dash内置的组件："),
        html.Label("下拉框（单选）："),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'},
            ],
            value='MTL',
        ),
        html.Label("下拉框（多选）："),
        dcc.Dropdown(
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': u'Montréal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'},
            ],
            value=['MTL', 'SF'],
            multi=True,
        ),
        html.Label('单选框：'),
        dcc.RadioItems(options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'},
        ],
            value='MTL',
        ),
        html.Label("复选框："),
        dcc.Checklist(options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': u'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'},
        ],
            value=['MTL',"SF"]
        ),
        html.Label("输入框："),
        dcc.Input(value='MTL', type='text'),
        html.Label("文本框："),
        dcc.Textarea(),
        html.Label('滑动线：'),
        dcc.Slider(
            min=0,max=9,
            marks={i:'Label {}'.format(i) if i == 1 else str(i) for i in range(1,6)},
            value=5,
        )

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

```

![Dash](D:\learn\hello_python\数据与编程之美\后端项目\Dash后端\图片\dash_layout02.png)

