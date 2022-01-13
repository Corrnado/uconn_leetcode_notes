"""
not done yet,
"""

import heapq
class Solution:
    """
    @param maps: 
    @return: nothing
    """
    def theMazeIV(self, maps):

        for i in range(len(maps)):
            for j in range(len(maps[0])):
                if maps[i][j] == 'S':
                    return self.bfs(maps, [i, j])
        return -1

    def bfs(self, maps, start):
        m, n = len(maps), len(maps[0])
        queue = [(0, start[0], start[1])]
        seen = set()

        DIRECTION = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        MINSTEP = sys.maxsize


        while queue:
            step, x, y  = heapq.heappop(queue)
            seen.add((x, y))

            if maps[x][y] == "T":
                return step
            for dx, dy in DIRECTION:
                nx, ny = dx + x, dy + y
#               1    4
                newStep = 0
                if m > nx >= 0 and n > ny >= 0 and maps[nx][ny] != '#':
                    newStep += 1   # 2
     
                    newStep = step + newStep    # 2
                    heapq.heappush(queue, (newStep, nx, ny))

        return -1
