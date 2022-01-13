import heapq
class Solution:
    """
    @param maze: the maze
    @param ball: the ball position
    @param hole: the hole position
    @return: the lexicographically smallest way
    """
    def findShortestWay(self, maze, ball, hole):
        # write your code here
        return self.bfs(maze, ball, hole)

    def bfs(self, maze, ball, hole):
        m, n = len(maze), len(maze[0])
        queue = [(0, '', ball[0], ball[1])]
        seen = set()

        DIRECTION = [[0, 1, 'r'], [1, 0, 'd'], [-1, 0, 'u'], [0, -1, 'l']]

        while queue:
            step, path, x, y  = heapq.heappop(queue)

            if hole[0] == x and hole[1] == y:
                    return path 

            if (x, y) not in seen:
                seen.add((x, y))                 

                for dx, dy, ds in DIRECTION:
                    nx, ny = x, y
    #               1    4
                    newStep = step
 
                    while m > nx >= 0 and n > ny >= 0 and maze[nx][ny] != 1 and not (hole[0] == nx and hole[1] == ny):
                        nx += dx   
                        ny += dy                     
                        newStep += 1   

                    if nx != hole[0] or ny != hole[1]:
                        newStep -=1
                        nx -= dx
                        ny -= dy
                   
                    p = path

                    if nx != x or ny != y:
                        p += ds

                    heapq.heappush(queue, (newStep, p, nx, ny))   
        return 'impossible'


"""                 右下上zuo
 [0,0,0,0,0],                  q = []     start = [4,3]   end [0,1]          path =                       step =     
 [1,1,0,0,1],                  seen = ((0, 4), (0,3), (1,3), (1,4),(1,0),(2,0),(2,2),(4,2))
 [0,0,0,0,0],
 [0,1,0,0,1],                 ul     lul
 [0,1,0,s,0]
                                                 x,y,step, path
                                                (0,4,0,'')                          
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
