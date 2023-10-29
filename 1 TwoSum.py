class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict={}
        # iterate through array enumerate return the num and index
        for i,num in enumerate(nums):
            numX=target-num
            if numX in num_dict:
                return [num_dict[numX],i]
            num_dict[num]=i
        return False
        
