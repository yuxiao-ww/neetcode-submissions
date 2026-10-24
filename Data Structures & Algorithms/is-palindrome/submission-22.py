class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        
        chars = "QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp1234567890"
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] not in chars:
                l += 1
            elif s[r] not in chars:
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True
            