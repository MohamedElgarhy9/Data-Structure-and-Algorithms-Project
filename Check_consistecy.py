# importing "double-ended queue"
from collections import deque


# class for making a stack
class Stack:
    def __init__(self):
        self.c = deque()  # initializing class object as a deque

    # function for appending stack
    def push(self, value):
        self.c.append(value)

    # function to pop out latest value
    def pop(self):
        return self.c.pop()

    # returns the size of stack
    def size(self):
        return len(self.c)

    # returns if stack is empty or not
    def is_empty(self):
        return len(self.c) == 0


# Function to check whether two characters are opening and closing of same type.
def pair(opening, closing):
    if opening == '{' and closing == '}':
        return True
    elif opening == '[' and closing == ']':
        return True
    elif opening == '(' and closing == ')':
        return True
    elif opening == '<' and closing == '>':
        return True
    elif opening == '"' and closing == '"':
        return True
    else:
        return False


# function for balancing parentheses
def check_cosistency(exp):
    stack = Stack()
    # loop to iterate over string
    for i in exp:
        # check if it's opening bracket
        if i == '(' or i == '[' or i == '{' or i == '<' or i == '"':
            stack.push(i)  # append to stack
        # check if it's closing bracket
        elif i == ')' or i == ']' or i == '}' or i == '>' or i == '"':
            popped = ""
            if not stack.is_empty():
                stack.pop()
            elif (stack.is_empty()) or (not pair(i, popped)):
                print("Not Balanced!")
                return
    # nothing in stack means all is well/balanced ;)
    if stack.is_empty():
        print("All Balanced!")
    else:
        print("Not Balanced!")


# parsing a string value (expression) for balance check
check_cosistency("[ksdk+(){}<.sdkjkff>()]")
