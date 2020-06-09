from tkinter import *
import time


# creating class for window.
class Window(Frame):
    # Define setting upon initialization . Here you can specify
    def __init__(self, window_title=None, master=None, name=None, link=None):
        self.frame = None
        self.panel = None
        self.name = name
        self.link = link
        # Parameter that you want to send through the Frame class.
        Frame.__init__(self, master)
        self.master = master
        self.master.title(window_title)
        self.init_window(self.name, self.link)
        self.mainloop()

    # Function for the creation of Initial window of GUI
    def init_window(self, name, link):
        # changing the title of our widget
        # self.master.title('Surat Kmart')

        # packing the frame
        self.pack(fill=BOTH, expand=1)
        self.title = Label(self, text='lets extract Detail of link.',
                           font="Verdana 10 bold", fg="blue", bg='yellow')
        self.title.place(x=155, y=5)

        # Labelling rows and column.
        self.qrimage = Canvas(self, bg="blue")
        self.qrimage.grid(padx=10, pady=30, column=0, row=0, columnspan=2, rowspan=2)

        self.linklilst = Listbox(self)
        self.linklilst.grid(pady=30, row=0, column=2, sticky='NESW')
        self.linklilst.delete(0, END)
        for row in link:
            self.linklilst.insert(END, row)
        self.sb1 = Scrollbar(self)
        self.sb1.grid(pady=30, row=0, column=3, sticky='NESW')
        self.linklilst.configure(xscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.linklilst.yview)

        self.linkname = Listbox(self)
        self.linkname.grid(pady=30, row=0, column=4, sticky='NESW')
        self.linkname.delete(0, END)
        for row in name:
            self.linkname.insert(END, row)
        self.sb2 = Scrollbar(self)
        self.sb2.grid(pady=30, row=0, column=5, sticky='NESW')
        self.linkname.configure(xscrollcommand=self.sb2.set)
        self.sb2.configure(command=self.linkname.yview)

        # self.searchname = StringVar()
        # self.searchtab = Entry(self, textvariable=self.searchname)
        # self.searchtab.grid(row=1, column=2, ipadx=10, ipady=3, sticky='NWE')


def main():
    window = Tk()
    # window.geometry("500x500")
    # window.resizable(False, False)
    app = Window('surya', window)


if __name__ == '__main__':
    main()
