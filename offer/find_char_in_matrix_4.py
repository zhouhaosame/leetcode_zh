import bisect


class find_char_in_matrix:
    def __init__(self, matrix, number):
        self.matrix = matrix
        self.number = number

    def find_char(self):
        if not self.matrix: return False
        rows, cols = len(self.matrix), len(self.matrix[0])
        row, col = 0, cols - 1
        while (row < rows and col >= 0):
            index = bisect.bisect_left(self.matrix[row][:col + 1], self.number)
            #这种情况一定要小心，因为当列表中所有的元素都是小于number的时候，返回的是最右侧index+1，是超过范围的
            if index==col+1:
                row+=1
                continue
            elif index==-1:
                return False
            else:
                if self.matrix[row][index] == self.number:
                    return True
                else:
                    col = index - 1
                    row += 1
        return False


test = find_char_in_matrix(
    [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]],
    20).find_char()
print(test)
"""一般应用场景都不用考虑这个大小，因为这个上限很高，需要用到这么多元素的list的时候，都需要考虑很多其它问题。
32位python的限制是 536870912 个元素。
64位python的限制是 1152921504606846975 个元素。"""