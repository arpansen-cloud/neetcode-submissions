class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #an optimal way to do this is to start from the parts of the grid that is equal to a tresure chest and iterate out to see the distances from each land cell to the tresure chest. 
        #we can use a breath first search algorithim for this, we also need 2 data structures (queue and a set). The queue will store the current coord that we are iterating from and the set will hold coords that we have already seen 
        #we can check the adjacent coords for the current layer we are at for bfs. and then we can run breath for search on the adjacent coordinates and add to the distance for those coordinates if they are a land piece. For this we can use a helper function and check for if the adjacent coords are out of bounds and if they are not in the set and if they are equal to land and

        rows , cols = len(grid), len(grid[0])

        q = deque()
        visit = set()

        def addValue(r, c):
            if (r == rows or r < 0 or c < 0 or c == cols or grid[r][c] == -1 
            or (r,c) in visit):
                return 
            visit.add((r,c))
            q.append([r,c])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c))
        dist = 0
        while q: 

            for i in range(len(q)):
                
                r, c = q.popleft()
                grid[r][c] = dist
                addValue(r+1,c) 
                addValue(r-1,c) 
                addValue(r,c+1) 
                addValue(r,c-1) 
            dist  +=1 

                

        