"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...
Note:
n is positive and will fit within the range of a 32-bit signed integer (n < 231).
Example 2:
Input:11
Output:0
Explanation:
The 11th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ... is a 0,
which is part of the number 10.
"""
def f(n):#leetcode 400. Nth Digit
    char_nums=0
    k=1
    while(char_nums+9*pow(10,k-1)*k<n):
        char_nums+=9*pow(10,k-1)*k
        k+=1
        #先找到这个n在哪个数位段上。然后确定数位段的第一个数，在这个数位段上继续找
    n-=char_nums
    x=n/k
    y=n%k
    if y==0:
        #这意味着。要找的恰好在这个数位段上的某个数的最后一个字符。比如
        #k=2的时候，从10开始，我找第4位，当时是11的后面的1.4/2=2,4%2=0。说明是已经过去两个数了
        #但是是下一个数的第0个，这个就是相当于下一个数的前一个数的最后位置。 这个所以是pow(10,k-1)+x-1，
        #找到这个number之后，取出最后一位即可
        return str(pow(10,k-1)+x-1)[-1]
    else:
        #但是找第五位呢。5/2=2,5%2=1.说明是已经过去两个k了，分别是10,11.并且是12的第一个数
        x_post=str(pow(10,k-1)+x)
        for i in range(len(x_post)):
            if i==y-1:
                return x_post[i]
print(f(11))





