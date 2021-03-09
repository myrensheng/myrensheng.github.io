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
    "Amount": [4, 4, 2, 3, 4, 5],
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
