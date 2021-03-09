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
