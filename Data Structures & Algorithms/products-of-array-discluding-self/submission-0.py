from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        prefix = [1] * n
        suffix = [1] * n
        output = [1] * n

        # Calculate prefix products
        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]

        # Multiply prefix and suffix
        for i in range(n):
            output[i] = prefix[i] * suffix[i]

        return output