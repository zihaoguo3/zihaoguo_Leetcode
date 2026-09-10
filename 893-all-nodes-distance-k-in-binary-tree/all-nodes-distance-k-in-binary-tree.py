# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        queue=deque([root])
        parent={}
        while queue:
            node=queue.popleft()
            if node.right:
                parent[node.right]=node
                queue.append(node.right)
            
            if node.left:
                parent[node.left]=node
                queue.append(node.left)

        visited={target}
        queue=deque([target])
        dist=0

        while queue:
            if dist==k:
                return [node.val for node in queue]

            for _ in range(len(queue)):
                curr=queue.popleft()
                for node in (curr.left, curr.right, parent.get(curr)):
                    if node and node not in visited:
                        visited.add(node)
                        queue.append(node)
            dist+=1
        return []




        