def remove_element(nums,val):
    if not nums:return 0
    head,tail,l=0,len(nums)-1,len(nums)
    while(head<=tail):
        while(tail>=head and nums[tail]==val):
            tail-=1
        while(head<=tail):
            if nums[head]==val:
                temp=nums[head]
                nums[head]=nums[tail]
                nums[tail]=temp
                head+=1
                break
            else:head+=1
    return nums[:tail+1],tail+1
print(remove_element([1,2,3,3,3,4,5,6,6,7,7,8],3))