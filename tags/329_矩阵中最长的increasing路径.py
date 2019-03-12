class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        rows,cols=len(matrix),len(matrix[0])
        ans=[]
        #assist_matrix=[[0]*len(matrix[0]) for _ in range(0,len(matrix))]
        def find_increasing_path(res,i,j,visited):
            #if not assist_matrix[i][j]:
            if not res or matrix[res[-1][0]][res[-1][1]]<matrix[i][j]:
                last_flag=1#一定要设置一个flag，看是否是最后一个。
                for (a,b) in [(m,n) for (m,n) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if m>=0 and m<rows and\
                             n<cols and n>=0 and (m,n) not in visited]:
                    #assist_matrix[i][j]=1
                    last_flag=0#
                    find_increasing_path(res+[(i,j)],a,b,visited|set([(i,j)]))
                if last_flag:
                    ans.append(res+[(i,j)])
            else:
                ans.append(res)
        for i in range(0,len(matrix)):
            for j in range(0,len(matrix[i])):
                find_increasing_path([],i,j,set())
        ans.sort(key=len)
        return ans
#超时了。
matrix=[[9,9,4],[6,6,8],[2,1,1]]
matrix=[[1]]
test=Solution()
print(test.longestIncreasingPath(matrix))