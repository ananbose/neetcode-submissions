class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # SO we need to track cycles, hw do we do that in BST ?? 
        # So 1 has 2,4 , 2 has 1,3 but 3 gets back to 1 so there is a cycle 
        q = deque()
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
        if n==1:
            return True
        q.append([0,-1])
        visited = set()
        while  q:
            node,parent = q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for g in graph.get(node,[]):
                if g == parent:
                    continue
                q.append([g,node])
        if len(visited)!=n:
            return False
        return True


                
