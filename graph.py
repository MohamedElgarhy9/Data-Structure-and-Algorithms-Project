import networkx as nx

def toUsers(xml_file):
    file = ''

    for i in xml_file:
        file = file + str(i)

    l = []
    s = ''
    t = ''
    for i in file:
        t += i
        if i == '<':
            s = i

        elif i == '>':
            s += i
            if s == "</user>":
                l.append(t.replace('\n', '').strip())
                t = ''
            s = ''
        else:
            s += i

    return l
def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub)

def edges(xml):
    x = toUsers(xml)
    dic = dict()
    source = []
    target = []
    for txt in x:
        indices = list(find_all(txt,'<id>'))
        key = txt[indices[0]+4]
        values = []
        for i in indices[1:]:
            values.append(txt[i+4])
        dic[key]=values

    for i in dic:
        for j in dic[i]:
            target.append(i)
            source.append(j)
    ss=list(zip(source, target))
    return ss
