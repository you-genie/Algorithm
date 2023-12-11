class Solution:
    def isValid(self, s: str) -> bool:
        def match(c1: str, c2: str) -> bool:
            matches = ['()', '[]', '{}']
            for m in matches:
                if c1+c2 == m:
                    return True
            return False

        stack, ready_stack = list(s), []
        while stack:
            c = stack.pop()
            if c in ')]}':
                ready_stack.append(c)
            else:
                if (not ready_stack) or (not match(c, ready_stack.pop())):
                    return False
        
        return not ready_stack