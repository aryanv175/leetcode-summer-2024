class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        
        start = 0
        end = len(needle)

        while end < len(haystack):
            print(haystack[start:end])
            if haystack[start:end] == needle:
                return start
            start+=1 
            end+=1
        return start