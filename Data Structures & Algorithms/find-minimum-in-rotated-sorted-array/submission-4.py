class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float("inf")

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                return res
                break
            
            mid = (l + r) // 2
            res = min(res, nums[mid])

            if nums[l] <= nums[mid]:
                # right unsorted, minimum at right
                l = mid + 1
            else:
                r = mid - 1
        
        return res

        