from tkinter import *
import json

class mainApp(Tk):
    dataFile = './data.json'
    count = 0

    def __init__(self):
        super().__init__()
        self.initWindow()
        self.initLayout()        
        self.getTotal()

    def initWindow(self):
        self.title("Library Book Information")
        self.configure(
            bg="white",
            
            )
        self.geometry('720x576')
        self.resizable(False, False)

    def addBook(self):

        def submitBook():
            id = self.id.get()
            author = self.author.get()
            name = self.bookName.get()
            date = self.issueDate.get()

            self.count += 1
            
            self.idListBox.insert(self.count, id)
            self.authorListBox.insert(self.count, author)
            self.bookNameListBox.insert(self.count, name)
            self.issueDateListBox.insert(self.count, date)

            self.addWindow.destroy()

        self.id = StringVar()
        self.author = StringVar()
        self.bookName = StringVar()
        self.issueDate = StringVar()

        self.addWindow = Toplevel(self)
        self.addWindow.title("Add book")
        self.addWindow.config(
            bg="white"
        )

        # LABEL WIDGETS
        idLbl = Label(self.addWindow, text="ID")
        authorLbl = Label(self.addWindow, text="Author")
        bookNameLbl = Label(self.addWindow, text="Book Name")
        issueDateLbl = Label(self.addWindow, text="Issue Date")

        for widget in [idLbl, authorLbl, bookNameLbl, issueDateLbl]:
            widget.configure(
                anchor="w",
                font=("Noto Sans Condensed", 18),
                bg="white",
            )

        # ENTRY WIDGETS
        idEntry = Entry(self.addWindow, textvariable=self.id)
        authorEntry = Entry(self.addWindow, textvariable=self.author)
        bookNameEntry = Entry(self.addWindow, textvariable=self.bookName)
        issueDateEntry = Entry(self.addWindow, textvariable=self.issueDate)

        for widget in [idEntry, authorEntry, bookNameEntry, issueDateEntry]:
            widget.configure(
                font=("Noto Sans Condensed", 16), bg="white",
                background="white",
                relief='groove'
            )

        # BUTTON WIDGETS
        submitBtn = Button(self.addWindow, text="Submit", command=submitBook)

        # LABELS GRID
        idLbl.grid(row=0, column=0, padx=6, pady=6)
        authorLbl.grid(row=1, column=0, padx=6, pady=6)
        bookNameLbl.grid(row=2, column=0, padx=6, pady=6)
        issueDateLbl.grid(row=3, column=0, padx=6, pady=6)

        # ENTRY GRID
        idEntry.grid(row=0, column=1, padx=6, pady=6)
        authorEntry.grid(row=1, column=1, padx=6, pady=6)
        bookNameEntry.grid(row=2, column=1, padx=6, pady=6)
        issueDateEntry.grid(row=3, column=1, padx=6, pady=6)

        # BUTTON GRID
        submitBtn.grid(row=4, column=0, columnspan=2, padx=6, pady=6, sticky="nsew")
        submitBtn.configure(
            font=("Noto Sans", 16),
            relief='flat',
            bd=0

        )

    def initLayout(self):

        self.totalStringVar = StringVar()

        # LABELS / STYLES
        headerLbl = Label(self, text="Library Book Information", anchor="center", bg="black", fg="white", justify="center", font=("Noto Sans Bold", 36))
        idLbl = Label(self, text="ID")
        authorLbl = Label(self, text="Author")
        bookNameLbl = Label(self, text="Book Name")
        issueDateLbl = Label(self, text="Issue Date")
        totalLbl = Label(self, textvariable=self.totalStringVar, font=("Noto Sans Light", 14), bg="white")

        for widget in [idLbl, authorLbl, bookNameLbl, issueDateLbl]:
            widget.configure(
                anchor="center",
                font=("Noto Sans Condensed", 18),
                bg="white"
            )

        # LISTBOX / STYLES
        self.idListBox = Listbox(self, bg="grey")
        self.authorListBox = Listbox(self, bg="grey")
        self.bookNameListBox = Listbox(self, bg="grey")
        self.issueDateListBox = Listbox(self, bg="grey")

        for widget in [self.idListBox, self.authorListBox, self.bookNameListBox, self.issueDateListBox]:
            widget.configure(
                background="white",
                font=("Noto Sans Condensed", 16),
                relief="flat",                
            )

        # BUTTONS / STYLES
        addBtn = Button(self, text="Add Book", font=("Noto Sans", 14), command=self.addBook)
        removeBtn = Button(self, text="Remove Book", font=("Noto Sans", 14))
        
        for widget in [addBtn, removeBtn]:
            widget.configure(
                bd=0,
                background="black",
                fg="white",
                activebackground="white",
                activeforeground="black"
            )

        # LABELS PLACE
        headerLbl.place(x=0,y=0,width=720,height=72)
        idLbl.place(x=0,y=70,width=144,height=45)
        authorLbl.place(x=140,y=70,width=144,height=45)
        bookNameLbl.place(x=280,y=70,width=216,height=45)
        issueDateLbl.place(x=490,y=70,width=229,height=45)
        totalLbl.place(x=440,y=510,width=270,height=52)

        # LISTBOX PLACE
        self.idListBox.place(x=0,y=60,width=140,height=385)
        self.authorListBox.place(x=140,y=60,width=141,height=386)
        self.bookNameListBox.place(x=280,y=60,width=211,height=386)
        self.issueDateListBox.place(x=490,y=60,width=229,height=386)

        # BUTTONS PLACE
        addBtn.place(x=10,y=510,width=207,height=54)
        removeBtn.place(x=220,y=510,width=207,height=54)

        with open(self.dataFile, 'r') as temp:
            data = json.load(temp)

            for book in data.values():
                count = 0
                for element, value in book.items():
                    if element == "id":
                        self.idListBox.insert(count, value)
                    elif element == "author":
                        self.authorListBox.insert(count, value)
                    elif element == "name":
                        self.bookNameListBox.insert(count, value)
                    elif element == "issued":
                        self.issueDateListBox.insert(count, value)
                count += 1
    
    def getTotal(self):
        with open(self.dataFile, 'r') as temp:
            data = json.load(temp)

            for book in data.items():
                self.count += 1

            self.totalStringVar.set(f"Total number of books: {self.count}")

if __name__ == "__main__":
    win = mainApp()
    win.mainloop()