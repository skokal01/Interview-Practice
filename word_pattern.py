from collections import defaultdict
def wordPattern(pattern, str):
    """
    :type pattern: str
    :type str: str
    :rtype: bool
    """
    t = str.split()
    if len(pattern) != len(t):
        return False

    import pdb
    pdb.set_trace()
    p_dict = defaultdict(int)
    t_dict = defaultdict(int)

    for i in xrange(len(pattern)):
        if p_dict[pattern[i]] == 0 and t_dict[t[i]] == 0:
            p_dict[pattern[i]] = t[i]
            t_dict[t[i]] = pattern[i]
        elif p_dict[pattern[i]] != t[i] or t_dict[t[i]] != pattern[i]:
            return False
    return True

if __name__ == "__main__":
    print wordPattern("abba", "dog dog dog dog")
    print wordPattern("abba", "dog cat cat dog")
    print wordPattern("abba", "dog cat cat fish")
