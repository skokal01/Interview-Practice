from collections import deque

def isAdjacent(str1,str2):
    count_diffs = 0
    for a,b in zip(str1,str2):
        if a != b:
            if count_diffs:
                return False
            count_diffs += 1

    return True
def ladderLength(beginWord,endWord,wordList):
    # import pdb
    # pdb.set_trace()
    queue = deque([[beginWord,1]])
    while queue:
        cur,length = queue.popleft()
        print cur,
        if cur == endWord:
            return length

        for i in xrange(len(cur)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                next_word = cur[:i] + c + cur[i+1:]
                if next_word in wordList:
                    wordList.remove(next_word)
                    queue.append([next_word, length+1])
    return 0

if __name__ == "__main__":
    print ladderLength("hit","cog", ["hot","dot","dog","lot","log","cog"])
