#http://www.geeksforgeeks.org/dynamic-programming-subset-sum-problem/
'''
Dynamic Programming | Set 25 (Subset Sum Problem)
Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Examples: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
'''
def isSubSetSum(arr,n,sum):
    if sum != 0 and n == 0:
        return False
    if sum == 0:
        return True

    return isSubSetSum(arr,n-1,sum) or isSubSetSum(arr,n-1,sum-arr[n-1])

if __name__ == "__main__":
    print isSubSetSum([3,34,4,12,5,2],6,9)
    print isSubSetSum([3,34,4,12,5,2],6,16)
    print isSubSetSum([1],1,1)
    print isSubSetSum([1,2,3],3,7)
