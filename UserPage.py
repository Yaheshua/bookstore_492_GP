from tkinter import *
#import ttk
from tkinter import ttk
import BuyBook
import BookInformationPage
import Message


class UserPage(object):
    def __init__(self, root, color, font, dbConnection, userInfo):

        for child in root.winfo_children():
            child.destroy()

        self.root = root
        self.color = color
        self.font = font
        self.dbConnection = dbConnection
        self.userInfo = userInfo

        self.screen_width = self.root.winfo_screenwidth() * 3 / 4
        self.screen_height = self.root.winfo_screenheight() * 3 / 4

        self.gui_init()

    def gui_init(self):

        self.up_frame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            height=self.screen_height / 8,
            width=self.screen_width)
        self.up_frame.grid_propagate(0)
        self.up_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.down_frame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            height=self.screen_height * 7 / 8,
            width=self.screen_width)
        self.down_frame.grid_propagate(0)
        self.down_frame.pack(side=TOP, expand=True, fill=BOTH)

        self.profileFrame = ProfileFrame(self.up_frame, self.screen_width / 2,
                                         self.screen_height / 8, self.color,
                                         self.font, self.userInfo)

        self.logoutFrame = LogOutFrame(
            self.root, self.up_frame, self.screen_width / 2,
            self.screen_height / 8, self.color, self.font, self.dbConnection)

        self.booksInfoFrame = BuyedBooks(
            self.down_frame, self.screen_width, self.screen_height * 7 / 8,
            self.color, self.font, self.dbConnection, self.userInfo)


class ProfileFrame(object):
    def __init__(self, root, width, height, color, font, userInfo):

        self.root = root
        self.width = width
        self.height = height
        self.color = color
        self.font = font
        self.userInfo = userInfo

        self.gui_init()

    def gui_init(self):

        self.frame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            bd=5,
            relief=RAISED,
            width=self.width,
            height=self.height)
        self.frame.pack(expand=True, side=LEFT, fill=BOTH)
        self.frame.grid_propagate(0)

        profile_info = self.extract_profile()
        self.profileLabel = Label(
            self.frame, text=profile_info, font=self.font, bg=self.color)
        self.profileLabel.place(relx=0.5, rely=0.5, anchor='center')

    def extract_profile(self):

        userInfo = "\n".join(self.userInfo.values())
        return userInfo


class LogOutFrame(object):
    def __init__(self, parent, root, width, height, color, font, dbConnection):

        self.root = root
        self.width = width
        self.height = height
        self.color = color
        self.font = font
        self.parent = parent
        self.dbConnection = dbConnection

        self.gui_init()

    def gui_init(self):

        self.frame = Frame(
            self.root,
            cursor='hand1',
            bd=5,
            relief=RAISED,
            bg=self.color,
            width=self.width,
            height=self.height)
        self.frame.pack(side=LEFT, expand=True, fill=BOTH)
        self.frame.grid_propagate(0)

        self.logout_button = Button(
            self.frame, text="LogOut", font=self.font, borderwidth=5)
        self.logout_button.place(relx=0.5, rely=0.5, anchor='center')

        self.logout_button.bind("<Button-1>", self.__logOutAction)

    def __logOutAction(self, event):

        self.dbConnection.close()
        for child in self.parent.winfo_children():
            child.destroy()
        self.parent.destroy()
