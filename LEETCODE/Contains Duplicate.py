


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i,n in enumerate((nums)):
            aux=target- n
            if aux in dic: 
                return[dic[aux],i]
            dic[n]=i
            return 