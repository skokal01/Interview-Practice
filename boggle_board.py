'''
http://www.geeksforgeeks.org/boggle-find-possible-words-board-characters/
https://leetcode.com/problems/word-search/#/description
https://leetcode.com/problems/word-search/#/description
Boggle (Find all possible words in a board of characters) | Set 1
Given a dictionary, a method to do lookup in dictionary and a M x N board where every cell has one character. Find all possible words that can be formed by a sequence of adjacent characters. Note that we can move to any of 8 adjacent characters, but a word should not have multiple instances of same cell.

Example:

Input: dictionary[] = {"GEEKS", "FOR", "QUIZ", "GO"};
       boggle[][]   = {{'G','I','Z'},
                       {'U','E','K'},
                       {'Q','S','E'}};
      isWord(str): returns true if str is present in dictionary
                   else false.

Output:  Following words of dictionary are present
         GEEKS
         QUIZ

'''
dictionary = ["GEEKS", "FOR", "QUIZ", "GO", "SEEK"]
def findWordsHelper(board,visited,i,j,res,str):
    global dictionary
    visited[i][j] = 1
    str += board[i][j]

    if str in dictionary and str not in res:
        res.append(str)

    # These two for loops are for 8 neighbors
    for r in xrange(max(i-1,0),min(i+2,len(board))):
        for c in xrange(max(j-1,0),min(j+2,len(board[0]))):
            if not visited[r][c]:
                findWordsHelper(board,visited,r,c,res,str)

    str = str[:-1]
    visited[i][j] = 0

def findWords(board):
    visited = [[0]*len(board[0]) for i in xrange(len(board))]

    res = []
    for i in xrange(len(board)):
        for j in xrange(len(board[0])):
            findWordsHelper(board,visited,i,j,res,"")
    return res

if __name__ == "__main__":
    board = [['G','I','Z'],['U','E','K'],['Q','S','E']]
    print findWords(board)
