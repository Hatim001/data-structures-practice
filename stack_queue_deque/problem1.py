"""
Balanced Parentheses Check

Problem Statement

Given a string of opening and closing parentheses, check whether it's balanced. We have 3 types 
of parentheses: round brackets: (), square brackets: [], and curly brackets: {}. 
Assume that the string doesn't contain any other character than these, no spaces words or numbers. 
As a reminder, balanced parentheses require every opening parenthesis to be closed in the reverse order opened. 
For example '([])' is balanced but '([)]' is not.

You can assume the input string has no spaces.
"""

from stack import Stack


def balance_check(s):

    if not s:
        return False

    stack = Stack()
    brackets = {')': '(', '}': '{', ']': '['}

    for ele in s:
        if not stack.isEmpty() and brackets.get(ele) == stack.peek():
            stack.pop()
        else:
            stack.push(ele)

    return bool(stack.isEmpty())
