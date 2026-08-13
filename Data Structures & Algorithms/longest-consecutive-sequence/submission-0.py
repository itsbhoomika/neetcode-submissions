class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set= set(nums)
        """So logically:

1. Convert the numbers into a set.
2. Look at each unique number.
3. If num - 1 exists, skip it because it’s somewhere in the middle of a sequence.
4. If num - 1 does not exist, this is a sequence start.
5. From that number, keep looking for num + 1, num + 2, num + 3, etc.
6. Keep track of the longest length seen."""

        longest=0

        for num in nums_set:
            if num-1 not in nums_set:
                current= num
                length =1

                while current + 1 in nums_set:
                    current+=1
                    length+=1
                longest= max(longest, length)
        return longest