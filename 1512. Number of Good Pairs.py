#1512. Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        l=len(nums)
        c=0
        for i in range(l):
            for j in range(i+1,l):
                if (nums[i]==nums[j]):
                    c=c+1
        return c

        


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res={}
        ans=0
        for num in nums:
            if num in res:
                ans+=res[num]
                res[num]+=1
            else:
                res[num]=1
        return ans

            

        
