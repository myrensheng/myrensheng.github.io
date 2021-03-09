案例官方地址：https://dash.plotly.com/basic-callbacks

Dash中的回调函数:根据app的输入信息，自动调用该函数，主要用到dash.dependcies中的Input和Output方法。

## 导包

```python
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
```

## 初始化app

```python
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.read_csv('./csv/gapminder.csv')
```

为了提升加载速度，我把官网的数据下载到本地。

## 简单的布局

```python
app.layout = html.Div([
    html.H6("改变输入值，观察回调函数的返回情况"),
    html.Div(
        ["输入：",
         dcc.Input(id='my-input', value='initial value', type='text')
         ]
    ),
    html.Br(),
    html.Div(id="my-output"),
    # 滑动不同的值，改变图表
    html.Br(),
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=int(df["year"].min()),
        max=int(df["year"].max()),
        value=int(df["year"].min()),
        marks={str(year): str(year) for year in df["year"].unique()},
        step=None,
    )
])
```

1、注意dash_core_components中的Input与dash.dependencies中的Input的区别：前者用在回调函数中进行数据传输，后者用在构造页面布局中的输入标签。

2、**为标签加上id属性，可以在回调函数中接受输入的数据，也可以将回调函数的输出显示在对应的位置。**

页面呈现的效果如下：

![dash_callback01](D:\learn\hello_python\数据与编程之美\后端项目\Dash后端\图片\dash_callback01.png)

改变输入的值，输出的值也会对应改变。改变滑条的位置，散点图会发生改变。

## 回调函数

### 一个输入对应一个输出

```python
# 回调函数，当app的输入改变，自动调用该函数，返回改变的值
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_val(input_value):
    return "输出：{}".format(input_value)
```

1、@app.callback()，回调函数的装饰器，需要传入Output()和Input()参数。

2、Output()第一个参数为对应组件id，也就是网页标签的id；第二个参数为组件的属性，children表示，将返回的结果嵌套到对应id标签里面。

3、Input()第一个参数也是网页标签对应的id；第二个参数为标签对应的属性，value表示将返回的结果当做该标签的value值。

4、回调函数update_output_val，第一个参数input_value对应就是网页标签id为my-input的value值。

```python
@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value')
)
def update_figure(selected_year):
    filtered_df = df[df["year"] == selected_year]
    fig = px.scatter(
        filtered_df,
        x='gdpPercap',
        y='lifeExp',
        size='pop',
        color='continent',
        hover_name='country',
        log_x=True,
        size_max=55
    )
    # transition_duration，过渡时间
    fig.update_layout(transition_duration=500)
    return fig
```

1、回调函数可以有多个，只要改变对应id的值，就会自动调用对应的回调函数

### 完整代码

```python
#!/usr/bin/env python
# coding: utf-8
# Dash中的回调函数:根据app的输入信息，自动调用该函数

import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# 自己构造数据
df = pd.read_csv('./csv/gapminder.csv')

# 简单的布局
app.layout = html.Div([
    html.H6("改变输入值，观察回调函数的返回情况"),
    html.Div(
        ["输入：",
         dcc.Input(id='my-input', value='initial value', type='text')
         ]
    ),
    html.Br(),
    html.Div(id="my-output"),
    # 滑动不同的值，改变图表
    html.Br(),
    dcc.Graph(id='graph-with-slider'),
    dcc.Slider(
        id='year-slider',
        min=int(df["year"].min()),
        max=int(df["year"].max()),
        value=int(df["year"].min()),
        marks={str(year): str(year) for year in df["year"].unique()},
        step=None,
    )
])


# 回调函数，当app的输入改变，自动调用该函数，返回改变的值
@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_val(input_value):
    return "输出：{}".format(input_value)


@app.callback(
    Output('graph-with-slider', 'figure'),
    Input('year-slider', 'value')
)
def update_figure(selected_year):
    filtered_df = df[df["year"] == selected_year]
    fig = px.scatter(
        filtered_df,
        x='gdpPercap',
        y='lifeExp',
        size='pop',
        color='continent',
        hover_name='country',
        log_x=True,
        size_max=55
    )
    # transition_duration，过渡时间
    fig.update_layout(transition_duration=500)
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
```

### 多个输入对应一个输出

1、callback()中的Input顺序要与回调函数中的参数顺序保持一致

2、该案例有5个输入值，1个输出值，改变任意一个值，散点图都会改变

3、改变散点图的布局用update_layout(margin,hovermode)，改变坐标轴的横纵坐标用update_xaxis(title,type),update_yaxis(title,type)

```python
#!/usr/bin/env python
# coding: utf-8
# 选择不同的x，y轴，对应图表发生改变
# 多个输入，一个输出

import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('./csv/country_indicators.csv')

available_indicators = df['Indicator Name'].unique()

app.layout = html.Div([
    html.Div([
        # x轴选项设置
        html.Div([
            dcc.Dropdown(id='xaxis-column',
                         options=[{"label": i, "value": i} for i in available_indicators],
                         value="Fertility rate, total (births per woman)",
                         ),
            dcc.RadioItems(id="xaxis-type",
                           options=[{"label": i, "value": i} for i in ["Linear", "Log"]],
                           value="Linear",
                           labelStyle={'display': 'inline-block'}
                           )
        ],
            style={"width": "48%", "display": "inline-block"}
        ),
        # y轴选项设置
        html.Div([
            dcc.Dropdown(id='yaxis-column',
                         options=[{"label": i, "value": i} for i in available_indicators],
                         value="Life expectancy at birth, total (years)",
                         ),
            dcc.RadioItems(id="yaxis-type",
                           options=[{"label": i, "value": i} for i in ["Linear", "Log"]],
                           value="Linear",
                           labelStyle={'display': 'inline-block'}
                           )
        ],
            style={"width": "48%", "float": "right", "display": "inline-block"}
        ),
    ]),
    dcc.Graph(id="indicator-graphic"),
    dcc.Slider(
        id='year-slider',
        min=df["Year"].min(),
        max=df["Year"].max(),
        value=df["Year"].max(),
        marks={str(year): str(year) for year in df['Year'].unique()},
        step=None,
    )
])


@app.callback(
    Output('indicator-graphic', 'figure'),
    Input('xaxis-column', 'value'),
    Input('yaxis-column', 'value'),
    Input('xaxis-type', 'value'),
    Input('yaxis-type', 'value'),
    Input('year-slider', 'value'),
)
def update_graph(xaxis_column_name,yaxis_column_name,xaxis_type,yaxis_type,year_value):
    dff = df[df["Year"]==year_value]
    fig = px.scatter(
        x=dff[dff["Indicator Name"] == xaxis_column_name]["Value"],
        y=dff[dff["Indicator Name"] == yaxis_column_name]["Value"],
        hover_name=dff[dff["Indicator Name"] == yaxis_column_name]["Country Name"]
    )
    fig.update_layout(margin={'l':40,'b':40,'t':10,'r':0},hovermode='closest')
    fig.update_xaxes(title=xaxis_column_name,type='linear' if xaxis_type=='Linear' else 'log')
    fig.update_yaxes(title=yaxis_column_name,type='linear' if xaxis_type=='Linear' else 'log')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
```

启动效果如下：

![dash_callback02](D:\learn\hello_python\数据与编程之美\后端项目\Dash后端\图片\dash_callback02.png)

### 一个输入对应多个输出

1、回调函数callback_x的return顺序与app.callback()中的Output()顺序一致

```python
#!/usr/bin/env python
# coding: utf-8

# 一个输入对应多个输出
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        dcc.Input(id='num-multi', type='number', value=5),
        html.Table([
            html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
            html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
            html.Tr([html.Td([2, html.Sup("x")]), html.Td(id='twos')]),
            html.Tr([html.Td([3, html.Sup("x")]), html.Td(id='threes')]),
            html.Tr([html.Td(['x', html.Sup("x")]), html.Td(id='x^x')]),
        ])
    ]
)


@app.callback(Output('square', 'children'),
              Output('cube', 'children'),
              Output('twos', 'children'),
              Output('threes', 'children'),
              Output('x^x', 'children'),
              Input('num-multi', 'value'),
              )
def callback_x(x):
    if x:
        return x ** 2, x ** 3, 2 ** x, 3 ** x, x ** x
    else:
        return '', '', '', '', ''


if __name__ == '__main__':
    app.run_server(debug=True)
```

运行结果如下：

![dash_callback03](D:\learn\hello_python\数据与编程之美\后端项目\Dash后端\图片\dash_callback03.png)

## State代替Input

**上面的例子中，当输入值改变后，输出的值也会改变。但有的时候，我们需要等输入完成，点击提交之后才改变数据。这时就要用到State代替Input**

```python
#!/usr/bin/env python
# coding: utf-8

# 一个输入对应多个输出
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        # 当提交之后才改变数据
        dcc.Input(id='input-1-state', type='text', value="hello"),
        dcc.Input(id='input-2-state', type='text', value='world'),
        html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
        html.Div(id='output-state')
    ]
)

@app.callback(Output('output-state', 'children'),
              Input('submit-button-state', 'n_clicks'),
              State('input-1-state', 'value'),
              State('input-2-state', 'value'),
              )
def update_output(n_clicks, input1, input2):
    out_str = "the button has been pressed {} time,Input 1 is '{}' and input 2 is '{}'".format(n_clicks, input1, input2)
    return out_str


if __name__ == '__main__':
    app.run_server(debug=True)
```

效果如下：

![dash_callback04](D:\learn\hello_python\数据与编程之美\后端项目\Dash后端\图片\dash_callback04.png)

只有点击submit按钮之后，下面的文字才会改变

## 回调函数之间的联动

第一个回调函数的输出值，是第二个回调函数的输入值，可以用来制作省份城市之间的联动框。第一个选择对应的省份，第二款为去城市。

```python
# 链式调用，类似于省份，城市选择联动
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

all_options = {
    "American": ["new york", "san francisco", "cincinnati"],
     'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}
app.layout = html.Div([
    dcc.RadioItems(id='countries-radio',
                   options=[{'label': k, 'value': k} for k in all_options.keys()],
                   value="American",
                   ),
    html.Br(),
    dcc.RadioItems(id='cities-radio'),
    html.Hr(),
    html.Div(id='display-selected-values'),
])


@app.callback(
    Output('cities-radio', 'options'),
    Output('cities-radio', 'value'),
    Input('countries-radio', 'value'),
)
def set_cities_options(selected_country):
    # 根据选择的国家，返回对应的城市
    return [{'label': i, "value": i} for i in all_options[selected_country]],all_options[selected_country][0]


@app.callback(
    Output('display-selected-values','children'),
    Input('countries-radio','value'),
    Input('cities-radio','value'),
)
def set_display_children(selected_country,selected_city):
    return u"{} is a city in {}".format(selected_city,selected_country)


if __name__ == '__main__':
    app.run_server(debug=True)
```

效果如下：

![dash_callback05](D:\learn\hello_python\数据与编程之美\后端项目\Dash后端\图片\dash_callback05.png)

