"""Here are your instructions:

Starting with the project you created at the end of the last lesson, add components to the existing framework so that:
•When the areas occupied by Frame 1 or Frame 2 are clicked with mouse button 1, the program should print which frame was
clicked and the X and Y coordinates (relative to the Frame).
•Frame 3 should contain an Entry and a Text widget. When the button now labeled "Open" is clicked, the content
of the Entry should be used as a file name, and the content of the file (if any) displayed in the Text widget.
•The Entry and Text widgets should completely fill Frame 3 and continue to do so even as the application window is resize.
•The color of the text displayed in Frame 3's Text widget should change appropriately when the "Red," "Blue," "Green,"
or "Black" buttons are clicked.

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
 |    Red   |   Blue   |  Green   |  Black   |   Open   |
 +----------+----------+----------+----------+----------+                                               """
 
 ###############################################################################################################################################################################################################################################################################################################################
 
 from tkinter import *
x=1
while x>6:
    x=x+1

ALL = N+S+W+E
def handler(event):
    print ("Red Frame clicked at", event.x, event.y)
    
def handler2(event):
    print ("Green Frame clicked at", event.x, event.y)
    
class Application(Frame):


    def createWidgets(self):
        top_frame = Frame(self)
        self.text_in = Entry(top_frame)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        for r in range(4):
            self.rowconfigure(r, weight=1)
            Button(self, text="Row {0}".format(r)).grid(row=r, column=0, sticky=W+E)
        self.rowconfigure(5, weight=1)
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c+1)).grid(row=5, column=c, sticky=W+E)

        f = Frame(self, bg="red")
        f.grid(row=0, column=0, rowspan=2, columnspan=2, sticky=ALL)
        f.bind("<Button-1>",handler)
        g = Frame(self, bg= "blue")
        g.grid(row=0, column=2, rowspan=4, columnspan=3, sticky=ALL)

        h = Frame(self, bg= "green")
        h.grid(row=2, column=0, rowspan=2, columnspan=2, sticky=ALL)
        h.bind("<Button-1>",handler2)
root = Tk()
app = Application(master=root)                
app.mainloop()
