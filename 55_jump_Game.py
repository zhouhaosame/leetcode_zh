#上一题与这个类似的是找多少步跳到的，找到left-right之后，确定该范围内，能跳的最远的
#范围，那表示最少花费多少步可以跳的最远。如果跳的最远的时候仍然跳不出原先的范围呢，
#那不就是意味着，是跳不到最后的吗
def jumpGame(nums):
    left,right,l_nums=0,0,len(nums)
    while(right<l_nums-1):
        """为什么要减去1呢？
        因为，right表示的是能跳到的最大的范围的最右侧对吧。如果right==l_nums-1了
        这不就是意味着，已经可以跳到最后了吗？？
        如果不减去一,在【0】这种情况下，返回的是false"""
        pre_left,pre_right=left,right
        right=max([index+nums[index] for index in range(left,right+1)])
        if right<=pre_right:#意味着跳不出去啊
            return False
        else:
            left=pre_right+1#到这里就意味着right跳出原来的范围了，极端情况
            #left==right,nums[left]==0,这个再循环一次，就return false了
            # 然后left表示的
            #是什么？？不知道表示的是什么啊？应该就是一个bounds吧
    return True
nums=[3,2,1,0,4]
print(jumpGame(nums))