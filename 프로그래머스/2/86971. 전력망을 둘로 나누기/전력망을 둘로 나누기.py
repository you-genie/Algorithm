from typing import Tuple, List
from collections import defaultdict
import sys

def solution(n, wires):
    def to_dict(wires: List) -> dict:
        wire_dict = defaultdict(list)
        
        for src, dst in wires:
            wire_dict[src].append(dst)
            wire_dict[dst].append(src)
        
        return wire_dict
    
    def traverse(wires: dict) -> Tuple[List, List]:
        keys = list(range(1, n+1))
        visited = []
        
        def _traverse(root, tree):
            if root in keys:
                keys.remove(root)
                visited.append(root)

                if root in tree:
                    for c in tree[root]:
                        _traverse(c, tree)
                    
            return

            
        root = list(wires.keys())[0]
        _traverse(root, wires)        
        
        return keys, visited
    
    min_delta = sys.maxsize
    for i in range(len(wires)):
        keys, visited = traverse(to_dict(wires[:i]+wires[i+1:]))
        min_delta = min(min_delta, abs(len(keys)-len(visited)))
        
    return min_delta