import pandas as pd
import numpy as np
import random
import math

def square(min, max):  # 随机生成正方形
    a = random.randint(min, max)
    b = random.randint(min, max)
    return a, b


def triangle(min, max):  # 随即生成三角形
    a = random.randint(min, max)
    b = random.randint(min, max)
    c = random.randint(min, max)
    return a, b, c

def item_set(n, min, max):  # 生成物品集合
    item_list = []
    num = random.randint(0, n)
    for i in range(num):
        item_list.append(square(min, max))
    for j in range(n-num):
        item_list.append(triangle(min, max))
    item_list = [sorted(i) for i in item_list]
    return item_list



print(item_set(10, 1, 10))
