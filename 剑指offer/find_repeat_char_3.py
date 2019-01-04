from collections import defaultdict


class find_repeat:
    def __init__(self, nums):
        self.nums = nums
        self.dct = defaultdict(int)
    
    def create_dict(self):
        for x in self.nums:
            self.dct[x] += 1
    
    def find_first_unique_char(self):
        if not self.nums: return -1
        self.create_dict()
        unique_char = dict(filter(lambda k_v: k_v[1] < 2, self.dct.items())).keys()
        for x in self.nums:
            if x in unique_char:
                return x
                break
    
    def find_arbitrary_repeat_char(self):
        """发现任意的char，不使用字典（可以先排序，然后，，，）。因为题目中是，n个char，每个char在1至n-1之间
        """
        if not self.nums: return -1
        temp_nums = self.nums
        i = 0
        while (i < len(temp_nums)):
            if temp_nums[i] == i:
                i += 1
            elif temp_nums[i] == temp_nums[temp_nums[i]]:
                return temp_nums[i]
                break
            else:
                temp = temp_nums[temp_nums[i]]
                temp_nums[temp_nums[i]] = temp_nums[i]
                temp_nums[i] = temp
        if i == len(temp_nums):
            return -1
        """这个时间复杂度N，因为任意char交换两次就能够找到位置，空间复杂度1，但是nuns改变了"""
    def find_arbitrary_repeat_char_without_modifing(self):
        """这里与之前的条件是不一样的。共n+1个char，数字在1到n之间
        如果使用字典N时间复杂度，但是浪费空间。如果和上面类似，又修改了nums。
        按照要求，只能够空间来换时间了。
        思路就是，n+1个放到n个框里。那么肯定有重复的啊。因为是找任意一个，所以看多余的那一个在n/2哪一边就好了"""
        left,right=1,len(self.nums)-1
        while(left<right):#因为是一定有的，所以可以true
            count2=count1=0
            flag = (left + right) // 2
            for x in self.nums:
                if left<=x<=flag:
                    count1+=1
                elif flag<x<=right:
                    count2+=1
            if count1>(flag-left+1):
                right=flag
            elif count2>(right-flag):
                left=flag+1
        return left
        
