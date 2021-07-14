"""
127. Word Ladder
Hard

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

    Every adjacent pair of words differs by a single letter.
    Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
    sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

 

Constraints:

    1 <= beginWord.length <= 10
    endWord.length == beginWord.length
    1 <= wordList.length <= 5000
    wordList[i].length == beginWord.length
    beginWord, endWord, and wordList[i] consist of lowercase English letters.
    beginWord != endWord
    All the words in wordList are unique.
"""

from typing import List
from collections import defaultdict,deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord not in wordList:
            wordList.append(beginWord)
        graph = self.buildGraph(wordList)
        ans = self.bfsGetDistance(graph, beginWord, endWord)    
        return ans 
        
    def bfsGetDistance(self, graph, beginWord, endWord):
        visited = set()
        queue = deque([(beginWord,1)])
        while queue:
            word, steps = queue.popleft()
            if word not in visited:
                visited.add(word)
                if word == endWord:
                    return steps
                
                for i in range(len(word)):
                    key = word[:i]+"-"+word[i+1:]
                    neighbours = graph.get(key, [])
                    for neighbour in neighbours:
                        if neighbour not in visited:
                            queue.append((neighbour, steps+1))
        return 0
    
    
    def buildGraph(self,wordList: List[str]):
        graph = defaultdict(list)
        
        for word in wordList:
            for i,char in enumerate(word):
                key = word[:i]+"-"+word[i+1:]
                graph[key].append(word)
        return graph
    
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

obj = Solution()
result = obj.ladderLength(beginWord, endWord, wordList)
print(result)