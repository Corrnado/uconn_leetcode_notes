"""
["hot","dot","dog","lot","log","cog"]                q = [ cog], seen = (hot, dot, lot,dog,log, cog) 

beginWord = "hit", endWord = "cog"                  word = log,     res = [dog, lot, cog ]
                        
                        hit
                        /
                      hot 
                     /  \
                   dot  lot  
                   /      \
                 dog       log
                 / 
                cog
                
sq = [  log]     sseen = (hit, hot, dot, lot, dog, log)                word =  dog,    res = []
eq = [dog, log]          eseen = (cog, dog, log)

                                 hit                           cog
                                 /                             / \
                               hot                        dog       log
                             /    \                        
                         dot         lot                
                            \        
                           dog    
"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if endWord not in wordList: return 0
        
        return self.bfs(beginWord, endWord, set(wordList))
    
    def bfs(self, beginWord, endWord, wordList):
        
        STEP = 1
        start_queue = collections.deque([beginWord])
        end_queue = collections.deque([endWord])
        start_seen = set([beginWord])
        end_seen = set([endWord])
        
        while start_queue and end_queue:
            
            if len(start_queue) > len(end_queue):
                start_queue, end_queue = end_queue, start_queue
                start_seen, end_seen = end_seen, start_seen
            
            for _ in range(len(start_queue)):
                word = start_queue.popleft()
                if word in end_seen:
                    return STEP
                
                for wrd in self._get_all_word(word, wordList):
                    if wrd not in start_seen:
                        start_seen.add(wrd)
                        start_queue.append(wrd)
            STEP += 1
        return 0
    
    def _get_all_word(self, word, wordList):
        word_list = []
        
        for i, char in enumerate(word):
            for l in 'abcdefghijklmnopqrstuvwxyz':
                if char != l:
                    temp = word[: i] + l + word[i + 1:]
                    if temp in wordList:
                        word_list.append(temp)
        return word_list
        
