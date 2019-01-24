def find_path_in_matrix(matrix, path):
    if not matrix:
        return False
    row, col,ans = len(matrix), len(matrix[0]),[]
    def dfs(res, i, j, visited, k):
        """其中，res表示已经走过的某条路径，i,j表示要检查的当前的格子，visited是一个集合，存储所有的已经访问过的位置，
        k表示将要匹配的路径的位置
        注意点，path是路径中的一些点，并不一定就是相邻的点。
        我们是找蕴含这条路径的长路径，所以path的最后一个点是长路径的结尾。
        一共有三个注意点一定要注意"""
        if not (0<=i<row and 0<=j<col):
            return
        if matrix[i][j] == path[k]:
            if k == len(path)-1:
                res.append(matrix[i][j])
                ans.append(res)
                """1、原来这里用的是return res，只想返回一条。
                其实这样是错误的，因为这一个返回只是结束了一条路径。
                也就是说，出现res一定要跟着ans"""
            else:
                for (a, b) in [(a, b) for (a, b) in [(i, j+1), (i, j-1), (i-1, j ), (i+1, j)] if
                               0 <= a < row and 0 <= b < col and (a, b) not in visited]:
                    dfs(res + [matrix[i][j]], a, b, visited | set([(i, j)]), k + 1)#集合的并集
                    """2、这里的res是[],所以matrix外面一定要加上[]"""
        else:
            for (a, b) in [(a, b) for (a, b) in [(i, j+1), (i, j-1), (i-1, j ), (i+1, j)] if
                           0 <= a < row and 0 <= b < col and (a, b) not in visited]:
                dfs(res+ [matrix[i][j]], a, b, visited | set([(i, j)]), k)
                """这里的res也要加上一个matrix，因为path是长路径的一个subsequence"""
    dfs([],0,0,set(),0)#这里是从左上角作为起点，当然也可以从任意的作为起点
    return ans
matrix=[['a','b','t','g'],['c','f','c','s'],['j','d','e','h']]
matrix=[['a','a','b','c']]
path='bfce'
#path='abfb'
path='abc'
print(find_path_in_matrix(matrix,path))