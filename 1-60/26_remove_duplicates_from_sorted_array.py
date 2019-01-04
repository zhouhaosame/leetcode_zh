"""
def removeDuplicates(nums):
    if not nums: return nums
    first,second,l=0,0,len(nums)
    while(second<l):
        if nums[first]==nums[second]:
            second+=1
            continue
        first+=1
        nums[first]=nums[second]
        second+=1
    return nums[:first+1]
x=[1,1,2,3,4,5,6,6,7,7,7,7,9]
print(removeDuplicates(x))
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return nums
        first, second, l = 0, 0, len(nums)
        while (second < l):
            if nums[first] == nums[second]:
                second += 1
                continue
            first += 1
            nums[first] = nums[second]
            second += 1
        return nums[:first + 1]

import json
def stringToIntegerList(input):
    return json.loads(input)


def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])


def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);

            ret = Solution().removeDuplicates(nums)

            out = integerListToString(nums, len_of_list=ret)
            print(out)
        except StopIteration:
            break
if __name__ == '__main__':
    main()