def findMedianSortedArrays(nums1, nums2):
    m, n = len(nums1), len(nums2)
    if m > n:#保证nuns1是短的那个
        nums1, nums2, m, n = nums2, nums1, n, m
    imin, imax, half_len = 0, m, (m + n + 1) // 2#奇数取中间的，偶数取中间左边的
    """一定存在这样的一组i，j，满足这个性质。我们所要做的只是找到他们"""
    while imin <= imax:#二分法的“标志性”判断
        i = (imin + imax) // 2
        j = half_len - i#保证part(left)==part(right),j>0已证。
        if i < m and nums2[j - 1] > nums1[i]:
            # i is too small, must increase it.这次找的i太小了，说明准确的i在后面，然后，则imin
            #做出相应的改变
            imin = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:#i一定要是>0
            # i is too big, must decrease it
            imax = i - 1#imin和imax每次都只改变一个
        else: # i is perfect    
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:#j==0的情况只有当m=n（n-1）时才成立
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])
            if (m + n) % 2 == 1:
                return max_of_left#因为设置求j的公式的原因，当奇数的时候，多余的那个在左侧
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])
            return (max_of_left + min_of_right) / 2
nums1=[1,3,4,5,67]
nums2=[3,5,8,9,77,88]
print(findMedianSortedArrays(nums1,nums2))
nums1=nums1+nums2#这才是正确的链接链接的方式
nums1.sort()
print(nums1)
nums1.append(nums2)#[1, 3, 4, 5, 67, [3, 6, 8, 9, 4, 88]]使用append方法是将nums2作为一个元素加入nums1中。

