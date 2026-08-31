import heapq
import collections
class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        frontier=[(0,k)]
        visited=set()
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        while frontier:
            time, node =heapq.heappop(frontier)
            if node in visited:
                continue
            visited.add(node)
            if len(visited)==n:
                return time

            for neighbor, weight in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(frontier,(time+weight, neighbor))
        return -1



    
        