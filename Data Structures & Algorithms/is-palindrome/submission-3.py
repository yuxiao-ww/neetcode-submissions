class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm1234567890"
        i, j = 0, len(s)-1

        while i <= j:
            print(i, j)
            if s[i] in valid and s[j] in valid:
                if s[i].lower() != s[j].lower():
                    return False
                i += 1
                j -= 1
            elif s[i] not in valid:
                i += 1
            elif s[j] not in valid:
                j -= 1
        return True
        