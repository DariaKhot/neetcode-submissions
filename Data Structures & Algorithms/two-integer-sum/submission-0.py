class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked={}
        for i in range(0,len(nums)):
            diff=target-nums[i]
            if diff in checked: 
                return [checked[diff],i]
            else:
                checked[nums[i]]=i
        return []