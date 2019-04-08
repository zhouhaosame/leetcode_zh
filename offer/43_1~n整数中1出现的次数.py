def f(n):#leetcode 233,使用递归
    if n<=0:
        return 0
    n = str(n)
    nums = [0] * (len(n)+1)
    """nums中存的是index位的所有树最多对应的1的个数，如nums[2]中存的是
    所有的两位数对应的1的个数"""
    def sum_one_frequency_according_to_len(l):
        for i in range(1, l+1):
            nums[i] = sum(nums[0:i]) * 9 + pow(10, i-1)
            """长度为l的所有数中包含的1的个数，类似动态规划"""
    sum_one_frequency_according_to_len(len(n))
    def sum_one_frequency_from_0_to_n(n):
        """这个函数的作用是，求从0到n中，所有1的个数"""
        if len(n)<=0 or not n.lstrip("0"):
            return 0
        n=n.lstrip("0")
        """这里之所以去除左边开始的一串0.是为了防止这种情况，比如1000023。很明显
        我们考虑的是从1000000,100000001,100000002.....到100000023"""
        if n[0]=="1" and n[1:]:
            """一定要判断一下，n[1;]，因为后面需要int(n[1:])"""
            return sum(nums[0:len(n)])+\
                   sum_one_frequency_from_0_to_n(n[1:])+int(n[1:])+1
        #假设n有len(n)。我们先求1位到len(n)-1位的所有number包含的1的个数
        #就是sum(nums[0:len(n)])，因为我们求的是从一位开始的，二位，三位...这样的
        #然后使用递归，求len(n)位时，1个个数。
        #int(n[1:])+1，这个是首位的1的个数。比如100,101,102.所以要加上1
        elif n[0]=="1":
            return 1#当n长度为1时
        else:
            return sum(nums[0:len(n)])+(int(n[0])-1)*sum(nums[0:len(n)])+\
                   sum_one_frequency_from_0_to_n(n[1:])+pow(10,len(n)-1)
        #第一个sum(nums[0:len(n)])是求1位到len(n)-1位的。第二个sum(nums[0:len(n)])
        #求的是首位1到（比如首位是n）n-1时，后面的其它位数表示的数中出现的1的数量。
        #因为首位不是1了，所以考虑首位是n的情况时，sum_one_frequency_from_0_to_n(n[1:])
        #pow(10,len(n)-1)表示首位是1时，首位1出现的个数。
    return sum_one_frequency_from_0_to_n(n)

def NumberOf1Between1AndN_Solution(n):
    # write code here
    if not n:
        return 0
    ans,m=0,10
    ans += n // m + int(n % m != 0)
    """
    这个是个位为1的个数，n/m表示当个位为1的时候，前面一定有多少个前缀。比如112，前缀是11（0-10）一共11个。接下来
    去判断前缀为11的时候，是否个位为1.这里一定要加上int，不然的话，返回的ans是一个bool变量
    """
    while(n//m):#看某位是否存在，存在的话才有比较的含义
        m = m * 10
        ans+=n//m*(m//10)+min(max(n%m-m//10+1,0),m//10)
        """n//m表示：看十位的时候，当十位为1，前面一共有多少种。*（m/10）是前缀确定，十位为1的时候，后面一共多少种变化
        比如112,1表示百位为0时候，十位为1，个位一共始终变化。当百位为1时（这种情况下由于不知道后缀从什么位置开始，所以要
        单独考虑。n%m取百位之后的。只要判断十位是否为1，为1的时候，个位有多少个。-m//10是为了减去0-9.（因为他们的十位不可能
        为1,12-10+1=3.正好10,11,12三个。如果十位不是1，而是大于1的。那么说明十位1的所有可能都出现了，所以使用min函数）"""
    return ans
#print(sum_one_frequency(4))
a=112
print(NumberOf1Between1AndN_Solution(a))
print(f(a))

# -*- coding:utf-8 -*-
class Solution:
    def movingCount(self, threshold, rows, cols):
        if not rows and not cols:
            return 0
        # write code here
        ans=set()
        def my_sum(x,y):
            newsum=0
            for item in [x,y]:
                while(item):
                    newsum+=item%10
                    item=item//10
            return newsum
        def back_tracking(i,j):
            ans.add((i,j))
            for x,y in [(a,b) for (a,b) in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if a<rows and a>=0 and b<cols and b>=0 \
                        and my_sum(a,b)<=threshold and (a,b) not in ans]:
                back_tracking(x,y)
        back_tracking(0,0)
        return len(ans)

