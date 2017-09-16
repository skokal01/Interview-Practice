def wordPatternMatch(pattern, str):
    return dfs(pattern, str, {})

def dfs(pattern, str, dict):
    if len(pattern) == 0 and len(str) > 0:
        return False
    if len(pattern) == len(str) == 0:
        return True
    import pdb
    pdb.set_trace()
    for end in range(1, len(str)-len(pattern)+2): # +2 because it is the "end of an end"
        if pattern[0] not in dict and str[:end] not in dict.values():
            dict[pattern[0]] = str[:end]
            if dfs(pattern[1:], str[end:], dict):
                return True
            del dict[pattern[0]]
        elif pattern[0] in dict and dict[pattern[0]] == str[:end]:
            if dfs(pattern[1:], str[end:], dict):
                return True
    return False
if __name__ == "__main__":
    print wordPatternMatch("ABBA", "redbluebluered")
