#!/usr/bin/env python
# coding: utf-8

# 可视化图表的属性
# 用Dash实现鼠标移动到图表上，改变其他图表的数据
"""
dash_core_components组件中的Graph方法，有四个属性：
1、hoverDate：鼠标悬停的数据集
2、clickDate：鼠标点击的数据集
3、selectedDate：图像中选择的数据集
4、relayoutDate：图像缩放的数据集
使用update_layout、update_traces方法实现图表的交互
"""
import dash
import dash_auth
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world'
}

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)
df = pd.read_csv('./csv/country_indicators.csv')
available_indicators = df["Indicator Name"].unique()
app.layout = html.Div([
    html.Div([
        # 下拉框，选择x轴名称
        html.Div([
            dcc.Dropdown(
                # id用来定位标签
                id='crossfilter-xaxis-column',
                # options选项，每一个选项都是一个字典
                options=[{'label': i, 'value': i} for i in available_indicators],
                # value默认值
                value='Fertility rate, total (births per woman)',
            ),
            # 圆形选项框
            dcc.RadioItems(
                id='crossfilter-xaxis-type',
                options=[{'label': i, 'value': i} for i in ['linear', 'log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            ),
        ], style={'width': '49%', 'display': 'inline-block'}),
        # 下拉框，选择y轴名称
        html.Div([
            dcc.Dropdown(
                # id用来定位标签
                id='crossfilter-yaxis-column',
                # options选项，每一个选项都是一个字典
                options=[{'label': i, 'value': i} for i in available_indicators],
                # value默认值
                value='Life expectancy at birth, total (years)',
            ),
            # 圆形选项框
            dcc.RadioItems(
                id='crossfilter-yaxis-type',
                options=[{'label': i, 'value': i} for i in ['linear', 'log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            ),
        ], style={'width': '49%', 'float': 'right', 'display': 'inline-block'}),
    ], style={'borderBottom': 'thin lightgrey solid', 'backgroundColor': 'rgb(250,250,250)', 'padding': '10px 5px'}),
    # 图像
    html.Div([
        # dcc.Graph图表对象
        dcc.Graph(
            # id定位图表
            id='crossfilter-indicator-scatter',
            # hoverDate鼠标悬停的数据，设置默认值
            hoverData={'points': [{'customdata': 'Japan'}]},
        )
    ], style={'width': '49%', 'display': 'inline-block', 'padding': '0 20'}),
    # 图像
    html.Div([
        dcc.Graph(id='x-time-series'),
        dcc.Graph(id='y-time-series'),
    ], style={'display': 'inline-block', 'width': '49%'}),
    # 滑动条
    html.Div(dcc.Slider(
        id='crossfilter-year-slider',
        min=df["Year"].min(),
        max=df["Year"].max(),
        value=df["Year"].max(),
        marks={str(year): str(year) for year in df["Year"].unique()},
        step=None,
    ), style={'width': '98%', 'padding': '0px 20px 20px 20px'})
])


# 这个回调函数用来监控x，y轴的名称及类别，滑动条的值，改变图表
@app.callback(
    Output('crossfilter-indicator-scatter', 'figure'),
    Input('crossfilter-xaxis-column', 'value'),
    Input('crossfilter-yaxis-column', 'value'),
    Input('crossfilter-xaxis-type', 'value'),
    Input('crossfilter-yaxis-type', 'value'),
    Input('crossfilter-year-slider', 'value'),
)
def update_graph(xaxis_column_name, yaxis_column_name, xaxis_type, yaxis_type, year_value):
    dff = df[df["Year"] == year_value]
    fig = px.scatter(
        x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
        y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
        # hover_name
        hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name']
    )
    fig.update_traces(customdata=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])
    fig.update_xaxes(title=xaxis_column_name, type='linear' if xaxis_type == 'linear' else 'log')
    fig.update_yaxes(title=yaxis_column_name, type='linear' if yaxis_type == 'linear' else 'log')
    fig.update_layout(margin={'l': 40, 'b': 40, 'r': 10, 't': 0}, hovermode='closest')
    return fig


def create_time_series(dff, axis_type, title):
    fig = px.scatter(dff, x='Year', y='Value')
    fig.update_traces(mode='lines+markers')
    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(type='linear' if axis_type == 'linear' else 'log')
    fig.add_annotation(x=0, y=0.85, xanchor='left', yanchor='bottom', xref='paper', yref='paper', showarrow=False,
                       align='left', bgcolor='rgba(255,255,255,0.5)', text=title)
    fig.update_layout(height=225, margin={'l': 20, 'b': 30, 'r': 10, 't': 10})
    return fig


@app.callback(
    dash.dependencies.Output('x-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
     dash.dependencies.Input('crossfilter-xaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-xaxis-type', 'value')])
def update_y_timeseries(hoverData, xaxis_column_name, axis_type):
    country_name = hoverData['points'][0]['customdata']
    dff = df[df['Country Name'] == country_name]
    dff = dff[dff['Indicator Name'] == xaxis_column_name]
    title = '<b>{}</b><br>{}'.format(country_name, xaxis_column_name)
    return create_time_series(dff, axis_type, title)


@app.callback(
    dash.dependencies.Output('y-time-series', 'figure'),
    [dash.dependencies.Input('crossfilter-indicator-scatter', 'hoverData'),
     dash.dependencies.Input('crossfilter-yaxis-column', 'value'),
     dash.dependencies.Input('crossfilter-yaxis-type', 'value')])
def update_x_timeseries(hoverData, yaxis_column_name, axis_type):
    dff = df[df['Country Name'] == hoverData['points'][0]['customdata']]
    dff = dff[dff['Indicator Name'] == yaxis_column_name]
    return create_time_series(dff, axis_type, yaxis_column_name)


if __name__ == '__main__':
    app.run_server(debug=True)
