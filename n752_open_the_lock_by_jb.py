"""
bfs solution
"""
"""
deadend = ["0201","0101","0102","1212","2002"],    target = "0002"        q = [ (0900,1)..... (8000, 2)]

             0                  0                    0                 0
           /    \             /   \               /    \             /   \
    9000         1000      0900    0100       0090     0010       0009    0001        step = 1
       /\         /\       /\       /\         /\        /\        /\        /\
    8000 0000 0000 2000 0800 0000 0000 0200 0000 0080 0000 0020 0000 0008 0000 0002   step = 2    
""" 
class Solution:
    def __init__(self):
        self.__start = '0000'
        self.__step = 0
        self.__code_len = 4
    
    def openLock(self, deadends: List[str], target: str) -> int:
        
        if target == self.__start: return 0
        if self.__start in deadends: return -1
        
        return self.bfs(deadends, target)
    
    def bfs(self, deadends, target):
        
        queue = collections.deque()
        queue.append((self.__start, self.__step))
        seen = set(self.__start)
        
        while queue:
            code, step = queue.popleft()
            
            if code in deadends:
                continue
            if code == target:
                return step
            
            for i in range(self.__code_len):
                num = int(code[i])
                
                for dx in [-1, 1]:
                    update_code = code[:i] + str((num + dx) % 10) + code[i + 1:]
                    if update_code not in seen:
                        queue.append((update_code, step + 1))
                        seen.add(update_code)                        
        return -1
"""
dfs solution
"""

