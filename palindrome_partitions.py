'''
https://leetcode.com/problems/subsets/#/solutions
https://leetcode.com/problems/palindrome-partitioning/
https://discuss.leetcode.com/topic/6186/java-backtracking-solution
http://www.geeksforgeeks.org/print-palindromic-partitions-string/
https://discuss.leetcode.com/topic/33425/python-recursive-iterative-backtracking-solution/2
Print all palindromic partitions of a string
Given a string s, partition s such that every string of the partition is a palindrome. Return all possible palindrome partitioning of s.

Example :

Input  : s = "bcc"
Output : [["b", "c", "c"], ["b", "cc"]]

Input  : s = "geeks"
Output : [["g", "e", "e", "k", "s"],
          ["g", "ee", "k", "s"]]
'''
def isPalindrome(s):
    return s == s[::-1]
def dfs(s,path,res):
    if not s:
        res.append(path)
    for i in xrange(1,len(s)+1):
        if isPalindrome(s[:i]):
            dfs(s[i:],path+[s[:i]],res)

def partition(s):
    res = []
    dfs(s,[],res)
    return res

def palindromePartitionsUtil(res,temp,s,start):
    if start == len(s):
        res.append(temp[:])
    else:
        for i in xrange(start+1, len(s)+1):
            if isPalindrome(s[start:i]):
                temp.append(s[start:i])
                palindromePartitionsUtil(res,temp,s,i)
                temp.pop()
def palindromePartitions(s):

    # Will call the helper code
    res = []
    palindromePartitionsUtil(res,[],s,0)
    return res

if __name__ == "__main__":
    print palindromePartitions("geeks")
    print palindromePartitions("aab")
    print palindromePartitions("bcc")
    print partition("geeks")
    print partition("aab")
    print partition("bcc")
