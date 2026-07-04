class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""

        need = {}
        window = {}

        for c in t:
            need[c] = need.get(c,0)+1

        have = 0
        needCount = len(need)
        left = 0
        result = [-1,-1]
        resultLength = float("inf")

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c,0)+1

            if c in need and window[c]==need[c]:
                have+=1

            while have == needCount:
                if (right-left+1)<resultLength:
                    result = [left,right]
                    resultLength = right - left + 1

                window[s[left]] -= 1

                if s[left] in need and window[s[left]]<need[s[left]]:
                    have-=1

                left+=1

        l,r = result

        if resultLength == float("inf"):
            return ""

        return s[l:r+1]