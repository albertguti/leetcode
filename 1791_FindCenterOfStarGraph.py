from typing import List
from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        maxlen = -1
        ans = -1
        for node in graph:
            print(maxlen, ans, node, len(graph[node]))
            if len(graph[node]) > maxlen:
                maxlen = len(graph[node])
                ans = node
                
        print(graph)
        return ans


obj = Solution()
obj.findCenter([[1,2],[2,3],[4,2]])