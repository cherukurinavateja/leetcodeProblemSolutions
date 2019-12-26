class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s) == 1) or (s == s[::-1]):
            return s
    
        else:

            sr=""
            for i in range(len(s)):
                for j in range(i,len(s)):
                    if s[i:j+1] == s[i:j+1][::-1]:
                        if len(s[i:j+1]) > len(sr):
                            sr=s[i:j+1]
            return sr