class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checker = set()

        for n in nums:
            if n in  checker:
                return True
            checker.add(n)
        return False
            
        
            
        