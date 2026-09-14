class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        hash = {}
        l = 0
        r = 0 
        while r < len(s): 
            if s[r] in hash:
                if hash[s[r]] >= l:
                    l = hash[s[r]] + 1
                    
            cnt = r-l+1
            longest = max(longest,cnt)
            hash[s[r]] = r
            r+=1 
            
            
        return longest

    
        