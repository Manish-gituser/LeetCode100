1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m=max(candies)
        list1=[]
        for i in candies:
            if (i+extraCandies)>=m:
                list1.append(True)
            else:
                list1.append(False)
        return list1


from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        m = max(candies)
        return list(map(lambda i: (i + extraCandies) >= m, candies))
