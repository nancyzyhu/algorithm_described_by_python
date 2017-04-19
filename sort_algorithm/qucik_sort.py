# -*- coding: utf8 -*-
# 实现快速排序算法


def quick_sort(item_list):
    """
    使用快速排序算法，对item_list进行排序，从小到大排序
    :param item_list:
    :return:
    """
    if not item_list or len(item_list) < 2:
        return item_list

    item_base = item_list[0]
    less_than_item_list = [item for item in item_list[1:] if item <= item_base]
    greater_than_item_list = [item for item in item_list[1:] if item > item_base]

    return quick_sort(less_than_item_list) + [item_base] + quick_sort(greater_than_item_list)


if __name__ == '__main__':
    item_list = [1, 6, 5, 9, 3, 7, 11]
    print quick_sort(item_list)
