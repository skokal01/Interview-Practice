'''
http://codercareer.blogspot.com/2013/02/no-37-missing-number-in-array.html
'''
def missingNumber(arr):
    if not arr:
        return None

    left,right = 0,len(arr)-1

    # import pdb
    # pdb.set_trace()
    while left <= right:
        middle = (left+right)/2
        if arr[middle] != middle+1:
            if middle == 0 or arr[middle-1] == middle:
                return middle
            right = middle-1
        else:
            left = middle+1

    if left == len(arr):
        return len(arr)

    return None

if __name__ == "__main__":
    print missingNumber([1,2,3,3,4])
    print missingNumber([1,2,3,4,5,6,6,7,8,9])
