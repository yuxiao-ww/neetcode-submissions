class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]

        while slow != fast:  # 检测环
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        # 找环的入口
        slow = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow