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

# print(evalRevPolishNotation(["1","2","+","3","*","4","-"]))
# print(evalRevPolishNotation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
# print(evalRevPolishNotation(["0","3","/"]))



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

#print(generateParenthesis(3))


# DAILY TEMPERATURES
# You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.
# Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a
# future day. If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.
# Ex:
# Input: temperatures = [30,38,30,36,35,40,28]
#
# Output: [1,4,1,2,1,0,0]
def dailyTemperatures(temperatures: List[int]) -> List[int]:
    result = []
    for i in range(len(temperatures) - 1):
        counter = 0
        found_warmer = False
        for j in range(i + 1, len(temperatures)):
            counter += 1
            if temperatures[j] > temperatures[i]:
                found_warmer = True
                break

        if found_warmer:
            result.append(counter)
        else:
            result.append(0)

    return result

#use monotonic stack (push )
def dailyTemperaturesEfficient(temperatures: List[int]) -> List[int]:
    stack = [] # keep tuples of index and temperature: (temp, ind)
    result = [0] * len(temperatures)

    for i in range(len(temperatures)):
        while stack and temperatures[i] > stack[-1][0]: #get temp from pair
            temp, ind = stack.pop()
            result[ind] = i - ind
        stack.append((temperatures[i], i))
    return result

# print(dailyTemperaturesEfficient([30,38,30,36,35,40,28]))
# print(dailyTemperaturesEfficient([23,22,21]))


# CAR FLEET
# There are n cars traveling to the same destination on a one-lane highway.
# You are given two arrays of integers position and speed, both of length n.
# position[i] is the position of the ith car (in miles)
# speed[i] is the speed of the ith car (in miles per hour)
# The destination is at position target miles.
# A car can not pass another car ahead of it. It can only catch up to another car and then drive at the same speed as the car ahead of it.
# A car fleet is a non-empty set of cars driving at the same position and same speed. A single car is also considered a car fleet.
# If a car catches up to a car fleet the moment the fleet reaches the destination, then the car is considered to be part of the fleet.
# Return the number of different car fleets that will arrive at the destination.
#
# Example 1:
# Input: target = 10, position = [1,4], speed = [3,2]
# Output: 1
def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    pos_speed_array = []
    stack = []

    for i in range(len(position)):
        pos_speed_array.append((position[i], speed[i]))

    # sorted merged array by position descending to start the parsing from the first car
    # the bigger the position, the closer is the target
    pos_speed_array.sort(key = lambda x: x[0], reverse=True)

    for i in range(len(pos_speed_array)):
        stack.append((target - pos_speed_array[i][0]) / pos_speed_array[i][1])
        # in this case the current added vehicle will enter the fleet of the one before him
        if len(stack) > 1 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)

# print(carFleet(10, [1, 4], [3, 2]))
# print(carFleet(10, [4, 1, 0, 7], [2, 2, 1, 1]))





# LARGEST RECTANGLE IN HISTOGRRAM
# You are given an array of integers heights where heights[i] represents the height of a bar. The width of each bar is 1.
# Return the area of the largest rectangle that can be formed among the bars.
# Note: This chart is known as a histogram.
#
# Ex:
# Input: heights = [7,1,7,2,2,4]
# Output: 8
def largestRectangleArea(heights: List[int]) -> int:
    max_area = 0

    for i in range(len(heights)):
        min_height = heights[i]
        for j in range(i+1, len(heights)):
            min_height = min(min_height, heights[j])
            current_area = (j - i + 1) * min_height
            max_area = max(max_area, current_area)

    return max_area

def largestRectangleAreaEfficient(heights: List[int]) -> int:
    max_area = 0
    stack = [] # array of pairs of index and its height

    for i in range(len(heights)):
        start = i
        while stack and stack[-1][1] > heights[i]:
            ind, height = stack.pop()
            max_area = max(max_area, (i - ind) * height) #calculate max potential area for the popped height
            start = ind

        stack.append((start, heights[i]))

    for i, height in stack:
        max_area = max(max_area, height * (len(heights) - i))

    return max_area


#def largestRectangleAreaEfficient2()

print(largestRectangleAreaEfficient([7,1,7,2,2,4]))