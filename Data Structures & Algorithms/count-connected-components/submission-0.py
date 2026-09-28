class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        q = deque()
        if n ==1:
            return 1
        graph = {}
        for i, j in edges:
            if i in graph:
                graph[i].append(j)
            else:
                graph[i] = [j]
            if j in graph:
                graph[j].append(i)
            else:
                graph[j] = [i]
        print("graph", graph)
        visited = set()
        cnt =0
        for i in range(n):
            if i in visited:
                continue
            q.append(i)
            print("appending i", i)
            cnt+=1
            while(q):
                node=q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for comp in graph.get(node,[]):
                    q.append(comp)
        return cnt
