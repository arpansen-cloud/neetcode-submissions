class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #we can use a bfs algorithim that searches for islands horizontally layer by layer
        #a counter for islands, we will need set that holds on to land pieces that we already visited. We need to get the row and col variables and use them to iterate through the grid. 
        #check for where the grid is equal to 1 and check if it is not in our set() we can iniate the bfs algorithim. we can append islands after it runs through our algorithim. 
        #BFS: queue(first in, first out approach), add the r,c to our set() so we do not visit it again, append the r,c in our queue. and set up a loop that runs while there are values in our queue. To access the r,c and go through the grid we popleft from our queue and assign to a row, col value. We need a varibale that holds on to the different possible directions[right, left, top, and bottom] of that position. For dr , dc in directions we can add it to the row and col of the point we are currently on. We can check if that new point is in the range of our cols and rows and check if the position has not been visited and check if it is a piece of land. If true, we can add it to our queue so we can run bfs on it again and then we can add it to our set() so we dont visit it again. 
        if not grid:
            return 0
        rows , cols = len(grid), len(grid[0])
        islands = 0 
        visited = set()

        def bfs(r, c):
            q = deque()
            visited.add((r,c))
            q.append((r,c)) #storing it as a tuple because we need both row and col simutaneoulsy

            while q:

                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr , dc in directions:
                    r, c = row + dr , col + dc
                    if (r in range(rows) and c in range(cols)
                    and grid[r][c] == "1" and (r,c) not in visited):
                        q.append((r,c))
                        visited.add((r,c))

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r, c)

                    islands +=1 
        return islands

        