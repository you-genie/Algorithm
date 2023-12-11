class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for string in strs:
            _prefix = ''
            for c1, c2 in zip(prefix, string):
                if c1 != c2:
                    break
                else:
                    _prefix += c1
            
            prefix = _prefix
        return prefix