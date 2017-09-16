def numIslands(grid):
    if not grid:
        return 0

    count = 0
    for i in xrange(len(grid)):
        for j in xrange(len(grid[0])):
            if grid[i][j] == 1:
                dfs(grid,i,j)
                count += 1
    return count

def dfs(grid,i,j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
        return

    if grid[i][j] != 1:
        return

    grid[i][j] = -1
    dfs(grid,i+1,j)
    dfs(grid,i-1,j)
    dfs(grid,i,j+1)
    dfs(grid,i,j-1)

if __name__ == "__main__":
    graph = [[1, 1, 0, 0, 0],
            [0, 1, 0, 0, 1],
            [1, 0, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1]]

    print numIslands(graph)
