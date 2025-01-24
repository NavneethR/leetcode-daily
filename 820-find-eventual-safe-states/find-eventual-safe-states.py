from collections import deque

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        degreein = [0] * n
        rGraph = [[] for _ in range(n)]
        ans = []
        
        # Initialize reverse graph and in-degrees
        for u in range(n):
            for v in graph[u]:
                rGraph[v].append(u)
                degreein[u] += 1
        
        # Queue for nodes with no outgoing edges
        que = deque()
        for i in range(n):
            if degreein[i] == 0:
                que.append(i)
        
        # Perform topological sorting
        while que:
            u = que.popleft()
            ans.append(u)
            for v in rGraph[u]:
                degreein[v] -= 1
                if degreein[v] == 0:
                    que.append(v)
        
        # Return sorted result
        return sorted(ans)
