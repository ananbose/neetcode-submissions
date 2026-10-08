class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # shortest path first algorithm , you add the first 0,0 to the queue , and if there is another 0 add it to the queue till you reach the destination , but you need to keep the shortest distance as the main result , so can you keep visited ?? you need to keep vistd or yio will 
        q = deque()
        m = len(grid)
        n = len(grid[0])
        if grid[0][0]!=0 or grid[m-1][n-1]!=0:
            return -1
        q.append([0,0,1])
        dirs = [[0,1], [1,0], [-1,0], [0,-1],[1,1], [-1,-1], [1,-1], [-1,1]]
        while q:
            i,j, dist = q.popleft()
            if i == m-1 and j == n-1:
                return dist
            for x,y in dirs:
                dx, dy = i+x, j+y
                if 0<=dx<m and 0<=dy<n and grid[dx][dy]==0:
                    grid[dx][dy]=1
                    q.append([dx,dy, dist+1])
        return -1