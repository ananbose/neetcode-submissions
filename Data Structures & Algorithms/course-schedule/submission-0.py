class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        indegree = [0]*numCourses
        for i,j in prerequisites:
            indegree[i]+=1
            if j in graph:
                graph[j].append(i)
            else:
                graph[j]=[i]
        q = deque()
        for index, i in enumerate(indegree):
            if i == 0:
                q.append(index)
        c =0
        while q:
            course = q.popleft()
            c+=1
            for d in graph.get(course,[]):
                indegree[d]-=1
                if indegree[d]==0:
                    q.append(d)
        return c==numCourses
                
            