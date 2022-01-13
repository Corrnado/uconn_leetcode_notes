"""
 [0,0,1,x,s],                  q = []        end [3,2]
 [x,0,0,x,x],                  seen = ((0, 4), (0,3), (1,3), (1,4),(1,0),(2,0),(2,2),(4,2))
 [x,0,x,1,x],
 [1,1,e,1,1],
 [x,0,x,0,x]
 
                                                (0,4)
                                        /                \
                                      (0,3)              (2,4)
                                        /                   e
                                    (1,3)  
                                    /   \
                                (1,4)   (1,0) 
                                e        / \
                                    (2,0)  
                                    /
                                 (2,2)
                                 /
                              (4,2)
                              /   \
                           (4,0)  (0,4)
""" 
"""
below is bfs solution
"""
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: whether the ball could stop at the destination
    """
    def hasPath(self, maze, start, destination):
        # write your code here
        return self.bfs(maze, start, destination)

    def bfs(self, maze, start, destination):

        m, n = len(maze), len(maze[0])
        seen = set()
        queue = collections.deque([(tuple(start))])

        DIRECTION = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while queue:
            x, y = queue.popleft()
            seen.add((x, y))
            if x == destination[0] and y == destination[1]:
                return True
            for dx, dy in DIRECTION:
                nx = dx + x
                ny = dy + y

                while m > nx >= 0 and n > ny >= 0 and maze[nx][ny] != 1:
                    nx += dx
                    ny += dy
                nx -= dx
                ny -= dy

                if maze[nx][ny] == 0 and (nx, ny) not in seen:
                    queue.append((nx, ny))
        return False
