#Valid Parentheses
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
# -Every open bracket is closed by the same type of close bracket.
# -Open brackets are closed in the correct order.
# -Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.
from typing import List


def isValid(s: str) -> bool:
    stack = []

    closeOpenMap = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    if s and s[0] in closeOpenMap:
        return False

    for ch in s:
        if ch in closeOpenMap.values():
            stack.append(ch)
        elif ch in closeOpenMap and stack:
            if stack.pop() != closeOpenMap[ch]:
                return False
        else:
            return False

    return len(stack) == 0

#
# print(isValid("([{}])"))
# print(isValid("[(])"))


# MINIMUM STACK
#Design a stack class that supports the push, pop, top, and getMin operations.
#
# -MinStack() initializes the stack object.
# -void push(int val) pushes the element val onto the stack.
# -void pop() removes the element on the top of the stack.
# -int top() gets the top element of the stack.
# -int getMin() retrieves the minimum element in the stack.
#
# Each function should run in O(1) time.
class MinStack:
    def __init__(self):
        self._stack = []
        self._minStack = []

    def push(self, val: int) -> None:
        self._stack.append(val)

        if not self._minStack or val <= self._minStack[-1]:
            self._minStack.append(val)

    def pop(self) -> None:
        if self._stack[-1] == self._minStack[-1]:
            self._minStack.pop()
        self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._minStack[-1]


# EVALUATE REVERSE POLISH NOTATION
#
# You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
# Return the integer that represents the evaluation of the expression.
# -The operands may be integers or the results of other operations.
# -The operators include '+', '-', '*', and '/'.
# -Assume that division between integers always truncates toward zero.
# EX:
# Input: tokens = ["1", "2", "+", "3", "*", "4", "-"]
# Output: 5
# Explanation: ((1 + 2) * 3) - 4 = 5
def evalRevPolishNotation(tokens: List[str]) -> int:
    stack = []

    for token in tokens:
        if token in "+-*/":
            b = stack.pop()
            a = stack.pop()

            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                #truncation towards zero
                stack.append(int(a / b))
        else:
            stack.append(int(token))

    return stack[0]

print(evalRevPolishNotation(["1","2","+","3","*","4","-"]))
print(evalRevPolishNotation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(evalRevPolishNotation(["0","3","/"]))


#GENEREATE PARANTHESES
# You are given an integer n. Return all well-formed parentheses strings that you can generate with
# n pairs of parentheses.
# Ex:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
def generateParenthesis(n: int) -> List[str]:
    # add open par if open < n
    # add closing par if closed < open
    # valid if open == closed == n
    stack = []
    solution = []

    def backtrack(open, closed):
        if open == closed == n:
            solution.append("".join(stack))
            return
        if open < n:
            stack.append('(')
            backtrack(open + 1, closed)
            stack.pop()
        if closed < open:
            stack.append(')')
            backtrack(open, closed + 1)
            stack.pop()

    backtrack(0, 0)
    return solution

print(generateParenthesis(3))