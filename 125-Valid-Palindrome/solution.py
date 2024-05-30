import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase
        lowercase_str = s.lower()

        # Filter out non-letter characters
        cleaned = re.sub(r'[^a-z0-9]', '', lowercase_str)    

        if cleaned == cleaned[::-1]:
            return True
        return False