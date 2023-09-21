import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        low_s = s.lower()
        clear_s = re.sub(r'[^a-z0-9]',"",low_s)
        a1 = clear_s
        a2 = clear_s[::-1]
        return a1 == a2