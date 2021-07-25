def twosum(nums,target):
    lens = len(nums)
    for i in range(lens):
        need = target - nums[i]
        if need in nums:
            if(nums.count(need) == 1) and (need == nums[i]):
                continue
            else:
                j = nums.index(target - nums[i],i+1)
                break
    if j > 0:
        return [i,j]
    else:
        return[]

print(twosum(nums=[1,8,9,20,35,60],target=55))
