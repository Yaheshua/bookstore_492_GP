from tkinter import *
from LogInPage import *
import Message
#import ttk
from tkinter import ttk


class BuyBook(object):
    def __init__(self, root, color, font, dbConnection, userInfo):

        self.root = root
        self.color = color
        self.font = font
        self.dbConnection = dbConnection
        self.userName = userInfo['userName']

        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.height = self.screen_height * 3 / 4
        self.width = self.screen_width * 3 / 4

        self.gui_init()

    def gui_init(self):

        self.root.title("Buy new Book")
        self.root.resizable(width=False, height=FALSE)

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

        topFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 1 / 10,
            width=self.width)

        topFrame.grid_propagate(0)
        topFrame.pack(side=TOP, expand=True, fill=BOTH)

        downFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 9 / 10,
            width=self.width)

        downFrame.grid_propagate(0)
        downFrame.pack(side=TOP, expand=True, fill=BOTH)

        self.__printBooks(downFrame)
        self.__printTitle(topFrame)

    def __printTitle(self, frame):

        titleLable = Label(
            frame, text='Available Books', font=self.font, bg=self.color)
        titleLable.place(relx=0.5, rely=0.5, anchor='center')

