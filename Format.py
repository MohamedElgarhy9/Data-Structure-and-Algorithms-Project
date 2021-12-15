# importing "double-ended queue"
from collections import deque

i = -1
level = -1
xml = []


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
        if self.is_empty():
            return None
        return self.c[-1]


# check if it's an oppening tag
def is_Opening(word):
    return (word[0] == '<' and word[1] != '/' and word[-1] == '>')


# check if it's a closing tag
def is_Closing(word):
    return (word[0] == '<' and word[1] == '/' and word[-1] == '>')


# Check matching
def matching(opening, closing):
    return (opening == closing[0] + closing[2:])


def is_String(word):
    return ((not is_Opening(word)) and (not is_Closing(word)))


# This function takes a string and rearranges it in a list
def toList(input_string):
    file = ''

    for i in input_string:
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


# function which format an unformatted code
def format(input_string):
    global i
    global level
    stack = Stack()
    toList(input_string)
    s = ''
    while (i < (len(xml) - 1)):
        i = i + 1
        if is_Opening(xml[i]):
            stack.push(xml[i])
            level = level + 1
            s+='    ' * level + xml[i] + '\n'
        elif is_Closing(xml[i]):
            if not (stack.is_empty() and matching(stack.peek(), xml[i])):
                stack.pop()
                level = level - 1
                s+='    ' * (level + 1) + xml[i] + '\n'
        elif is_String(xml[i]):
            s+='    ' * (level + 1) + xml[i] + '\n'
    return s
    
