def push_and_pop_match(nums1,nums2):
    if not nums1 or not nums2:
        return None
    stack_1,i,j=nums1 and [nums1[0]],0,1
    while(stack_1):
        if stack_1[-1]==nums2[i]:
            stack_1.pop()
            i+=1
        elif j<len(nums1):
            stack_1.append(nums1[j])
            j+=1
        else:
            return False
    return True

nums1=[1,2,3,4,5]
nums2=[4,5,3,2,1]
nums3=[4,3,5,1,2]
nums4=[1,1,1,1,1]
print(push_and_pop_match(nums1,nums2))
print(push_and_pop_match(nums1,nums3))
print(push_and_pop_match(nums1,nums3))