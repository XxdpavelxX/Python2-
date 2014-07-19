"""Here are your instructions:

Write a GUI-based program to build a window layout as shown below. When the frame is resized, the buttons should 
stay the same height and expand sideways. Frame 1 and Frame 2 should always be the same height and width as each other, 
and Frame 3 should be half as wide again as they are (i.e. 150% wider, as shown below).  Labeling each Frame is 
optional / good exercise.

 +---------------------+--------------------------------+

|                     |                                |
 |                     |                                |
 |                     |                                |
 |      Frame 1        |                                |
 |                     |                                |
 |                     |                                |
 |                     |                                |
 +---------------------+               Frame 3          |
 |                     |                                |
 |                     |                                |
 |                     |                                |
 |     Frame 2         |                                |
 |                     |                                |
 |                     |                                |
 +----------+----------+----------+----------+----------+
 | Button 1 | Button 2 | Button 3 | Button 4 | Button 5 |
 +----------+----------+----------+----------+----------+                            """
 
 ####################################################################################################################################################################################################################################################################################################################
 
 from tkinter import *
x=1
while x>6:
    x=x+1

ALL = N+S+W+E

class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        for r in range(4):
            self.rowconfigure(r, weight=1)
            Button(self, text="Row {0}".format(r)).grid(row=r, column=0, sticky=W+E)
        self.rowconfigure(0, weight=1)
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c+1)).grid(row=5, column=c, sticky=W+E)
           

        f = Frame(self, bg="red")
        f.grid(row=0, column=0, rowspan=2, columnspan=2, sticky=ALL)
        g = Frame(self, bg= "blue")
        g.grid(row=0, column=2, rowspan=4, columnspan=3, sticky=ALL)
        h = Frame(self, bg= "green")
        h.grid(row=2, column=0, rowspan=2, columnspan=2, sticky=ALL)
root = Tk()
app = Application(master=root)                
app.mainloop()
