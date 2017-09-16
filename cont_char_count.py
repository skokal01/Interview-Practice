'''
https://www.careercup.com/question?id=6441875862978560
I/p: aaaabbbcdddeeeeeeff
O/p: a4b3c1d3e7f2
'''
def countContinuousCharacaters(s):
    if not s:
        return ""

    ret = []
    count = 1

    for i in xrange(1,len(s)):
        if s[i-1] == s[i]:
            count += 1
        else:
            ret.append(s[i-1] + str(count))
            count = 1
    return ''.join(ret)

if __name__ == "__main__":
    print countContinuousCharacaters("aaaabbbcdddeeeeeeff")
    print countContinuousCharacaters("abcdef")
    print countContinuousCharacaters("")
