# STACKS - Medium

# Given an encoded string, return its decoded string.

# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc.

class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []
        curr_num = 0
        curr_str = ''

        for ch in s:
            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)  # handle numbers > 9
            elif ch == '[':
                num_stack.append(curr_num)
                str_stack.append(curr_str)
                curr_num = 0
                curr_str = ''
            elif ch == ']':
                repeat = num_stack.pop()
                prev_str = str_stack.pop()
                curr_str = prev_str + curr_str * repeat
            else:
                curr_str += ch

        return curr_str
