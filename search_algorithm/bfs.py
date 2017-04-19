# -*- coding: utf8 -*-
# 实现广度优先搜索算法

import collections


# 定义一个图
graph = dict()
graph['me'] = ['hello', 'world', 'sking']
graph['hello'] = ['sk', 's4']
graph['s4'] = ['sk']
graph['sk'] = []
graph['world'] = ['s2']
graph['s2'] = []
graph['sking'] = ['s3']
graph['s3'] = []


def is_finish_search(vertex):
    # 判断当前搜索顶点是否为终点
    # 这里判断终点的条件可以自定义
    if vertex == 's2':
        return True

    return False


def bsf(vertex, graph):
    """
    实现广度优先搜索算法
    :param vertex: 起始顶点
    :param graph: 搜索
    :return:
    """
    search_vertexes = collections.deque()
    search_vertexes += [vertex]
    searched_path = []

    while len(search_vertexes) > 0:
        search_vertex = search_vertexes.popleft()

        if search_vertex not in searched_path:
            if is_finish_search(search_vertex):
                searched_path.append(search_vertex)
                break
            else:
                search_vertexes += graph[search_vertex]
                searched_path.append(search_vertex)

    print '->'.join(searched_path)


if __name__ == '__main__':
    bsf('me', graph)
