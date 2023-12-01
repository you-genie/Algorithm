class Solution:
    def romanToInt(self, s: str) -> int:
        roman2int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        answer = 0
        
        reverse_s = s[::-1]
        for i, c in enumerate(reverse_s):
            c_num = roman2int[c]
            
            if i > 0 and roman2int[reverse_s[i-1]] > c_num:
                c_num = -c_num
                
            answer += c_num
            
        return answer