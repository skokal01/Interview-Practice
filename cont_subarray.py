def findUnsortedSubarray(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 2:
        if nums[0] > nums[1]:
            return 2
        else:
            return 0

    s = 0
    e = len(nums)-1
    found = False

    for i in xrange(0,len(nums)-1,1):
        if nums[i] > nums[i+1]:
            s = i
            found = True
            break

    if not found:
        return 0

    for i in xrange(len(nums)-1,0,-1):
        if nums[i] < nums[i-1]:
            import pdb
            pdb.set_trace()
            e = i
            break

    min = nums[s]
    max = nums[s]

    for i in xrange(s,e+1,1):
        if nums[i] > max:
            max = nums[i]
        if nums[i] < min:
            min = nums[i]

    for i in xrange(0,s,1):
        if nums[i] > min:
            s = i
            break
    for i in xrange(len(nums)-1,e-1,-1):
        if nums[i] < max:
            e = i
            break

    return e+1-s

if __name__ == "__main__":
    print findUnsortedSubarray([2,3,3,2,4])
