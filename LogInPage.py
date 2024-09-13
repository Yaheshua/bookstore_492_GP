from tkinter import *
import AdminPage
import UserPage
import Message


class LoginFrame(object):
    '''
    This Class handles the LogIn action.
    '''
    def __init__(self, parent, root, height, width, side, color, dbConnection,
                 adminCredentials):

        self.parent = parent
        self.root = root
        self.height = height
        self.width = width
        self.side = side
        self.font = ('Times', 12, 'roman')
        self.color = color
        self.dbConnection = dbConnection
        self.adminCredentials = adminCredentials

        self.gui_init()

    def gui_init(self):

        self.frame = Frame(
            self.root,
            cursor='hand1',
            bg=self.color,
            height=self.height,
            width=self.width,
            relief=RAISED,
            bd=5)

        self.frame.grid_propagate(0)
        self.frame.pack(expand=True, side=self.side, fill=BOTH)
        #creating labels

        frame1 = Frame(
            self.frame,
            cursor='hand1',
            bg=self.color,
            height=self.height / 3,
            width=self.width * 2 / 3)
        frame1.grid_propagate(0)
        frame1.pack(expand=True, fill=BOTH)
        frame1.place(relx=0.5, rely=0.5, anchor='center')

        self.userNameLabel = Label(
            frame1, text="UserName", font=self.font, bg=self.color)
        self.userNameLabel.grid(row=0, column=0, sticky=E, padx=2, pady=2)

        self.passwordLabel = Label(
            frame1, text="Password", font=self.font, bg=self.color)
        self.passwordLabel.grid(row=1, column=0, sticky=E, padx=2, pady=2)

        #creating entries
        self.userNameEntry = Entry(frame1, width=25, font=self.font)
        self.userNameEntry.grid(row=0, column=1, sticky=W, padx=2, pady=2)

        self.passwordEntry = Entry(frame1, width=25, show='*', font=self.font)
        self.passwordEntry.grid(row=1, column=1, sticky=W, padx=2, pady=2)

        #creating login button
        self.loginButton = Button(frame1, text="Login", font=self.font)
        self.loginButton.bind("<Button-1>", self.__loginAction)
        self.loginButton.grid(row=2, column=0, columnspan=2, padx=2, pady=2)

