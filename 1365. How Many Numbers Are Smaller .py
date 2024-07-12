1365. How Many Numbers Are Smaller Than the Current Number
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=len(nums)
        res=[]
        for i in range(l):
            count=0
            for j in range(l):
                if(i!=j) and nums[j]<nums[i]:
                    count+=1
            res.append(count)
        return res

        
