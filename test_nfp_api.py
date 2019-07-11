# -*- coding: utf-8 -*-
from nfp_function import Nester, content_loop_rate, set_target_loop
from tools import input_utls
from settings import BIN_WIDTH, BIN_NORMAL, BIN_CUT_BIG


if __name__ == '__main__':
    n = Nester()
    # s = input_utls.input_polygon('./T9.dxf')  # 读取数据 多边形各个端点的xy坐标
    # s = [[[1, 1], [2, 1], [1, 2], [2, 2]], [[3, 1], [3, 2], [4, 1], [4, 2]]]
    s = [[[100, 200], [100, 100], [200, 100], [200, 200]], [[100, 200], [100, 100], [200, 100], [200, 200]]]
    # s = [[[1, 2], [1, 1], [2, 1], [2, 2]], [[5, 2], [4, 6], [3, 4]]]

    # s = [[[136.9936081807218, 998.9169826996906], [136.9936081807216, 54.57371176989091], [1825.691430368993, 54.57371176989091], [1825.691430368993, 998.9169826996906]], [[1978.085632549847, 240.4232012368257], [2052.85203853564, 81.04629519616445], [2322.011097849328, 114.249818284944], [2235.614361174293, 240.4232012368257]], [[2438.314399153845, 129.1914031431747], [2398.43897964787, 252.0444327227383], [2430.0070200901, 270.3063709532871], [2554.617694870451, 178.9966851177437]]]
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
    set_target_loop(best, n)
    # content_loop_rate(best, n, loop_time=5)   # T7 , T4



