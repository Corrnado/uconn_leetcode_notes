import heapq
class Solution:
    """
    @param maze: the maze
    @param start: the start
    @param destination: the destination
    @return: the shortest distance for the ball to stop at the destination
    """
    def shortestDistance(self, maze, start, destination):
        # write your code here
        return self.bfs(maze, start, destination)

    def bfs(self, maze, start, destination):
        m, n = len(maze), len(maze[0])
        queue = [(0, start[0], start[1])]
        seen = set()

        DIRECTION = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        MINSTEP = sys.maxsize


        while queue:
            step, x, y  = heapq.heappop(queue)
            seen.add((x, y))

            if destination[0] == x and destination[1] == y:
                return step
            for dx, dy in DIRECTION:
                nx, ny = dx + x, dy + y
#               1    4
                newStep = 0
                while m > nx >= 0 and n > ny >= 0 and maze[nx][ny] != 1:
                    nx += dx   # 3
                    ny += dy   # 4
                    newStep += 1   # 2
     
                nx -= dx   # 2
                ny -= dy   # 4
                newStep = step + newStep    # 2

                if maze[nx][ny] == 0 and (nx, ny) not in seen:
                    heapq.heappush(queue, (newStep, nx, ny))

        return -1


"""
 [0,0,1,x,s],                  q = []        end [3,2]
 [x,0,0,x,x],                  seen = ((0, 4), (0,3), (1,3), (1,4),(1,0),(2,0),(2,2),(4,2))
 [x,0,x,1,x],
 [1,1,e,1,1],
 [x,0,x,0,x]
                                                 x,y,step
                                                (0,4,0)                          
                                        /                \
                                      (0,3,1)              (2,4,2)            
                                        /                   e
                                    (1,3,2)  
                                    /   \
                                (1,4,3)   (1,0,5) 
                                e        / \
                                    (2,0,6)  
                                    /
                                 (2,2,8)
                                 /
                              (4,2,10)
                              /   \
                           (4,0,12)  (4,4,12)
""" 
