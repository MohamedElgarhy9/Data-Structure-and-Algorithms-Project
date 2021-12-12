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
    
    # returns the top element of the stack
    def peek(self):
        if self.isEmpty():
            raise Exception("Stack empty!")
        return self.container[-1]  

i = -1
xml = []

# check if oppening tag
def isOpening(word):
    return (word[0] == '<' and word[1] != '/' and word[-1] == '>')

# check if closing tag
def isClosing(word):
    return (word[0] == '<' and word[1] == '/' and word[-1] == '>')

# Check matching
def matching(opening, closing):
    return (opening == closing[0] + closing[2:])

# This function takes a file.txt and rearrange it in a list 
def toList(xml_file):
    file = ''

    for i in xml_file:
        file = file + str(i)

    l = []
    s = ''
    for i in file:
        if i == '<':
            l.append(s.replace('\n', '').strip())
            s = i
        elif i == '>':
            s += i
            l.append(s.replace('\n', '').strip())
            s = ''
        else:
            s += i

    for i in range(len(l)):
        if l[i] == '':
            continue
        xml.append(l[i])

    return xml

# function for ckecking balance 
def check_cosistency(xml_file):
    global i
    stack = Stack()
    toList(xml_file)
    # loop to iterate over string
    while (i < (len(xml) - 1)):
        i = i + 1
        # check if it's opening bracket
        if isOpening(xml[i]):
            stack.push(xml[i])  # append to stack
        # check if it's closing bracket
        elif isClosing(xml[i]):
            if not (stack.is_empty() and matching(stack.peek(), xml[i])):
                stack.pop()
            elif (stack.is_empty()) or (not matching(stack.peek(), xml[i])):
                print("Not Balanced!")
                return
    # nothing in stack means all is well balanced
    if stack.is_empty():
        print("All Balanced!")
    else:
        print("Not Balanced!")
