'''
http://www.geeksforgeeks.org/word-break-problem-using-backtracking/
Word Break Problem using Backtracking
Given a valid sentence without any spaces between the words and a dictionary of valid English words, find all possible ways to break the sentence in individual dictionary words.

Example

Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input: "ilikesamsungmobile"
Output: i like sam sung mobile
        i like samsung mobile

Input: "ilikeicecreamandmango"
Output: i like ice cream and man go
        i like ice cream and mango
        i like icecream and man go
        i like icecream and mango
'''
dic = ['i','like','samsung','sam','sung','mobile','ice','cream','icecream','and','man','go','mango']
def dfs(s,res,path):
    for i in xrange(1,len(s)+1):
        if s[:i] in dic:
            if i == len(s):
                # import pdb
                # pdb.set_trace()
                path += s[:i]
                res.append(path[:])
                return
            dfs(s[i:],res,path+s[:i]+" ")

def wordBreak(s):
    res = []
    dfs(s,res,"")
    return res

if __name__ == "__main__":
    print wordBreak("ilikeicecreamandmango")
    print wordBreak("ilikesamsungmobile")
