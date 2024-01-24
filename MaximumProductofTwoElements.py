#1464. Maximum Product of Two Elements in an Array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        l=len(nums)
        # res=0
        # nums.sort()
        # return((nums[-1]-1)*(nums[-2]-1))

        maxi=0
        second=0
        counter=0

        for i in range(l):
            # second=maxi
            if(nums[i]>=maxi):
                counter=maxi
                maxi=nums[i]
               
                continue

            elif (nums[i]>counter):
                    counter = nums[i]
                

                

            
        #print(maxi,counter)    
        return ((maxi-1) * (counter-1))    




        
