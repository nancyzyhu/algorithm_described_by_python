# -*- coding: utf8 -*-
# 实现dijkstra算法


# 定义一个图
graph_dict = dict()
graph_dict['a'] = {'b': 2, 'c': 5}
graph_dict['b'] = {'c': 8, 'd': 7}
graph_dict['c'] = {'d': 2, 'e': 4}
graph_dict['d'] = {'f': 1}
graph_dict['e'] = {'d': 6, 'f': 3}
graph_dict['f'] = {}

# graph_dict['a'] = {'b': 10}
# graph_dict['b'] = {'d': 20}
# graph_dict['c'] = {'b': 1}
# graph_dict['d'] = {'c': 1, 'e': 30}
# graph_dict['e'] = {}

# graph_dict['a'] = {'b': 2, 'c': 2}
# graph_dict['b'] = {'c': 2}
# graph_dict['c'] = {'d': 2, 'e': 2}
# graph_dict['d'] = {'b': 1, 'e': 2}
# graph_dict['e'] = {}

max_weight = float('inf')


def _create_costs_dict(from_vertex, graph_dict):
    """
    生成起点到其他顶点的最短路径
    :param from_vertex:
    :param graph_dict:
    :return:
    {'vertex': cost}
    """
    costs_dict = {}
    for vertex in graph_dict:
        if vertex != from_vertex:
            costs_dict[vertex] = graph_dict[from_vertex].get(vertex, max_weight)
    return costs_dict


def _get_parent_for_vertex(vertex, graph_dict):
    """
    寻找顶点的父顶点
    :param vertex:
    :param graph_dict:
    :return:
    """
    for parent_vertex in graph_dict:
        if vertex in graph_dict[parent_vertex]:
            return parent_vertex

    return None


def _create_parent_dict(from_vertex, graph_dict):
    """
    生成起点到其他顶点路径中：其他顶点的父顶点
    :param from_vertex:
    :param graph_dict:
    :return:
    {'vertex': parent vertex}
    """
    parent_dict = {}
    for vertex in graph_dict:
        if vertex != from_vertex:
            parent_dict[vertex] = _get_parent_for_vertex(vertex, graph_dict)
    return parent_dict


def find_min_cost_vertex(costs_dict, process_vertexes):
    """
    获取当前路径（加权）最短且没有被处理过的顶点
    :param costs_dict:
    :param process_vertexes:
    :return:
    """
    min_path = max_weight
    min_path_vertex = None
    for vertex in costs_dict:
        if vertex not in process_vertexes:
            if min_path > costs_dict[vertex]:
                min_path = costs_dict[vertex]
                min_path_vertex = vertex

    return min_path_vertex


def dijkstra(from_vertex, to_vertex, graph_dict):
    """
    计算从起点到终点的最短路径（加权路径）
    :param from_vertex:
    :param to_vertex:
    :param graph_dict:
    :return:
    """
    costs_dict = _create_costs_dict(from_vertex, graph_dict)
    parent_dict = _create_parent_dict(from_vertex, graph_dict)
    process_vertexes = []

    min_path_vertex = find_min_cost_vertex(costs_dict, process_vertexes)
    parent_dict[min_path_vertex] = from_vertex
    while min_path_vertex:
        min_path = costs_dict[min_path_vertex]
        neighbor_vertexes = graph_dict[min_path_vertex].keys()
        for vertex in neighbor_vertexes:
            if min_path + graph_dict[min_path_vertex][vertex] < costs_dict[vertex]:
                costs_dict[vertex] = min_path + graph_dict[min_path_vertex][vertex]
                parent_dict[vertex] = min_path_vertex
        process_vertexes.append(min_path_vertex)
        min_path_vertex = find_min_cost_vertex(costs_dict, process_vertexes)
    print 'min path: %.1f' % costs_dict[to_vertex]

    # 打印最短路径（加权）
    min_path_vertexes = [to_vertex]
    temp_vertex = to_vertex
    while parent_dict[temp_vertex] != from_vertex:
        min_path_vertexes.append(parent_dict[temp_vertex])
        temp_vertex = parent_dict[temp_vertex]
    min_path_vertexes.append(from_vertex)
    min_path_vertexes.reverse()
    print ' -> '.join(min_path_vertexes)

if __name__ == '__main__':
    dijkstra('a', 'e', graph_dict)
