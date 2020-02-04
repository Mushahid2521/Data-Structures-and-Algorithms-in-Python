def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    res = []
    nums.sort()
    l = len(nums)
    print(nums)

    for i in range(0,l-2):
        if(i>0 and nums[i-1]==nums[i]):
            continue
        j = i+1
        k = l-1

        while(j<k):
            s = nums[i]+nums[j]+nums[k]
            if(s==0):
                res.append([nums[i],nums[j],nums[k]])
                j+=1
                while(j<l and nums[j]==nums[j-1]):
                    j+=1
                while(k>0 and nums[k]==nums[k-1]):
                    k-=1
            elif(s>0):
                k-=1
            elif(s<0):
                j+=1

    return res


print(threeSum([-1,0,1,2,-1,-4]))