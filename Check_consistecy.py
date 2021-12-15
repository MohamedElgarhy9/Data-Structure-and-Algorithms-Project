# importing "double-ended queue"
from collections import deque

i = -1
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
def isOpening(word):
    return (word[0] == '<' and word[1] != '/' and word[-1] == '>')

# check if it's closing tag
def isClosing(word):
    return (word[0] == '<' and word[1] == '/' and word[-1] == '>')

# Check matching
def matching(opening, closing):
    return (opening == closing[0] + closing[2:])

# This function takes a string and rearrange it in a list 
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
    s = ''
    balanced = None
    mistakes = 0
    while (i < (len(xml) - 1)):
        i = i + 1
        # check if it's opening tag
        if isOpening(xml[i]):
            stack.push(xml[i])  # append to stack
            s += '\n' + xml[i]
        # check if it's closing tag
        elif isClosing(xml[i]):
            if stack.is_empty():
                mistakes += 1
                if balanced == None:
                    balanced = False
                s += '\n' + xml[i] + ' <== this closing tag has no opening'

            elif matching(stack.peek(), xml[i]):
                stack.pop()
                s += '\n' + xml[i]

            elif not matching(stack.peek(), xml[i]):
                mistakes += 1

                if balanced == None:
                    balanced = False

                last = stack.pop()
                if matching(stack.peek(), xml[i]):
                    s += '\n<== the closing tag of {} is missing here'.format(last)
                    s += '\n' + xml[i]
                    stack.pop()
                elif matching(last, xml[i+1]):
                    s += '\n' + xml[i] + ' <== this closing tag is not in the right place'
                    stack.push(last)

                else:
                    s += '\n' + xml[i] + ' <== the right closing tag should be that of {}'.format(last)

        else:
                s += '\n' + xml[i]
                if i+1<(len(xml) - 1):
                    if not isClosing(xml[i+1]):
                        if not isOpening(xml[i+1]):
                            pass
                        else:
                            s += '\n  <== the closing tag of {} is missing here'.format(stack.peek())
                            mistakes += 1
                            stack.pop()
                else:
                    s += '\n  <== the closing tag is missing here'
                    mistakes += 1
                    
    # nothing in stack means all is well balanced
    if stack.is_empty():

        if balanced == None:
            balanced = True
    else:
        if balanced == None:
            balanced = False
        while not stack.is_empty():
            tag = stack.pop()
            s += '\n<== the closing tag of {} is missing here'.format(tag)
            mistakes += 1
    if balanced:
        str="All Balanced!"
    else: str="Not Balanced!"

    return str +'\nThere are {} errors'.format(mistakes) + '\n' + s

