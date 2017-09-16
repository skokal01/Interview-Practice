# https://discuss.leetcode.com/topic/30941/here-is-a-10-line-template-that-can-solve-most-substring-problems/12
#1. Use two pointers: start and end to represent a window.
#2. Move end to find a valid window.
#3. When a valid window is found, move start to find a smaller window.
from collections import defaultdict
from sys import maxint
def findSubString(str, pat):
    import pdb
    pdb.set_trace()
    MAX_INT = maxint
    start = end = 0
    char_need = defaultdict(int)    # the count of char needed by current window, negative means current window has it but not needs it
    count_need = len(pat)             # count of chars not in current window but in t
    min_length = MAX_INT
    min_start = 0
    for i in pat:
        # current window needs all char in t
        char_need[i] += 1
    while end < len(str):
        if char_need[str[end]] > 0:
            count_need -= 1
        # current window contains s[end] now, so does not need it any more
        char_need[str[end]] -= 1
        end += 1
        while count_need == 0:
            if min_length > end - start:
                min_length = end - start
                min_start = start
            # current window does not contain s[start] any more
            char_need[str[start]] += 1
            # when some count in char_need is positive, it means
            # there is char in t but not current window
            if char_need[str[start]] > 0:
                count_need += 1
            start += 1
    return "" if min_length == MAX_INT else str[min_start:min_start + min_length]

print findSubString("ADOBECODEBANC", "ABC")
