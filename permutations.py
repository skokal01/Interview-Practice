# Python function to print permutations of a given list
def perms(lst):
    import pdb
    pdb.set_trace()
    stack = lst
    results = [stack.pop()]
    while len(stack) != 0:
        c = stack.pop()
        new_results = []
        for w in results:
            for i in range(len(w)+1):
                new_results.append(w[:i] + c + w[i:])
        results = new_results
    return results

# Another iterative version
# https://discuss.leetcode.com/topic/6377/my-ac-simple-iterative-java-python-solution
def permute(nums):
    perms = [[]]
    for n in nums:
        new_perms = []
        for perm in perms:
            for i in xrange(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])   ###insert n
                if i < len(perm) and perm[i] == n: # to handle duplication
                    import pdb
                    pdb.set_trace()
                    break
        perms = new_perms
    return perms

# Not working retLst() not appending
def perm_helper(lst, l, r):
    if len(lst) == 0:
        return []

    if len(lst) == 1:
        return [lst]

    if l == r:
        return lst

    retLst = []

    for i in xrange(l, r+1):
        lst[l],lst[i] = lst[i], lst[l]
        retLst.append(perm_helper(lst, l+1, r))
        lst[l],lst[i] = lst[i], lst[l]

    return retLst

def perm2(lst):
    return perm_helper(lst,0, len(lst)-1)

def permutation(lst):

    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []

    # If there is only one element in lst then, only
    # one permuatation is possible
    if len(lst) == 1:
        return [lst]

    # Find the permutations for lst if there are
    # more than 1 characters

    l = [] # empty list that will store current permutation

    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]

       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]

       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l


# Driver program to test above function
data = list('112')
print permute(data)
# for p in permutation(data):
#     print p
