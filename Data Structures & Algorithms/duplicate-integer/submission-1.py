class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
            hashset = set()

## use the hashset as an extra space and compare, find the duplicates 
## in the array
            for n in nums:
                if n in hashset:
                    return True
                hashset.add(n)
            return False
