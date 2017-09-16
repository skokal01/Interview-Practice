'''
http://www.geeksforgeeks.org/match-a-pattern-and-string-without-using-regular-expressions/
https://discuss.leetcode.com/topic/28340/python-backtracking-48ms/8
Match a pattern and String without using regular expressions
Given a string, find out if string follows a given pattern or not without using
any regular expressions.

Input:
string - GraphTreesGraph
pattern - aba
Output:
a->Graph
b->Trees

Input:
string - GeeksforGeeks
pattern - GG
Output:
No solution exists
'''
class Solution(object):
    def wordPatternMatch(self, pattern, str):
        dic = {}
        self.dfs(pattern, str, dic)
        return dic


    def dfs(self, pattern, str, dict):
        if len(pattern) == 0 and len(str) > 0:
            return False
        if len(pattern) == len(str) == 0:
            return True
        # abcde redblue
        # ^xxxx ^^^xxxx
        #   5       7
        # Try to match pattern `a` with at most 3 characters.
        # That is 7 - 5 + 1, and the last + 1 is for Python range.
        for end in range(1, len(str)-len(pattern)+2): # +2 because it is the "end of an end"
            if pattern[0] not in dict and str[:end] not in dict.values():
                dict[pattern[0]] = str[:end]
                if self.dfs(pattern[1:], str[end:], dict):
                    return True
                del dict[pattern[0]]
            elif pattern[0] in dict and dict[pattern[0]] == str[:end]:
                if self.dfs(pattern[1:], str[end:], dict):
                    return True
        return False

if __name__ == "__main__":
    obj = Solution()
    print obj.wordPatternMatch("ABBA","redbluebluered")
    print obj.wordPatternMatch("aba", "GeeksForGeeks")
    print obj.wordPatternMatch("GG", "CatDogCat")
