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
            temp = []
            with open(self.dataFile, 'r') as tempFile:
                temp = json.load(tempFile)

            id = self.__add_id.get()
            author = self.__add_author.get()
            name = self.__add_bookName.get()
            date = self.__add_issueDate.get()

            self.count += 1

            self.idListBox.insert(self.count, int(id))
            self.authorListBox.insert(self.count, author)
            self.bookNameListBox.insert(self.count, name)
            self.issueDateListBox.insert(self.count, date)

            temp.append({
                'id': int(id),
                'author': str(author),
                'name': str(name),
                'date': str(date)
            })

            with open(self.dataFile, 'w') as jsonFile:
                json.dump(
                    temp, jsonFile, indent=4, separators=(',',': ')
                )

            self.addWindow.destroy()
            self.getTotal()

        self.__add_id = IntVar()
        self.__add_author = StringVar()
        self.__add_bookName = StringVar()
        self.__add_issueDate = StringVar()

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
        idEntry = Entry(self.addWindow, textvariable=self.__add_id)
        authorEntry = Entry(self.addWindow, textvariable=self.__add_author)
        bookNameEntry = Entry(self.addWindow, textvariable=self.__add_bookName)
        issueDateEntry = Entry(
            self.addWindow, textvariable=self.__add_issueDate)

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
        submitBtn.grid(row=4, column=0, columnspan=2,
                       padx=6, pady=6, sticky="nsew")
        submitBtn.configure(
            font=("Noto Sans", 16),
            relief='flat',
            bd=0
        )

    def removeBook(self):

        def submitRemove():
            for id in self.idListBox.get(0, END):
                if id == int(self.__remove_id.get()):
                    index = self.idListBox.get(0, END).index(
                        int(self.__remove_id.get()))

                    self.idListBox.delete(index)
                    self.authorListBox.delete(index)
                    self.bookNameListBox.delete(index)
                    self.issueDateListBox.delete(index)

            self.removeWindow.destroy()
            self.getTotal()

        self.__remove_id = IntVar()

        self.removeWindow = Toplevel(self)
        self.removeWindow.title("Remove book")
        self.removeWindow.configure(
            bg="white",
            bd=0
        )

        idLbl = Label(self.removeWindow, text="ID", anchor="w",
                      font=("Noto Sans Condensed", 18), bg="white",)
        idEntry = Entry(self.removeWindow, textvariable=self.__remove_id, font=(
            "Noto Sans", 16), relief='groove')
        submitBtn = Button(self.removeWindow, text="Submit",
                           command=submitRemove)

        idLbl.grid(row=0, column=0, padx=6, pady=6)
        idEntry.grid(row=0, column=1, padx=6, pady=6)
        submitBtn.grid(row=1, column=0, columnspan=2,
                       sticky='nsew', padx=6, pady=6)
        submitBtn.configure(
            font=("Noto Sans", 16),
            relief='flat',
            bd=0
        )

    def initLayout(self):

        self.totalStringVar = StringVar()

        # LABELS / STYLES
        headerLbl = Label(self, text="Library Book Information", anchor="center",
                          bg="black", fg="white", justify="center", font=("Noto Sans Bold", 36))
        idLbl = Label(self, text="ID")
        authorLbl = Label(self, text="Author")
        bookNameLbl = Label(self, text="Book Name")
        issueDateLbl = Label(self, text="Issue Date")
        totalLbl = Label(self, textvariable=self.totalStringVar,
                         font=("Noto Sans Light", 14), bg="white")

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
        addBtn = Button(self, text="Add Book", font=(
            "Noto Sans", 14), command=self.addBook)
        removeBtn = Button(self, text="Remove Book", font=(
            "Noto Sans", 14), command=self.removeBook)

        for widget in [addBtn, removeBtn]:
            widget.configure(
                bd=0,
                background="black",
                fg="white",
                activebackground="white",
                activeforeground="black"
            )

        # LABELS PLACE
        headerLbl.place(x=0, y=0, width=720, height=72)
        idLbl.place(x=0, y=70, width=144, height=45)
        authorLbl.place(x=140, y=70, width=144, height=45)
        bookNameLbl.place(x=280, y=70, width=216, height=45)
        issueDateLbl.place(x=490, y=70, width=229, height=45)
        totalLbl.place(x=440, y=510, width=270, height=52)

        # LISTBOX PLACE
        self.idListBox.place(x=0, y=120, width=140, height=385)
        self.authorListBox.place(x=140, y=120, width=141, height=386)
        self.bookNameListBox.place(x=280, y=120, width=211, height=386)
        self.issueDateListBox.place(x=490, y=120, width=229, height=386)

        # BUTTONS PLACE
        addBtn.place(x=10, y=510, width=207, height=54)
        removeBtn.place(x=220, y=510, width=207, height=54)

        with open(self.dataFile, 'r') as temp:
            data = json.load(temp)

            for book in data:
                print(book)
                countBox = 0
                for element, value in book.items():
                    if element == "id":
                        self.idListBox.insert(countBox, value)
                    elif element == "author":
                        self.authorListBox.insert(countBox, value)
                    elif element == "name":
                        self.bookNameListBox.insert(countBox, value)
                    elif element == "issued":
                        self.issueDateListBox.insert(countBox, value)
                countBox += 1

                self.count += 1

    def getTotal(self):
        self.totalStringVar.set(
            f"Total number of books: {len(self.idListBox.get(0, END))}")


if __name__ == "__main__":
    win = mainApp()
    win.mainloop()
