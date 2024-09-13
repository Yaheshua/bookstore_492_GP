from tkinter import *
#import ttk
from tkinter import ttk
import AddReview
import Message


class BookInformation(object):
    def __init__(self, root, color, dbConnection, bookName, userInfo):

        self.root = root
        self.color = color
        self.bookName = bookName
        self.dbConnection = dbConnection
        self.userName = userInfo['userName']
        self.font = ('Times', 12, 'roman')
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.height = self.screen_height / 3
        self.width = self.screen_width / 3
        self.gui_init()

    def gui_init(self):

        self.root.title(self.bookName)
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

        upFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 9 / 10,
            width=self.width)

        upFrame.grid_propagate(0)
        upFrame.pack(side=TOP, expand=True, fill=BOTH)

        upLeftFrame = Frame(
            upFrame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 9 / 10,
            width=self.width / 3,
            relief=RAISED,
            bd=5)
        upLeftFrame.grid_propagate(0)
        upLeftFrame.pack(side=LEFT, expand=True, fill=BOTH)

        upRightFrame = Frame(
            upFrame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 9 / 10,
            width=self.width * 2 / 3,
            relief=RAISED,
            bd=5)
        upRightFrame.grid_propagate(0)
        upRightFrame.pack(side=LEFT, expand=True, fill=BOTH)

        downFrame = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height / 10,
            width=self.width)
        downFrame.grid_propagate(0)
        downFrame.pack(side=TOP, expand=True, fill=BOTH)

        self.__initBookInfo(upLeftFrame)
        self.__initReviews(upRightFrame)
        self.__initAddReviewButton(downFrame)

    def __initBookInfo(self, frame):

        book_information = self._getBookInformation()

        bookProfileLabel = Label(
            frame,
            text=book_information,
            font=self.font,
            bg=self.color,
            fg='red')
        bookProfileLabel.place(relx=0.5, rely=0.5, anchor='center')

