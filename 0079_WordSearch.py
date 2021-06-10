"""
79. Word Search
Medium

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Example 3:

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

"""

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        result = False
        for r in range(rows):
            for c in range(cols):
                result |= self.searchWord(board, word, set(), 0, r, c)
                if result:
                    return True
        return result

    def searchWord(self, board, word, visited, index, r, c):
        rows = len(board)
        cols = len(board[0])
        if index == len(word):
            return True
        result = False
        if 0 <= r < rows and 0 <= c < cols and (r,c) not in visited and board[r][c] == word[index]:
            result |= self.searchWord(board, word, visited|{(r,c)}, index+1, r, c+1)
            result |= self.searchWord(board, word, visited|{(r,c)}, index+1, r, c-1)
            result |= self.searchWord(board, word, visited|{(r,c)}, index+1, r-1, c)
            result |= self.searchWord(board, word, visited|{(r,c)}, index+1, r+1, c)
        return result
            
obj = Solution()
#board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
#word = "SEE"
word = "ABCB"
res = obj.exist(board, word)
print(res)