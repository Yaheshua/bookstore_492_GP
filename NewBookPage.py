from tkinter import *
import Message

#creating the new book page class and corresponding functions & links
class NewBook(object):
    def __init__(self, root, color, dbConnection):

        self.root = root
        self.color = color
        self.dbConnection = dbConnection
        self.font = ('Times', 14, 'roman')

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.height = self.screen_height / 3
        self.width = self.screen_width / 3

        self.gui_init()

  
#initializing the GUI components
    def gui_init(self):

        self.root.title("Add new book page")
        self.root.resizable(width=False, height=False)

        self.frame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            height=self.height,
            width=self.width,
            relief=RAISED,
            bd=5)
        self.frame.pack(side=TOP, expand=True, fill=BOTH)
        self.frame.grid_propagate(0)

        self.topFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 4 / 5,
            width=self.width * 4 / 5,
        )

        self.topFrame.grid_propagate(0)
        self.topFrame.pack(expand=True, fill=BOTH)
        self.topFrame.place(relx=0.5, rely=0.5, anchor='center')

        self.bookNameLable = Label(
            self.topFrame, text="BookName", font=self.font, bg=self.color)
        self.bookNameLable.grid(row=1, column=0, sticky=W, padx=2, pady=2)

        self.bookAuthorLabel = Label(
            self.topFrame, text="Author", font=self.font, bg=self.color)
        self.bookAuthorLabel.grid(row=2, column=0, sticky=W, padx=2, pady=2)

        self.bookGenreLabel = Label(
            self.topFrame, text="Genre", font=self.font, bg=self.color)
        self.bookGenreLabel.grid(row=3, column=0, sticky=W, padx=2, pady=2)

        self.bookYearLabel = Label(
            self.topFrame,
            text="Published Year",
            font=self.font,
            bg=self.color)
        self.bookYearLabel.grid(row=4, column=0, sticky=W, padx=2, pady=2)

        self.bookStockLabel = Label(
            self.topFrame, text="Stock", font=self.font, bg=self.color)
        self.bookStockLabel.grid(row=5, column=0, sticky=W, padx=2, pady=2)

        self.bookPriceLabel = Label(
            self.topFrame, text="Price", font=self.font, bg=self.color)
        self.bookPriceLabel.grid(row=6, column=0, sticky=W, padx=2, pady=2)
