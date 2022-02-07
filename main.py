from tkinter import *
from tkinter import filedialog
from xml2json import *
from Check_consistecy import check_cosistency
from Format import format
from sys import exit
from compression import huffmancode
import networkx as nx
from graph import edges
import matplotlib.pyplot as plt



data = ''
out = ''
i=0
json = None

def openFile():
    global data
    xml_1file = filedialog.askopenfilename(
        initialdir="F:\new term\DATASTR PROJECT\py\comxml",
        title="xml gui",
        filetypes=(("Text Files", "*.xml"),)
    )
    label_file_explorer.configure(text="File Opened: " + xml_1file)
    xml_1file = open(xml_1file)
    data = xml_1file.read()
    textbox_1.insert(END, data)
    xml_1file.close()


def convert_to_json():
    global out
    global json
    json = True
    out = Json(data)
    Output.delete(1.0, END)
    Output.insert(END, out)


def isConsistent():
    check = check_cosistency(data)
    Output.delete(1.0, END)
    Output.insert(END, check)


def formatxml():
    global out
    global json
    json = False
    out = format(data)
    Output.delete(1.0, END)
    Output.insert(END, out)

def graphit():
    out = edges(data)
    G = nx.DiGraph()
    G.add_edges_from(out)
    nx.draw_networkx(G, with_labels=True)
    plt.show()
    Output.delete(1.0, END)
    Output.insert(END, out)


def comp():
    xml_1file = filedialog.askopenfilename(
        initialdir="F:\new term\DATASTR PROJECT\py\comxml",
        title="xml gui",
        filetypes=(("Text Files", "*.xml"),)
    )
    with open(xml_1file, "r") as myfile:
        data_a = myfile.read()
    textfile = open("a_file.txt", "w")

    textfile.write(data_a)
    textfile.close()

    textfile.close()
    h = huffmancode('a_file.txt')
    h.compress()
    Output.delete(1.0, END)
    Output.insert(END, 'The file is compressed successfully!')


def savetout():
    global i
    i+=1
    if json:
        out_f = open("out{}.json".format(i), "w")
        out_f.write(out)
        out_f.close()
    else:
        out_f = open("out{}.xml".format(i), "w")
        out_f.write(out)
        out_f.close()


ws = Tk()
ws.title("gui_1")
ws.geometry("400x700")
textbox_1 = Text(ws, width=47, height=15)

Button(
    ws,
    text="choose file",
    command=openFile
).grid(row=0, column=0, columnspan=4, pady=2, padx=5)

label_file_explorer = Label(ws,
                            text="XML File",
                            width=50, height=4,
                            fg="blue")
label_file_explorer.grid(row=1, column=0, columnspan=4, padx=5, pady=2)

textbox_1.grid(row=2, column=0, columnspan=4, pady=2, padx=5)

Output = Text(ws, height=15,
              width=47,
              bg="light cyan")

Button1 = Button(
    ws,
    text="to json",
    command=convert_to_json
)
Button1.grid(row=3, column=0, pady=2, padx=5)

Button2 = Button(
    ws,
    text="check consistency",
    command=isConsistent
)
Button2.grid(row=3, column=1, pady=2, padx=5)
Button3 = Button(
    ws,
    text="format",
    command=formatxml
)
Button3.grid(row=3, column=2, pady=2, padx=5)
Button4 = Button(
    ws,
    text="compress",
    command=comp
)
Button4.grid(row=3, column=3, pady=2, padx=5)

Output.grid(row=4, column=0, columnspan=4, pady=2)

exit = Button(ws,
              text="Exit",
              command=exit)
exit.grid(row=5, column=2, columnspan=1, pady=2)

save = Button(ws,
              text="Save",
              command=savetout)
save.grid(row=5, column=0, columnspan=2, pady=2)

graph = Button(ws,
              text="Graph",
              command=graphit)
graph.grid(row=5, column=1, columnspan=2,  pady=2)

ws.mainloop()