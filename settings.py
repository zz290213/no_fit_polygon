# -*- coding: utf-8 -*-

POPULATION_SIZE = 10  # 基因组数
MUTA_RATE = 20        # 变异概率
ROTATIONS = 4    # 旋转选择， 1： 不能旋转
# 单位都是MM(毫米)
SPACING = 0     # 图形间隔空间
# 不同面料尺寸
BIN_HEIGHT = 1000
BIN_WIDTH = 2000
BIN_NORMAL = [[0, 0], [0, BIN_HEIGHT], [BIN_WIDTH, BIN_HEIGHT], [BIN_WIDTH, 0]]        # 一般布是无限长
BIN_CUT_BIG = [[0, 0], [0, 1570], [2500, 1570], [2500, 0]]       # 切割机尺寸 1
BIN_CUT_SMALL = [[0, 0], [0, 1200], [1500, 1200], [1500, 0]]     # # 切割机尺寸 2
#
# 增加重心目标函数
# 优化算法