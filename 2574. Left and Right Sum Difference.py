2574. Left and Right Sum Differences

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l=len(nums)
        left=[]
        right=[]
        ans=[]
        sum=0
        for i in range(l):
            for j in range(i+1,l):
                sum+=nums[j]
            right.append(sum)
            sum=0
        sum=0
        for i in range(0,l):
            for j in range(i-1,-1,-1):
                sum+=nums[j]
            left.append(sum)
            sum=0
        for i in range(l):
            ans.append(abs(right[i]-left[i]))

        return ans

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        l = len(nums)
        left_sum = 0
        right_sum = sum(nums)
        ans = []

        for i in range(l):
            right_sum -= nums[i]
            ans.append(abs(left_sum - right_sum))
            left_sum += nums[i]

        return ans

            
        