def removeDupes_hash(word):
    ret = ''
    dic = {}
    for c in word:
        if c not in dic:
            ret += c
            dic[c] = 1
    return ret

def removeDupes_NoOrder(word):
    ret = ''
    j = 0
    List = sorted(list(word))
    for i in xrange(len(List)):
        if List[i] != List[j]:
            j += 1
            List[j] = List[i]

    return ''.join(List[0:j+1])

if __name__ == "__main__":
    print removeDupes_hash("geeksforgeeks")
    print removeDupes_NoOrder("geeksforgeeks")
