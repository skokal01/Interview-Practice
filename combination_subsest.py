'''
https://leetcode.com/problems/subsets/#/description
https://discuss.leetcode.com/topic/46159/a-general-approach-to-backtracking-questions-in-java-subsets-permutations-combination-sum-palindrome-partitioning
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
def backtrack(arr,res,temp,start):
    res.append(temp[:])
    for i in xrange(start,len(arr)):
        temp.append(arr[i])
        backtrack(arr,res,temp,i+1)
        temp.pop()

def subsets(arr):
    res = []
    backtrack(sorted(arr),res,[],0)
    return res

def backtrack_no_duplicates(arr,res,temp,start):
    res.append(temp[:])
    for i in xrange(start,len(arr)):
        if i > start and arr[i] == arr[i-1]:
            continue
        temp.append(arr[i])
        backtrack_no_duplicates(arr,res,temp,i+1)
        temp.pop()

def subsets_no_duplicates(arr):
    res = []
    backtrack_no_duplicates(sorted(arr),res,[],0)
    return res

def dfs(arr,res,path,start):
    res.append(path)
    for i in xrange(start,len(arr)):
        if i > start and arr[i] == arr[i-1]:
            continue
        dfs(arr,res,path+[arr[i]],i+1)

def susbsets_dfs_no_dups(arr):
    res = []
    dfs(arr,res,[],0)
    return res
if __name__ == "__main__":
    print subsets([1,2,3])
    print subsets([1,2,2])
    print subsets_no_duplicates([1,2,3])
    print subsets_no_duplicates([1,2,2])
    print susbsets_dfs_no_dups([1,2,3])
    print susbsets_dfs_no_dups([1,2,2])
