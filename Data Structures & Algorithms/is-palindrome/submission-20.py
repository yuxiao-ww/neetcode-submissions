class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        valid = "QAZWSXEDCRFVTGBYHNUJMIKOLPqazwsxedcrfvtgbyhnujmikolp1234567890"
        while l <= r:
            if s[l] in valid and s[r] in valid:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            elif s[l] not in valid:
                l += 1
            else:
                r -= 1
            
        return True