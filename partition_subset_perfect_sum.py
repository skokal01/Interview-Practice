#http://www.geeksforgeeks.org/perfect-sum-problem-print-subsets-given-sum/
'''
Perfect Sum Problem (Print all subsets with given sum)
Given an array of integers and a sum, the task is to print all subsets
of given array with sum equal to given sum.

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
def isSubSetSum(arr,n,sum):
    def isSubSetSumUtil(arr,res,n,sum):
        if sum != 0 and n == 0:
            if res:
                del res[:]
            return
        if sum == 0:
            return res

        res.append(arr[n-1])

        isSubSetSumUtil(arr,res,n-1,sum)
        isSubSetSumUtil(arr,res,n-1, sum-arr[n-1])

    res = []
    res = isSubSetSumUtil(arr,res,n,sum)
    return res

if __name__ == "__main__":
    print isSubSetSum([2,3,5,6,8,10],6,14)
