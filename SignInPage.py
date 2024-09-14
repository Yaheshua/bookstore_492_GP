from tkinter import *
from LogInPage import *
import Message

#Creating sign in page class
class SignInPage(object):
    def __init__(self, parent, root, height, width, side, color, dbConnection):

        self.parent = parent
        self.root = root
        self.height = height
        self.width = width
        self.side = side
        self.color = color
        self.dbConnection = dbConnection
        self.font = ('Times', 14, 'roman')

        self.gui_init()

  
#initializing the GUI for the sign in page
    def gui_init(self):

        self.topFrame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            height=self.height,
            width=self.width,
            relief=RAISED,
            bd=5)
        self.topFrame.pack(side=self.side, expand=True, fill=BOTH)
        self.topFrame.grid_propagate(0)
        #self.bottomFrame = Frame(master)
        #self.bottomFrame.pack(side=BOTTOM, fill=X)

        #creating labels

        int_frame = Frame(
            self.topFrame,
            cursor='hand1',
            bg=self.color,
            height=self.height * 4 / 5,
            width=self.width * 4 / 5)
        int_frame.grid_propagate(0)
        int_frame.pack(expand=True, fill=BOTH)
        int_frame.place(relx=0.5, rely=0.5, anchor='center')

        self.userNameLabel = Label(
            int_frame, text="UserName", font=self.font, bg=self.color)
        self.userNameLabel.grid(row=1, column=0, sticky=W, padx=2, pady=2)

        self.firstNameLabel = Label(
            int_frame, text="FirstName", font=self.font, bg=self.color)
        self.firstNameLabel.grid(row=2, column=0, sticky=W, padx=2, pady=2)

        self.lastNameLabel = Label(
            int_frame, text="LastName", font=self.font, bg=self.color)
        self.lastNameLabel.grid(row=3, column=0, sticky=W, padx=2, pady=2)

        self.emailLabel = Label(
            int_frame, text="Email", font=self.font, bg=self.color)
        self.emailLabel.grid(row=4, column=0, sticky=W, padx=2, pady=2)

        self.passwordLabel = Label(
            int_frame, text="Password", font=self.font, bg=self.color)
        self.passwordLabel.grid(row=5, column=0, sticky=W, padx=2, pady=2)

        self.bankingCardLabel = Label(
            int_frame, text="Banking Card Nr", font=self.font, bg=self.color)
        self.bankingCardLabel.grid(row=6, column=0, sticky=W, padx=2, pady=2)
