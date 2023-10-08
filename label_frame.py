from tkinter import *


def validate_entry(symbol):
    return symbol.isdecimal() or symbol == '.' or symbol == '-' or symbol == 'e'


class FrameLEB:

    def __init__(self, name_label, name_button, fr, func, args):
        self.label_frame = LabelFrame(fr)
        self.label = Label(self.label_frame, text=name_label, width=15, font=('Times 14'))
        self.entry = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"))
        self.button = Button(self.label_frame, text=name_button, font=('Times 14'), command=lambda: func(*args))
        self.label.pack(side=LEFT, ipadx=5, padx=5)
        self.entry.pack(side=LEFT, ipadx=5, padx=5)
        self.button.pack(side=LEFT, ipadx=5, padx=5)
        self.label_frame.pack(side=TOP, fill='both')

    def get(self):
        return self.entry.get()


class FrameLE:

    def __init__(self, name_label, fr):
        self.label_frame = LabelFrame(fr)
        self.label = Label(self.label_frame, text=name_label, width=15, font=('Times 14'))
        self.entry = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"))
        self.label.pack(side=LEFT, ipadx=5, padx=5)
        self.entry.pack(side=LEFT, ipadx=5, padx=5)
        self.label_frame.pack(side=TOP, fill='both')

    def get(self):
        return self.entry.get()


class Row:
    def __init__(self, name, fr):
        self.label_frame = LabelFrame(fr)
        self.entry_x = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"), width=13)
        self.entry_y = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"), width=13)
        self.entry_vx = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"), width=13)
        self.entry_vy = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"), width=13)
        self.entry_L = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"), width=13)
        self.entry_S = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"), width=13)
        self.entry_m = Entry(self.label_frame, validate="key", validatecommand=(fr.register(validate_entry), "%S"), width=13)
        self.entry_x.insert(END, '0')
        self.entry_vx.insert(END, '0')
        self.entry_L.insert(END, '0')
        self.entry_S.insert(END, '0')
        self.entry_y.insert(END, '0')
        self.entry_vy.insert(END, '0')
        self.entry_m.insert(END, '0')
        self.label = Label(self.label_frame, text=name, width=10, font=('Times 14'))
        self.label.pack(side=LEFT, ipadx=5, padx=5)
        self.entry_x.pack(side=LEFT, ipadx=5, padx=5)
        self.entry_y.pack(side=LEFT, ipadx=5, padx=5)
        self.entry_vx.pack(side=LEFT, ipadx=5, padx=5)
        self.entry_vy.pack(side=LEFT, ipadx=5, padx=5)
        self.entry_L.pack(side=LEFT, ipadx=5, padx=5)
        self.entry_S.pack(side=LEFT, ipadx=5, padx=5)
        self.entry_m.pack(side=LEFT, ipadx=5, padx=5)
        self.label_frame.pack(side=TOP, fill='both')
