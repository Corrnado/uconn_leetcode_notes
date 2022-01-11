"""
solution for bfs
"""

class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    
    #corner case
    if not grid or not grid[0]: return 0
    
    # lengh and width of a 2D matix
    m, n = len(grid), len(grid[0])
    island_count = 0
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == '1':
          self.bfs(grid, i, j)
          island_count += 1
     return island_count
  
  def bfs(self, grid, x, y):
    
    # direction to move, order: right, left, up, down
    DIRECTION = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    queue = collections.deque([(x, y)])
    grid[x][y] = '0'
    
    while queue:
      qx, qy = queue.popleft()
      for dx, dy in DIRECTION:
        nx, ny = qx + dx, qy + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
          grid[nx][ny] = '0':
            queue.append((nx, ny))
            
            
  """
  solution for dfs
  """          
 class Solution:
  def numIslands(self, grid: List[List[str]]) -> int:
    #corner case
    if not grid or not grid[0]: return 0
    
    # lengh and width of a 2D matix
    m, n = len(grid), len(grid[0])
    island_count = 0
    
    for i in range(m):
      for j in range(n):
        if grid[i][j] == '1':
          self.dfs(grid, i, j)
          island_count += 1
     return island_count
  
   def dfs(self, grid, x, y):
      
      # return condition
      if grid[x][y] == '0': return
      if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]): return
      
      #mark the location is been visted
      grid[x][y] = '0'
      DIRECTION = [[0, 1], [0, -1], [1, 0], [-1, 0]]
      for dx, dy in DIRECTION:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '1':
          self.dfs(grid, nx, ny)
      
    
