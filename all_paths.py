'''
Print all possible paths from top left to bottom right of a mXn matrix
The problem is to print all the possible paths from top left to bottom right
of a mXn matrix with the constraints that from each cell you can either move
only to right or down.
http://www.geeksforgeeks.org/print-all-possible-paths-from-top-left-to-bottom-right-of-a-mxn-matrix/
'''
def findAllPaths(arr):
    res = []
    findAllPathsUtil(arr,0,0,[],res)
    return res

def findAllPathsUtil(arr,row,col,paths,res):
    # import pdb
    # pdb.set_trace()
    if row == len(arr)-1:
        for i in xrange(len(arr[0])-col):
            paths.append(arr[row][i+col])
        res.append(paths)
        # paths.append(paths)
        return

    if col == len(arr[0])-1:
        for i in xrange(len(arr)-row):
            paths.append(arr[i+row][col])
        res.append(paths)
        # paths.append(paths)
        return

    paths.append(arr[row][col])

    findAllPathsUtil(arr,row+1,col,paths[:],res)
    findAllPathsUtil(arr,row,col+1,paths[:],res)


if __name__ == "__main__":
    print findAllPaths([[1,2,3],[4,5,6]])
