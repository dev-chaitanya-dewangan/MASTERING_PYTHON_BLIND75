def minimumInRotatedArraySearch(nums):
    l,r=0,len(nums)-1
    while l< r:
        m=l+(r-l)//2
        # print(m,r,"nums[m]--->nums[r]",nums[m],nums[r])
        if nums[m]<nums[r]:
            # print(m,r,"nums[m]--->nums[r]",nums[m],nums[r])
            r=m
        else:
            # print(nums[l])
            l+=1
    # print(nums[l])
    return nums[l]
minimumInRotatedArraySearch([3,4,5,2])
