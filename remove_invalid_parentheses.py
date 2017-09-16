'''
http://www.geeksforgeeks.org/remove-invalid-parentheses/
https://discuss.leetcode.com/category/380/remove-invalid-parentheses
https://leetcode.com/problems/remove-invalid-parentheses/#/description
Remove Invalid Parentheses

An expression will be given which can contain open and close parentheses and optionally some characters, No other operator will be there in string. We need to remove minimum number of parentheses to make the input string valid. If more than one valid output are possible removing same number of parentheses then print all such output.
Examples:

Input  : str = ()())() -
Output : ()()() (())()
There are two possible solutions
"()()()" and "(())()"

Input  : str = (v)())()
Output : (v)()()  (v())()
'''
from collections import defaultdict
def isParentheses(ch):
    return ch == '(' or ch == ')'

def isValidString(s):
    cnt = 0
    for ch in s:
        if ch == '(':
            cnt += 1
        elif ch == ')':
            cnt -= 1
        if cnt < 0:
            return False
    return cnt == 0

def removeInvalidParenthese(s):
    if not s:
        return []

    visited = defaultdict()
    queue = []
    tmp = ""
    level = False
    res = []

    queue.append(s)
    visited[s] = True
    while queue:
        new_str = queue.pop(0)
        if isValidString(new_str):
            res.append(new_str)
            level = True

        if level:
            continue

        for i in xrange(len(new_str)):
            if not isParentheses(new_str[i]):
                continue

            tmp = new_str[:i] + new_str[i+1:]
            if tmp not in visited:
                queue.append(tmp)
                visited[tmp] = True

    return res

if __name__ == "__main__":
    print removeInvalidParenthese("()())()")
    print removeInvalidParenthese("(a)())()")
    print removeInvalidParenthese(")(")
