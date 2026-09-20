class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #the most efficent way of go through the grid would be recursively using a dfs algorithim
        #we can use a hashset so we dont visit the same coordinate more than once
        #within the dfs func we can set up a base case that checks for if the row value is < 0 or row == range of rows and if col < 0 or cols == range of cols or if (r,c) is in hashset, or if the coord in the grid is equal to a water piece, return 0 
        #else we add our r, c to our hashset 
        #return the area = 1 + dfs(directions)
        #we can then initiate our area variable and then loop through the rows and cols and find the max area by running the coords that we loop through into our dfs function. 

        rows, cols = len(grid), len(grid[0])

        visited = set()
                        
        def dfs(r,c):
            if (r < 0 or r == rows or c < 0 or c == cols or (r,c) in visited or grid[r][c] == 0):
                return 0
            
            visited.add((r,c))
            return (1 + dfs(r + 1, c) + dfs(r -1, c) + dfs(r,c+1)+ dfs(r, c-1))

        area = 0

        for r in range(rows):
            for c in range(cols):

                area = max(area, dfs(r,c))
        return area
        

        