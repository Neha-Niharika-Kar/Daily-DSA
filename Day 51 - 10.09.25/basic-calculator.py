# STACKS - Hard

# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result of the evaluation.
# You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        num = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch in "+-":
                result += sign * num
                num = 0
                sign = 1 if ch == "+" else -1

            elif ch == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1

            elif ch == ")":
                result += sign * num
                num = 0
                result *= stack.pop()
                result += stack.pop() 

        return result + sign * num
