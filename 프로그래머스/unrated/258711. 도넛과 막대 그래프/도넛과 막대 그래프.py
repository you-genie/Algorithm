
class Node:
    def __init__(self):
        self.parents = list()
        self.children = list()
    def __repr__(self):
        return f"parent: {self.parents}, children: {self.children}"
    
def solution(edges):
    graph_dict = {}
    
    for src, dst in edges:
        src_node = graph_dict[src] if src in graph_dict else Node()
        src_node.children.append(dst)
        graph_dict[src] = src_node
        
        dst_node = graph_dict[dst] if dst in graph_dict else Node()
        dst_node.parents.append(src)
        graph_dict[dst] = dst_node

    center = None
    for key in graph_dict:
        if len(graph_dict[key].children) >= 2 and not graph_dict[key].parents:
            center = key

    graph_roots = graph_dict[center].children
    for root in graph_roots:
        graph_dict[root].parents.remove(center)
    del graph_dict[center]
        
    len_total = len(graph_roots)
    line, eight = 0, 0
            
    for node in graph_dict.values():
        if not node.children:
            line += 1
        elif len(node.parents) == 2:
            eight += 1

    donut = len_total - line - eight
    return center, donut, line, eight