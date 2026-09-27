class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m = len(heights)
        n = len(heights[0])
        qa=deque()
        qp = deque()
        va = set()
        vp=set()
        def bfs(q, visited):

            while q:
                x,y = q.popleft()
                dir = [[0,1],[1,0],[0,-1],[-1,0]]
                for dx,dy in dir:
                    nx,ny = x+dx , y+dy
                    if 0<=nx<m and 0<=ny<n and heights[nx][ny]>=heights[x][y] and (nx,ny) not in visited:
                        q.append([nx,ny])
                        visited.add((nx,ny))
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    qp.append([i,j])
                    vp.add((i,j))
                if i == m-1 or j == n-1:
                    qa.append([i,j])
                    va.add((i,j))

        bfs(qp,vp)
        bfs(qa,va)
        return [list(cell) for cell in vp & va]

            
        
                    
                    
                
