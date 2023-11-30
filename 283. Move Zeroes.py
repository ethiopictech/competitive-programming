class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=0
        n=len(nums)
        for num in nums:
            if(num !=0):
                nums[j]=num
                j+=1

        for x in range(j,n):
            nums[x]=0
