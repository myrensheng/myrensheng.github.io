#!/usr/bin/env python
# coding: utf-8

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
    return [{'label': i, "value": i} for i in all_options[selected_country]], all_options[selected_country][0]


@app.callback(
    Output('display-selected-values', 'children'),
    Input('countries-radio', 'value'),
    Input('cities-radio', 'value'),
)
def set_display_children(selected_country, selected_city):
    return u"{} is a city in {}".format(selected_city, selected_country)


if __name__ == '__main__':
    app.run_server(debug=True)
