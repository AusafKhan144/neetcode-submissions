class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window = {}
        maxlen = 0

        for c in s:
            window[c] = window.get(c,0) + 1
            while window[c] > 1:
                left_value = s[left]
                window[left_value] -= 1
                if window[left_value] == 0:
                    del window[left_value]
                left += 1
            maxlen = max(maxlen,len(window))
        return max(maxlen,len(window))