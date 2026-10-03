class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        check1 = len(nums)
        checkSet = set(nums)
        check2 = len(checkSet)
        if (check1 == check2):
            return False
        else:
            return True