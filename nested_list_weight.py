from collections import deque
#https://discuss.leetcode.com/topic/41664/python-iterative
def depthSum_Iterative(nestedList):
    if not nestedList:
        return 0

    queue = deque()
    sum = 0
    for n in nestedList:
        queue.append((n,1))

    while queue:
        nxt,d = queue.popleft()
        if isinstance(nxt,int):
            sum += d * nxt
        else:
            for i in nxt:
                queue.append((i,d+1))
    return sum

def depthSum_Recursive(nestedList):
    def helper(nestedList, level):
        if not nestedList:
            return 0
        sum = 0
        for n in nestedList:
            if isinstance(n, int):
                sum += n * level
            else:
                sum += helper(n, level+1)
        return sum
    return helper(nestedList,1)

if __name__ == "__main__":
    print depthSum_Iterative([[1,1],2,[1,1]]) #return 10 (four 1's at depth 2, one 2 at depth 1)
    print depthSum_Iterative([1,[4,[6]]]) #return 27 (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)
    print depthSum_Recursive([[1,1],2,[1,1]]) #return 10 (four 1's at depth 2, one 2 at depth 1)
    print depthSum_Recursive([1,[4,[6]]]) #return 27 (one 1 at depth 1, one 4 at depth 2, and one 6 at depth 3; 1 + 4*2 + 6*3 = 27)
