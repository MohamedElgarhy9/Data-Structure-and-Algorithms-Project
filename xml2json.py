#!/usr/bin/env python
# coding: utf-8

# In[ ]:


stack = []
lvl = 0
i = -1

def isOpening(word):
    return (word[0] == '<' and word[1] != '/' and word[-1] == '>')


def isClosing(word):
    return (word[0] == '<' and word[1] == '/' and word[-1] == '>')


def matching(opening, closing):
    return (opening == closing[0] + closing[2:])


def display(lst, lvl=0, opening='',last_block=False):
    if len(lst) == 1:
        if last_block:
            return lst[0]
        else:
            return (1 + lvl) * '  ' + '\"{}\" : '.format(opening[1:-1]) + '{ \n' + lst[0] + '\n'+(1 + lvl) * '  ' + ' }'

    equal = True
    tag = lst[0][:lst[0].find(':') + 1]

    for i in lst:

        if i[:lst[0].find(':') + 1] != tag:
            equal = False

    if equal:

        for i in range(len(lst)):

            if i != len(lst) - 1:
                lst[i] += ', \n'
            else:
                lst[i] += '\n'

        block = ''
        for ele in lst:
            block += ele.replace(tag.strip(), '')
        return (1 + lvl) * '  ' + '\"{}\" : '.format(opening[1:-1]) + '[ \n' + block + (1 + lvl) * '  ' + '] '

    else:
        for i in range(len(lst)):

            if i != len(lst) - 1:
                lst[i] += ', \n'
            else:
                lst[i] += '\n'

        block = ''
        for ele in lst:
            block += ele
        return (1 + lvl) * '  ' + '\"{}\" : '.format(opening[1:-1]) + '{ \n' + block + (1 + lvl) * '  ' + '} '


def xml2json(xml, word=None, opening=None):
    global stack
    global lvl
    global i
    last_block = False
    lvlitems = []
    block = ''
    while i < (len(xml) - 1):
        i += 1
        #         print('i : ',i)
        #         print('blocklist of level',len(stack),' : ',lvlitems)
        #         print('stack : ',stack)

        if isOpening(xml[i]):
            opening = xml[i]
            stack.append(xml[i])
            lvl += 1
            lvlitems.append(xml2json(xml, xml[i], opening))

        elif isClosing(xml[i]):
            v = stack.pop()
            lvl -= 1
            if block != '':
                return block
            else:
                if last_block:
                    last_block = False
                    return display(lvlitems, lvl, v,True)
                else:
                    return display(lvlitems, lvl, v)

        else:
            block = block + (lvl + 1) * '  ' + '\"{}\" : '.format(opening[1:-1]) + '\"{}\"'.format(xml[i])
            last_block = True
    return  display(lvlitems)[7:-4]+'}' 


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
    xml = []
    for i in range(len(l)):
        if l[i] == '': continue
        xml.append(l[i])

    return xml

def Json(xml):
    try:
        f = xml.read()
    except:
        f = xml
    global stack
    global lvl
    global i
    stack = []
    lvl = 0
    i = -1
    return xml2json(toList(f))

