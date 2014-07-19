from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        top_frame = Frame(self)
        self.text_in = Entry(top_frame)
        self.text_oh=Entry(top_frame)
        self.text_oh.pack(side=LEFT) 
        self.text_in.pack(side=LEFT)
        self.label = Label(top_frame, text="Output label")
        self.label.pack()
            
        top_frame.pack(side=TOP)
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        self.handleb = Button(bottom_frame, text="Convert", command=self.handle)
        self.handleb.pack(side=LEFT)

    def handle(self):
        text = self.text_in.get()
        operation = self.text_oh.get()
        try:
            output = float(text)+float(operation)

        except:
            output = "***ERROR***"
        self.label.config(text=output)
            
root = Tk()
app = Application(master=root)
app.mainloop()
