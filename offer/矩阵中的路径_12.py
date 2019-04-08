# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self,matrix, rows, cols, path):
        # write code here
        #matrix=numpy.array([x for x in matrix]).reshape(rows,cols)
        """字符串path在找的字符串中是连续、有序存在的"""
        if not matrix or rows <= 0 or cols <= 0:
            return 0
        if not path:
            return 1
        #temp_col,temp_matrix=1,[[matrix[0]]]
        #for item in matrix[1:]:
        #    if temp_col<cols:
        #        temp_matrix[-1].append(item)
        #        temp_col+=1
        #    else:
        #        temp_matrix.append([item])
        #        temp_col=1
        #matrix=temp_matrix
        """可以先将matrix字符串转换成二维数组，或者直接将要检查的行列，转换成matrix的索引"""
        find_flag= [0]
        def find_path(i, j, visited, x):#x之前的已经被连续的匹配了
            index_1=i*cols+j#index_1从0开始
            # if x==len(path):
            #     find_flag[0] = 1
            #     return
            """这里一定不能写成这样的。比如matrix='aaaaaaaaaaaa'三行四列，path=‘aaaaaaaaaaaa'。这样的话
            当最后一个比较之后，x是无法到下一个的。所以要在比较是否相同的同时就判断是否是最后一个"""
            if matrix[index_1]==path[x]:
                if x==len(path)-1:
                    find_flag[0]=1
                else:
                    for (a, b) in [(m, n) for (m, n) in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)] if \
                                   m < rows and m >= 0 and n < cols and n >= 0 and (m, n) not in visited]:
                        if not find_flag[0]:
                            find_path(a, b, visited|set([(i,j)]), x + 1)
        for row in range(0,rows):
            for col in range(0,cols):
                if not find_flag[0] and matrix[row*cols+col]==path[0]:
                    find_path(row, col, set(), 0)
        return find_flag[0]

"""上述的是字符串path在找的字符串中是连续、有序存在的，如果不是连续的，但是有序的，那么也是好找的。
！！！！！！难点来了，如果是既不是连续的，也不是有序的呢。。这样的话都不要使用回溯。只要从头到尾吧matrix穿起来
，然后就是最完整的路径了，看这个路径和path的重合度。也就是说直接统计matrix里面的数量就好啦！！！"""
matrix='aaaaaaaaaaaa'
path='aaaaaaaaaaaa'
test=Solution()
print(test.hasPath(matrix,3,4,path))
