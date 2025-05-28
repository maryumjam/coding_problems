import numpy as np
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if np.abs(target-nums[i])==nums[j]:
                     print("Indices",i,j)
                     continue
                
    def twoSum_On(self, nums, target):
         """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
         hashmap={}
         for i in range(len(nums)):
             remainder= np.abs(target-nums[i])
             if remainder in hashmap:
                 print(i, hashmap[remainder])
                 return
             hashmap[nums[i]]=i #Values as keys and Indices and Values
             
                
if __name__ == "__main__":
    solution1= Solution()
    nums = [3,2,4, 9, 10, 22]
    target = 19
    solution1.twoSum(nums, target)
    solution1.twoSum_On(nums,target)