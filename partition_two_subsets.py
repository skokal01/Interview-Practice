#http://www.geeksforgeeks.org/dynamic-programming-set-18-partition-problem/
'''
Dynamic Programming | Set 18 (Partition problem)
Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.

Examples

arr[] = {1, 5, 11, 5}
Output: true
The array can be partitioned as {1, 5, 5} and {11}

arr[] = {1, 5, 3}
Output: false
The array cannot be partitioned into equal sum sets.
'''
def isSubSetSum(arr,n,sum):
    if sum != 0 and n == 0:
        return False
    if sum == 0:
        return True

    return isSubSetSum(arr,n-1,sum) or isSubSetSum(arr,n,sum-arr[n-1])

def findPartition(arr,n):
    if sum(arr)%2 != 0:
        return False

    return isSubSetSum(arr,n,sum(arr)/2)
if __name__ == "__main__":
    print findPartition([1,5,11,5],4)
    print findPartition([1,5,3],3)
