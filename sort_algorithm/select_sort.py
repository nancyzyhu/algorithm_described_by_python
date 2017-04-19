# -*- coding: utf8 -*-
# 实现选择排序算法


def _find_smallest_item_in_list(item_list):
    """
    在item_list查找最小的元素
    :param item_list:
    :return:
    index of smallest item in item list
    """
    if not item_list or len(item_list) <= 0:
        return -1

    smallest_item = item_list[0]
    smallest_item_index = 0

    for index in range(1, len(item_list), 1):
        if smallest_item > item_list[index]:
            smallest_item_index = index
            smallest_item = item_list[index]

    return smallest_item_index


def select_sort(item_list):
    """
    使用选择排序算法，对item_list进行排序，从小到大排列
    :param item_list:
    :return:
    sorted list: from small to big
    """
    sorted_list = []

    needed_sorted_list = item_list[:]
    for i in range(len(needed_sorted_list)):
        smallest_item_index = _find_smallest_item_in_list(needed_sorted_list)
        sorted_list.append(needed_sorted_list.pop(smallest_item_index))

    return sorted_list


if __name__ == '__main__':
    item_list = [5, 4, 3, 2, 1, 9, 2, 4]
    print select_sort(item_list)
    print item_list
