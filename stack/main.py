#Valid Parentheses
# You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
# The input string s is valid if and only if:
# -Every open bracket is closed by the same type of close bracket.
# -Open brackets are closed in the correct order.
# -Every close bracket has a corresponding open bracket of the same type.
# Return true if s is a valid string, and false otherwise.
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