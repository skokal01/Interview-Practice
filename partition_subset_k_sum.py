#http://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/
'''
Partition of a set into K subsets with equal sum
Given an integer array of N elements, the task is to divide this array into K non-empty subsets such that the sum of elements in every subset is same. All elements of this array should be part of exactly one partition.
Examples:

Input : arr = [2, 1, 4, 5, 6], K = 3
Output : Yes
we can divide above array into 3 parts with equal
sum as [[2, 4], [1, 5], [6]]

Input  : arr = [2, 1, 5, 5, 6], K = 3
Output : No
It is not possible to divide above array into 3
parts with equal sum
'''
class Solution(object):
    def __init__(self):
        pass

    def dfs(self,arr,res,path,start):
        if sum(path) == self.subset:
            res.append(path[:])

        for i in xrange(start,len(arr)):
            self.dfs(arr,res,path+[arr[i]],i+1)

    def doKPartitions(self,arr,k):
        if k == 1:
            return True
        if k > len(arr) or sum(arr) % k != 0:
            return False

        subset = sum(arr)/k
        subsetSums = [0]*k

        self.subset = subset

        res = []
        self.dfs(arr,res,[],0)
        return res

if __name__ == "__main__":
    obj = Solution()
    print obj.doKPartitions([2, 1, 4, 5, 6],3)
    print obj.doKPartitions([2, 1, 5, 5, 6],3)
