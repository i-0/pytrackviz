#! /usr/bin/env python2.7
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

# crack with gonzalo or without him =]

#def lost(graph):
    
#    dot_graph = [
#	[1, 10, 20, 30, 40, 50, 60, 70],
#	[1, 10, 20, 30, 41, 70],
#	[1, 10, 21, 211, 212, 30],
#	[1, 10, 21, 211, 213, 70],
#	[1 , 11],
#    ]

def dot2graph(dot_graph):
    node_edge_map = {} # {1:[10,11],10:[20,21],...}
    

    for i in dot_graph:
        for j in i:
            node = j
            edges =find_edges(j,i)
            assert(type(edges) == list)
            node_edge_map[node]=edges

    return node_edge_map

def find_edges(node, sub_graph):
    edges = []
    for i in sub_graph:
        if i == node:
            edges.append(follower(node,sub_graph))

    if None in edges:
        return [] # avoid returning [None] edges, TODO: find a more symetric way to handle those cases
    else:
        return edges

def follower(node, list):
    if list == []:
        return None
    elif not node in list:
        return None
    elif last(node, list):
        return None
    else:
        return list[list.index(node)+1]

def last(el, list):
    if list.index(el) + 1 >= len(list):
        return True
    else:
        return False

#if __name__ == main():
#    unittest.main()
#    #main()
#
