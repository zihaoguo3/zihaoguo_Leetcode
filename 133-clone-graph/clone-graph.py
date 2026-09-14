"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        clone_node={node:Node(node.val)}
        queue=deque([node])

        while queue:
            curr=queue.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in clone_node:
                    clone_node[neighbor]=Node(neighbor.val)
                    queue.append(neighbor)
                clone_node[curr].neighbors.append(clone_node[neighbor])
        return clone_node[node]
        

        
        