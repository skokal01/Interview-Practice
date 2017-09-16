'''
http://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/
Perfect Sum Problem (Print all subsets with given sum)
Given an array of integers and a sum, the task is to print all subsets of given array with sum equal to given sum.

Examples:

Input : arr[] = {2, 3, 5, 6, 8, 10}
        sum = 10
Output : 5 2 3
         2 8
         10

Input : arr[] = {1, 2, 3, 4, 5}
        sum = 10
Output : 4 3 2 1
         5 3 2
         5 4 1
'''
def dfs(arr,res,temp,start,target):
    if sum(temp) == target:
        res.append(temp[:])

    for i in xrange(start,len(arr)):
        dfs(arr,res,temp+[arr[i]],i+1,target)

def perfectSum(arr,target):
    res = []
    dfs(arr,res,[],0,target)
    return res

if __name__ == "__main__":
    print perfectSum([2,3,5,6,8,10],10)
    print perfectSum([1,2,3,4,5],10)
    print perfectSum([1,2,3,4,5],100)
