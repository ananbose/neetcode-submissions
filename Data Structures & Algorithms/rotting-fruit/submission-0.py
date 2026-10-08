class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append([i,j])
                if grid[i][j]==1:
                    fresh+=1
        cnt= -1
        if fresh == 0:
            return 0
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()

                dirs = [[0,1],[1,0],[-1,0],[0,-1]]
                for dx,dy in dirs:
                    nx,ny = i+dx, j+dy
                    print("nx,ny", nx, ny)
                    if 0<=nx<m and 0<=ny<n and grid[nx][ny]==1:
                        print("cominmg here")
                        grid[nx][ny] = 2
                        q.append([nx,ny])
                        fresh-=1
            cnt+=1
        if fresh == 0:
            return cnt
        
        return -1 