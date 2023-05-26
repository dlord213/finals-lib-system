from tkinter import *
import json

class mainApp(Tk):
    dataFile = './data.json'

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
        idListBox = Listbox(self, bg="grey")
        authorListBox = Listbox(self, bg="grey")
        bookNameListBox = Listbox(self, bg="grey")
        issueDateListBox = Listbox(self, bg="grey")

        for widget in [idListBox, authorListBox, bookNameListBox, issueDateListBox]:
            widget.configure(
                background="white",
                font=("Noto Sans Condensed", 16),
                relief="flat",                
            )

        # BUTTONS / STYLES
        addBtn = Button(self, text="Add Book", font=("Noto Sans", 14))
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
        idListBox.place(x=0,y=120,width=140,height=385)
        authorListBox.place(x=140,y=120,width=141,height=386)
        bookNameListBox.place(x=280,y=120,width=211,height=386)
        issueDateListBox.place(x=490,y=120,width=229,height=386)

        # BUTTONS PLACE
        addBtn.place(x=10,y=510,width=207,height=54)
        removeBtn.place(x=220,y=510,width=207,height=54)

        with open(self.dataFile, 'r') as temp:
            data = json.load(temp)

            for book in data.values():
                count = 0
                for element, value in book.items():
                    if element == "id":
                        idListBox.insert(count, value)
                    elif element == "author":
                        authorListBox.insert(count, value)
                    elif element == "name":
                        bookNameListBox.insert(count, value)
                    elif element == "issued":
                        issueDateListBox.insert(count, value)
                count += 1
    
    def getTotal(self):
        with open(self.dataFile, 'r') as temp:
            data = json.load(temp)
            count = 0

            for book in data.items():
                count += 1

            self.totalStringVar.set(f"Total number of books: {count}")

if __name__ == "__main__":
    win = mainApp()
    win.mainloop()