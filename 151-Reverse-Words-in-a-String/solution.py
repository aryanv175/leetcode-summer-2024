class Solution:
    def reverseWords(self, s: str) -> str:
        arr = s.split(' ')
        res = ''
        for i in range(len(arr)-1, -1, -1):
            if arr[i] != '':
                res = res + arr[i] + ' '
        return res[:-1]


