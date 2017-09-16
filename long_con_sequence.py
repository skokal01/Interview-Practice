'''
https://leetcode.com/problems/longest-consecutive-sequence/#/description
https://discuss.leetcode.com/topic/15383/simple-o-n-with-explanation-just-walk-each-streak
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
'''
def longestConsecutive(nums):
    nums = set(nums)
    best = 0
    for x in nums:
        if x - 1 not in nums:
            y = x + 1
            while y in nums:
                y += 1
            best = max(best, y - x)
    return best

if __name__ == "__main__":
    print longestConsecutive([100, 4, 200, 1, 3, 2])
    print longestConsecutive([10,20,20,30,40,50,11,12])
