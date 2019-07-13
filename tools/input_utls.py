# coding=utf8
# import dxfgrabber6
import pandas as pd

#
# def find_shape_from_dxf(file_name):
#     """
#     读取DXF文档，从LINE里面找出多边形
#     :param file_name: 文档路径
#     :return:
#     """
#     dxf = dxfgrabber.readfile(file_name)
#     all_shapes = list()
#     new_polygon = dict()
#     for e in dxf.entities:
#         if e.dxftype == 'LINE':
#             # print (e.start, e.end)
#             # 找封闭的多边形
#             # 线条不按顺序画
#             end_key = '{}x{}'.format(e.end[0], e.end[1])
#             star_key = '{}x{}'.format(e.start[0], e.start[1])
#             if new_polygon.has_key(end_key):
#                 # 找到闭合的多边形
#                 all_shapes.append(new_polygon[end_key])
#                 new_polygon.pop(end_key)
#                 continue
#
#             # 开始和结束点转换
#             if new_polygon.has_key(star_key):
#                 # 找到闭合的多边形
#                 all_shapes.append(new_polygon[star_key])
#                 new_polygon.pop(star_key)
#                 continue
#
#             # 找连接的点
#             has_find = False
#             for key, points in new_polygon.items():
#                 if points[-1][0] == e.start[0] and points[-1][1] == e.start[1]:
#                     new_polygon[key].append([e.end[0], e.end[1]])
#                     has_find = True
#                     break
#                 if points[-1][0] == e.end[0] and points[-1][1] == e.end[1]:
#                     new_polygon[key].append([e.start[0], e.start[1]])
#                     has_find = True
#                     break
#
#             if not has_find:
#                 new_polygon['{}x{}'.format(
#                     e.start[0], e.start[1])] = [[e.start[0], e.start[1]], [e.end[0], e.end[1]]]
#     return all_shapes
#
#
# def input_polygon(dxf_file):
#     """
#     :param dxf_file: 文件地址
#     :param is_class: 返回Polygon 类，或者通用的 list
#     :return:
#     """
#     # 从dxf文件中提取数据
#     datas = find_shape_from_dxf(dxf_file)
#     shapes = list()
#
#     for i in range(0, len(datas)):
#         shapes.append(datas[i])
#
#     return shapes
def rectangle(data, n=1):
    # 输入数据只有三个坐标点，当为矩形时要计算第四个点。先找到直角点(x1, y1)，然后用(x2+x3-x1, y2+y3-y1)得到第四个点的坐标。
    point_1 = [data['顶点1_X'] * n, data['顶点1_Y'] * n]
    point_2 = [data['顶点2_X'] * n, data['顶点2_Y'] * n]
    point_3 = [data['顶点3_X'] * n, data['顶点3_Y'] * n]
    shape_points = [point_1, point_2, point_3]
    line12 = (point_1[0] - point_2[0])**2 + (point_1[1] - point_2[1])**2
    line23 = (point_2[0] - point_3[0])**2 + (point_2[1] - point_3[1])**2
    line31 = (point_3[0] - point_1[0])**2 + (point_3[1] - point_1[1])**2
    if line12 + line23 == line31:
        right_angle = point_2
        other_1 = point_1
        other_2 = point_3
        shape_points = [point_1, point_2, point_3]
        shape_points.append([other_1[0] + other_2[0] - right_angle[0], other_1[1] + other_2[1] - right_angle[1]])
    if line23 + line31 == line12:
        right_angle = point_3
        other_1 = point_1
        other_2 = point_2
        shape_points = [point_2, point_3, point_1]
        shape_points.append([other_1[0] + other_2[0] - right_angle[0], other_1[1] + other_2[1] - right_angle[1]])
    if line31 + line12 == line23:
        right_angle = point_1
        other_1 = point_2
        other_2 = point_3
        shape_points = [point_3, point_1, point_2]
        shape_points.append([other_1[0] + other_2[0] - right_angle[0], other_1[1] + other_2[1] - right_angle[1]])
    return shape_points

def triangle(data, n=1):
    point_1 = [data['顶点1_X'] * n, data['顶点1_Y'] * n]
    point_2 = [data['顶点2_X'] * n, data['顶点2_Y'] * n]
    point_3 = [data['顶点3_X'] * n, data['顶点3_Y'] * n]
    shape_points = [point_1, point_2, point_3]
    return shape_points


def find_shape_from_csv(file_name, n):
    point_list = []
    datas = pd.read_csv(file_name, encoding='gbk')
    for index in datas.index:
        shape = datas.loc[index]
        if shape['物料代码'] == 0:
            number = shape['数量']
            for i in range(number):
                point_list.append(rectangle(shape, n))
        if shape['物料代码'] == 1:
            number = shape['数量']
            for i in range(number):
                point_list.append(triangle(shape, n))
    return point_list

def input_polygon(csv_file, n):
    data = find_shape_from_csv(csv_file, n)
    return data


if __name__ == '__main__':
    # s = reset_point('point_set.csv')
    s = input_polygon('point_set.csv')

    # s = find_shape_from_dxf('T2.dxf')
    print(s)
    print(len(s))

