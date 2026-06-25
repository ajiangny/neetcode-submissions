class Solution:
    def isValid(self, s: str) -> bool:
        """
        } //check if { is on top of stack pop off
        { //append
        [ //append
        ( //append
        """
        stack = []
        print(f"Testing: {repr(s)}")

        for i in range(len(s)):
            if s[i] == '[':
                stack.append('[')
            elif s[i] == '{':
                stack.append('{')
            elif s[i] == '(':
                stack.append('(')
            elif s[i] == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            elif s[i] == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop()
            elif s[i] == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
        
        if len(stack) > 0:
            return False
        else:
            return True

                