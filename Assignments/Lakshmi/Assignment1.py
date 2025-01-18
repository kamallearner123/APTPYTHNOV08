
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

<<<<<<< Updated upstream
def Solution(expression):
    # Stack to keep track of opening brackets
    stack = []
    # Dictionary to map closing brackets to their corresponding opening brackets
    bracket_map = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_map:
            # Pop from stack if it's not empty; otherwise, use a dummy value
            top_element = stack.pop() if stack else '#'
            # Check if the mapping matches the top element
            if bracket_map[char] != top_element:
                return False
        else:
            # Push opening brackets onto the stack
            stack.append(char)

    # If the stack is empty, all brackets were matched correctly
    return not stack


if __name__ == "__main__":
    assert(Solution(expression = "()") == True)
    assert(Solution(expression = "()[]{}") == True)
=======
class c1:
    pass

Version = "1.1: Date: 09/09/2021"
def Solution(expression):
    print("Solution funciton is getting called with expression = ", expression)

print("Mudule name = ", __name__)
if __name__ == "__main__": # If Assignment1.py is run directly, then only below code will run
    Solution(expression = "()") == True
    Solution(expression = "()[]{}") == True
>>>>>>> Stashed changes
