class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            print(c, stack)
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if not stack:
                    return False
                opening = stack.pop()
                if opening == '(' and c != ')':
                    return False
                if opening == '{' and c != '}':
                    return False
                if opening == '[' and c != ']':
                    return False
        return len(stack) == 0