# -*- coding: utf-8 -*-
from nfp_function import Nester, content_loop_rate, set_target_loop
from tools import input_utls
from settings import BIN_WIDTH, BIN_NORMAL, BIN_CUT_BIG


if __name__ == '__main__':
    n = Nester()
    s = input_utls.input_polygon('./E6.dxf')  # 读取数据 多边形各个端点的xy坐标
    n.add_objects(s)

    if n.shapes_max_length > BIN_WIDTH:  # 判断物品总面积和画布宽度的关系，允许增加画布
        BIN_NORMAL[2][0] = n.shapes_max_length
        BIN_NORMAL[3][0] = n.shapes_max_length

    # 选择面布
    n.add_container(BIN_NORMAL)  # 加入画布数据和画布包络矩阵
    # 运行计算
    n.run()

    # 设计退出条件
    res_list = list()
    best = n.best
    # 放置在一个容器里面
    # set_target_loop(best, n)    # T6

    # 循环特定次数
    # set_target_loop(best, n)
    content_loop_rate(best, n, loop_time=5)   # T7 , T4



