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
        dcc.Input(id='num-multi', type='number', value=5),
        html.Table([
            html.Tr([html.Td(['x', html.Sup(2)]), html.Td(id='square')]),
            html.Tr([html.Td(['x', html.Sup(3)]), html.Td(id='cube')]),
            html.Tr([html.Td([2, html.Sup("x")]), html.Td(id='twos')]),
            html.Tr([html.Td([3, html.Sup("x")]), html.Td(id='threes')]),
            html.Tr([html.Td(['x', html.Sup("x")]), html.Td(id='x^x')]),
        ]),
        # 当提交之后才改变数据
        dcc.Input(id='input-1-state', type='text', value="hello"),
        dcc.Input(id='input-2-state', type='text', value='world'),
        html.Button(id='submit-button-state', n_clicks=0, children='Submit'),
        html.Div(id='output-state')
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
