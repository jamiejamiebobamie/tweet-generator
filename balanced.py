"""checks a string to see if there are the same number of
closing and opening parentheses

what's the big-O notation way...
"""

def balanced(string):
    sum = 0
    for char in string:
        if char == '(':
            sum -= 1
        elif char == ')':
            sum += 1
        else:
            continue
    if sum == 0:
        return True
    else:
        return False

print(balanced("(((((titititjdjddjd1929393)))))"))



"""
OPENING = '('


def is_balanced(parentheses):
    stack = []
    for paren in parentheses:
        if paren == OPENING:
            stack.append(paren)
        else:
            try:
                stack.pop()
            except IndexError:  # too many closing parens
                return False
    return len(stack) == 0  # false if too many opening parens


is_balanced('((()))')  # => True
is_balanced('(()')  # => False
is_balanced('())')  # => False


-https://bradfieldcs.com/algos/stacks/balanced-parentheses/

_______
This method I believe is faster as it ends sometimes
without iterating through the entire string.

"""
