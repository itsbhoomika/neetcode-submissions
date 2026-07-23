class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap ={}

        for i in range(len(nums)):
            next= nums[i]
            if next in hashmap:
                return True

            hashmap[next]= i

        return False