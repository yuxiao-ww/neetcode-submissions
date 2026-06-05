class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "1234567890QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
        l, r = 0, len(s)-1

        while l <= r:
            if s[l] not in valid:
                l += 1
            elif s[r] not in valid:
                r -= 1
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True
