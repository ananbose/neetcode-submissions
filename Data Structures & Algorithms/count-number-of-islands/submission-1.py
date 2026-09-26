class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        cnt = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    q.append([i,j])
                    grid[i][j] = "0"
                    cnt+=1
                    while q:
                        i,j=q.popleft()
                        dir = [[0,1],[1,0],[0,-1],[-1,0]]
                        for dx,dy in dir:
                            x,y=i+dx,j+dy
                            if 0<=x<m and 0<=y<n and grid[x][y]=="1":
                                grid[x][y] = "0"
                                q.append([x,y])
        return cnt

