
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
            def dfs(i,j,k,visited):
                if k ==len(word):
                    return True
                if not (0<=i<m and 0<=j<n):
                    return False
                if board[i][j] != word[k]:
                    return False
                if (i,j) in visited:
                    return False
                visited.add((i,j))
                dirs = [[0,1],[1,0],[-1,0],[0,-1]]
                for dx,dy in dirs:
                    nx,ny = i+dx, j+dy
                    if dfs(nx,ny,k+1,visited):
                        return True
                visited.remove((i,j))
                return False     
                

            m = len(board)
            n = len(board[0])
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        visited = set()
                        if dfs(i,j,0,visited):
                            return True
            return False
