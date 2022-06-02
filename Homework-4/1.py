class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] + nums[i] == target:
                    return [i, j]

    def twoSum(self, nums: list, target: int) -> list:
        snums = sorted(nums)

        L, R = 0, len(nums) - 1

        while L < R:
            y = snums[L] + snums[R]
            if y > target:
                R -= 1
            elif y < target:
                L += 1
            else:
                i = nums.index(snums[L])

                nums.reverse()
                j = len(nums) - nums.index(snums[R]) - 1

                return [i, j]

    def twoSum(self, nums, target):
        dic = {}
        for i, n in enumerate(nums):
            if n in dic:
                return [dic[n], i]
            dic[target - n] = i
