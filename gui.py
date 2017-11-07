import tkinter as tk
# from gps_utils import *

class Example:
    def __init__(self):
        self.createWindow()

    def createWindow(self):
        self.root=tk.Tk()
        self.root.title("GPS Reader")
        self.canvas = tk.Canvas(self.root, borderwidth=0, background="#ffffff")
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.vsb = tk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.vsb.set)


        self.vsb.pack(side="right", fill="y")
        self.canvas.pack(side="left", fill="both", expand=True)
        self.canvas.create_window((0,0), window=self.frame, anchor="nw", 
                                  tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)

        # add menu items
        self.createMenu()

        # display welcome prompt
        self.displayText = ""
        self.printWelcomePrompt()
        # self.populate()

        # keep window open until user exit
        self.root.mainloop()

    def createMenu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        fileMenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Start", command=self.startConnection)
        fileMenu.add_command(label="Stop", command=self.endConnection)

        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self.frame.quit)

        editMenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Edit", menu=editMenu)
        editMenu.add_command(label="Clear", command=self.clearWindow)

        helpMenu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="About")

    def startConnection(self):
        self.clearWindow()
        continuousRead()

    def endConnection(self):
        msg = "Connection ended.\n" 
        msg += "File 'Start' to restart reading from your GPS\n" 
        msg += "File 'Exit' to exit this application\n" 
        self.printMessage(msg)

    def printWelcomePrompt(self):
        msg = "A dumb GPS program\n"
        msg += "File 'Start' to start reading from your GPS\n"
        msg += "File 'Stop' to stop a running connection\n"
        msg += "File 'Exit' to exit this application\n"
        tk.Label(self.frame, text=msg, anchor="w", justify="left", bg="#ffffff").grid(
                row=0, column=0, sticky="w, e")

    def printMessage(self, msg):
        self.clearWindow()
        self.displayText += msg
        tk.Label(self.frame, text=self.displayText, anchor="w", justify="left", bg="#ffffff").grid(
                row=0, column=0, sticky="w, e")

    def clearWindow(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.canvas, background="#ffffff")
        self.canvas.create_window((4,4), window=self.frame, anchor="nw", tags="self.frame")
        self.frame.bind("<Configure>", self.onFrameConfigure)
        self.displayText = ""

    def populate(self):
        # some fake data
        for row in range(100):
            tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1", 
                     relief="solid").grid(row=row, column=0)
            t="this is the second column for row %s" %row
            tk.Label(self.frame, text=t).grid(row=row, column=1)

    def onFrameConfigure(self, event):
        '''Reset the scroll region to encompass the inner frame'''
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))


    def startProgramTester():
        Example().pack(side="top", fill="both", expand=True)

   
# Example()