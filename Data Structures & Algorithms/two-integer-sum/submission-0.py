class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        track = {}
        for i, num in enumerate(nums) :
            j = target - num
            if j in track:
                return [track[j], i]
            else:
                track[num] = i
            
        