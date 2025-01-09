
'''
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

    Input: s = "()"

    Output: true

Example 2:

    Input: s = "()[]{}"

    Output: true

Example 3:

    Input: s = "(]"

    Output: false

Example 4:

    Input: s = "([])"

    Output: true'''

def Solution(expression):
    stack = []
    for char in expression:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if char == ')' and stack[-1] != '(':
                return False
            if char == '}' and stack[-1] != '{':
                return False
            if char == ']' and stack[-1] != '[':
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == "__main__":
    assert(Solution(expression = "()") == True)
    assert(Solution(expression = "()[]{}") == True)