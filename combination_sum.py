class Solution(object):
    def backtrack(self,arr, target, res, tmp, start):
        if target < 0:
            return
        elif target == 0:
            res.append(tmp[:])
        else:
            for i in xrange(start,len(arr)):
                tmp.append(arr[i])
                self.backtrack(arr,target-arr[i],res,tmp,i+1)
                tmp.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        res = []
        self.backtrack(candidates,target,res,[],0)
        import pdb
        pdb.set_trace()
        return res

if __name__ == "__main__":
    obj = Solution()
    print obj.combinationSum([2,3,6,7],7)
