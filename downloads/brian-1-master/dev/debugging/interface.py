'''
Tk interface
From http://www.pythonware.com/library/tkinter/introduction/hello-again.htm

Idea: extend the Parameters class to generate interfaces with load/save abilities
Maybe use configparser? (and take care of units)

Suggestion:
* use wxpython
* editors: wxglade, boa, pythoncard
'''
from Tkinter import *


class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, text="QUIT", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)

        self.hi_there = Button(frame, text="Hello", command=self.say_hi)
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print "hi there, everyone!"

root = Tk()

app = App(root)

root.mainloop()
