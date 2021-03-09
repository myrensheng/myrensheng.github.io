#!/usr/bin/env python
# coding: utf-8
import datetime
import warnings
import numpy as np
from pyecharts.charts import Line, Bar, Map, TreeMap, Page
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.options import ComponentTitleOpts
from pyecharts.components import Table
from pyecharts.globals import ThemeType, _WarningControl
from pyecharts.charts import Tab

_WarningControl.ShowWarning = False
warnings.filterwarnings("ignore")


# 自定义的远程地址，防止pyecharts默认的地址访问不到
# custom_host_list = [
#     "https://cdn.bootcss.com/echarts/4.8.0/",
#     "https://cdnjs.cloudflare.com/ajax/libs/echarts/4.8.0/"
# ]
# CurrentConfig.ONLINE_HOST = self.custom_host_list[0]


class ChartsAPI:
    def __init__(self):
        self.width = "1000px"
        self.height = "500px"
        self.theme = ThemeType.WHITE
        self.now = datetime.datetime.now()
        self.first = self.now.replace(day=1)
        self.last_month_day = (self.first - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        self.last_month = (self.first - datetime.timedelta(days=1)).strftime("%Y-%m")
        self.fk_time = "按照放款时间统计  截止时间：{}".format(self.last_month_day)
        self.jj_time = "按照进件时间统计  截止时间：{}".format(self.last_month_day)
        self.dk_time = "按照垫款时间统计  截止时间：{}".format(self.last_month_day)
        self.text = "内部数据 请勿泄露"

    def graphic_opts(self, right_n=50, bottom_n=50, width_n=200, height_n=18,
                     font_n='12px', is_show=True):
        if is_show is True:
            graphic_opts = [
                opts.GraphicGroup(
                    graphic_item=opts.GraphicItem(
                        rotation=JsCode("Math.PI / 4"),
                        bounding="raw",
                        right=right_n,
                        bottom=bottom_n,
                        z=100,
                    ),
                    children=[
                        opts.GraphicRect(
                            graphic_item=opts.GraphicItem(
                                left="center", top="center", z=100
                            ),
                            graphic_shape_opts=opts.GraphicShapeOpts(
                                width=width_n, height=height_n
                            ),
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                fill="rgba(0,0,0,0.3)"
                            ),
                        ),
                        opts.GraphicText(
                            graphic_item=opts.GraphicItem(
                                left="center", top="center", z=100
                            ),
                            graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                                text=self.text,
                                font="bold %s Microsoft YaHei" % font_n,
                                graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                    fill="#fff"
                                ),
                            ),
                        ),
                    ],
                )
            ]
        else:
            graphic_opts = None
        return graphic_opts

    def line_(self, data=None, x_name=None, y_names=None, y_rate=False, width="1000px", height="500px", title="折线图",
              subtitle="折线图", x_rotate=0, graphic=True):
        """
        绘制折线图
        :param graphic: 是否添加水印
        :param data: DataFrame数据
        :param x_name: x轴数据名称
        :param y_names: y轴数据名称，传入list可以绘制多条折线图
        :param y_rate: y值是否转为百分比显示，默认不转
        :param width: 图表宽度，默认1000px
        :param height: 图表高度，默认500px
        :param title: 图表标题，默认：柱状图
        :param subtitle: 图表副标题默，认：柱状图
        :param x_rotate: x轴旋转角度，默认为0
        :return: 图表对象
        """
        if None in [x_name, y_names, y_rate]:
            return None
        x = data[x_name].to_list()
        line = Line(
            init_opts=opts.InitOpts(width=width, height=height, theme=self.theme, bg_color="white")
        )
        line = line.add_xaxis(x)
        if isinstance(y_names, list):
            # 多个y值
            for i in y_names:
                if y_rate:
                    # 把y变成百分比
                    y = data[i].apply(lambda items: round(items * 100, 2)).to_list()
                    line = line.add_yaxis(i, y, label_opts=opts.LabelOpts(formatter='{@y}%', ),
                                          linestyle_opts=opts.LineStyleOpts(width=1.5), )
                else:
                    y = data[i].tolist()
                    line = line.add_yaxis(i, y, linestyle_opts=opts.LineStyleOpts(width=1.5), )
        elif isinstance(y_names, str):
            # 单个y值
            if y_rate:
                # 把y变成百分比显示
                y = data[y_names].apply(lambda items: round(items * 100, 2)).to_list()
                line = line.add_yaxis(y_names, y, label_opts=opts.LabelOpts(formatter='{@y}%', ),
                                      linestyle_opts=opts.LineStyleOpts(width=1.5), )
            else:
                y = data[y_names].tolist()
                line = line.add_yaxis(y_names, y, linestyle_opts=opts.LineStyleOpts(width=1.5), )
        line = line.set_global_opts(
            title_opts=opts.TitleOpts(title=title, subtitle=subtitle),
            toolbox_opts=opts.ToolboxOpts(),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=x_rotate)),
            legend_opts=opts.LegendOpts(orient="vertical", pos_right='1%', pos_top='10%'),
            datazoom_opts=[opts.DataZoomOpts(range_start=40, range_end=100), opts.DataZoomOpts(type_="inside")],
            graphic_opts=self.graphic_opts(is_show=graphic),
        )
        return line

    def bar_(self, data=None, x_name=None, y_names=None, y_rate=False, width="1000px", height="500px", title="柱状图",
             subtitle="柱状图", x_rotate=0, graphic=True):
        if None in [x_name, y_names, y_rate]:
            return None
        x = data[x_name].to_list()
        bar = Bar(
            init_opts=opts.InitOpts(width=width, height=height, theme=self.theme, bg_color="white")
        )
        bar = bar.add_xaxis(x)
        if isinstance(y_names, list):
            # 多个y值
            for i in y_names:
                y = data[i].tolist()
                bar = bar.add_yaxis(i, y)
        elif isinstance(y_names, str):
            y = data[y_names].tolist()
            bar = bar.add_yaxis(y_names, y)
        bar = bar.set_global_opts(
            title_opts=opts.TitleOpts(title=title, subtitle=subtitle),
            toolbox_opts=opts.ToolboxOpts(),
            # legend_opts=opts.LegendOpts(orient="vertical", pos_right='1%', pos_top='10%'),
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=x_rotate)),
            yaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            datazoom_opts=opts.DataZoomOpts(range_start=40, range_end=100,type_="inside"),
            graphic_opts=self.graphic_opts(is_show=graphic),
        )
        return bar

    def bar_line(self, data=None, x_name=None, bar_y_names=None, line_y_name=None,
                 line_y_rate=False, width="1000px", height="500px",
                 title="柱状图-折线图", subtitle="柱状图-折线图", x_rotate=0, graphic=True):
        x = data[x_name].tolist()
        # 柱形图
        bar = Bar(
            init_opts=opts.InitOpts(width=width, height=height, theme=self.theme, bg_color="white")
        )
        if isinstance(bar_y_names, list):
            # 多个y值
            for i in bar_y_names:
                y = data[i].tolist()
                bar = bar.add_yaxis(i, y, label_opts=opts.LabelOpts(is_show=False), )
        elif isinstance(bar_y_names, str):
            y = data[bar_y_names].tolist()
            bar = bar.add_yaxis(bar_y_names, y, label_opts=opts.LabelOpts(is_show=False), )
        bar = bar.extend_axis(
            yaxis=opts.AxisOpts(name=line_y_name, type_="value", axislabel_opts=opts.LabelOpts(formatter="{value}"), )
        )
        bar = bar.set_global_opts(
            title_opts=opts.TitleOpts(title=title, subtitle=subtitle),
            toolbox_opts=opts.ToolboxOpts(),
            # legend_opts=opts.LegendOpts(orient="vertical", pos_right='1%', pos_top='10%'),
            datazoom_opts=[opts.DataZoomOpts(range_start=40, range_end=100), opts.DataZoomOpts(type_="inside")],
            graphic_opts=self.graphic_opts(is_show=graphic),
            tooltip_opts=opts.TooltipOpts(
                is_show=True, trigger="axis", axis_pointer_type="cross"
            ),
            xaxis_opts=opts.AxisOpts(
                axislabel_opts=opts.LabelOpts(rotate=x_rotate),
                type_="category",
                axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
            ),
            yaxis_opts=opts.AxisOpts(
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )

        # 折线图
        line = Line()
        line = line.add_xaxis(x)
        if line_y_rate:
            y = data[line_y_name].apply(lambda items: round(items * 100, 2)).to_list()
            line = line.add_yaxis(series_name=line_y_name, yaxis_index=1, y_axis=y,
                                  label_opts=opts.LabelOpts(is_show=True, formatter='{@y}%'),
                                  )
        else:
            y = data[line_y_name].tolist()
            line = line.add_yaxis(series_name=line_y_name, yaxis_index=1, y_axis=y,
                                  label_opts=opts.LabelOpts(is_show=True))
        bar.overlap(line)
        return bar

    def table_(self, data, title="表格", subtitle_text="表格"):
        table = Table()
        columns = data.columns.tolist()
        rows = np.array(data).astype(object)
        table.add(columns, rows).set_global_opts(
            title_opts=ComponentTitleOpts(title=title, subtitle=subtitle_text)
        )
        return table

    def map_(self, data, name="地图", min_=0, max_=0, title="地图", subtitle_text="地图", graphic=True):
        c = Map()
        c = c.add(name, data, "china", is_roam=False, )
        c = c.set_global_opts(
            toolbox_opts=opts.ToolboxOpts(),
            title_opts=opts.TitleOpts(title=title, subtitle=subtitle_text),
            visualmap_opts=opts.VisualMapOpts(min_=min_, max_=max_, is_piecewise=True),
            graphic_opts=self.graphic_opts(is_show=graphic),
        )
        return c

    def treemap_(self, data, title="矩形树图", subtitle_text="矩形树图", width="1000px", height="500px", graphic=True):
        # 支持三层数据
        treemap = TreeMap(init_opts=opts.InitOpts(width=width, height=height))
        treemap.add(
            series_name=title,
            data=data,
            visual_min=300,
            leaf_depth=1,
            roam=False,
            # 标签居中为 position = "inside"
            label_opts=opts.LabelOpts(position="inside"),
            levels=[
                opts.TreeMapLevelsOpts(
                    treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                        border_color="#555", border_width=4, gap_width=4
                    )
                ),
                opts.TreeMapLevelsOpts(
                    color_saturation=[0.3, 0.6],
                    treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                        border_color_saturation=0.7, gap_width=2, border_width=2
                    ),
                ),
                opts.TreeMapLevelsOpts(
                    color_saturation=[0.3, 0.5],
                    treemap_itemstyle_opts=opts.TreeMapItemStyleOpts(
                        border_color_saturation=0.6, gap_width=1
                    ),
                ),
                opts.TreeMapLevelsOpts(color_saturation=[0.3, 0.5]),
            ],
        )
        treemap.set_global_opts(
            graphic_opts=self.graphic_opts(is_show=graphic),
            toolbox_opts=opts.ToolboxOpts(),
            legend_opts=opts.LegendOpts(is_show=False),
            title_opts=opts.TitleOpts(
                title=title, subtitle=subtitle_text, pos_left="leafDepth"
            ),
        )
        return treemap

    def compose(self, type_="tab", title=None, charts=None, tab_names=None):
        if type_ == "tab":
            tab = Tab()
            if tab_names is None:
                tab_names = ["图表" + str(i) for i in range(1, len(charts) + 1)]
            for i in zip(charts, tab_names):
                tab.add(i[0], i[1])

            return tab
        elif type_ == "page":
            if title is None:
                title = "图表汇总"
            page = Page(page_title=title, layout=Page.SimplePageLayout)
            for c in charts:
                page.add(c)
            return page
        else:
            return None
