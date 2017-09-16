def solveNQueens(n):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum:
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
    result = []
    DFS([],[],[])
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.result = []
        self.board = [["." for _ in xrange(n)] for _ in xrange(n)]
        self.n = n
        self.solve(0)
        return self.result

    def solve(self,row):
        import pdb
        pdb.set_trace()
        if row == self.n:
            solution = []
            for i in self.board:
                solution.append(''.join(i))
            self.result.append(solution)

        for col in xrange(self.n):
            if self.isSafe(row,col):
                self.board[row][col] = 'Q'
                self.solve(row+1)
                self.board[row][col] = '.'

    def isSafe(self,row,col):
        for i in xrange(self.n):
            if self.board[i][col] == 'Q':
                return False

        i = row-1
        j = col-1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        i = row-1
        j = col+1
        while i >= 0 and j < self.n:
            if self.board[i][j] == 'Q':
                return False
            i -= 1
            j += 1

        return True;


if __name__ == "__main__":
    # print solveNQueens(4)
    q = Solution()
    print q.solveNQueens(4)
