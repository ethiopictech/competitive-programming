class Solution:
    def isPalindrome(self, s: str) -> bool:
        String=""
        for c in s:
            if c.isalnum():
                String+=c.lower()
        return String==String[::-1]
