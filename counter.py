#!/usr/bin/env python
"""
"""

__author__ = 'Sergey Lutskovsky'
__contact__ = 'sergius.lutskovsky@gmail.com'

import sys
import atexit
import importlib

if(sys.version_info[0]<3):
    from Tkinter import *
else:
    from tkinter import *

class Counter:
    def __init__(self, config):
        self.config = importlib.import_module(config)

        root=Tk()

        self.value = IntVar()
        self.value.trace('w', self.change_value)
        self.label = Label(root, textvariable=self.value)
        self.label.pack()

        self.value.set(0)


        in_1=Button(root,text='in 1', command=self.enter)
        in_1.pack()

        out_1=Button(root,text='out 1', command=self.exit)
        out_1.pack()

        reset=Button(root,text='reset', command=self.reset)
        reset.pack()

        root.mainloop()

    def change_value(self, name, index, mode):
        if self.value.get() < 0:
            self.value.set(0)

        if self.value.get() > self.config.limit:
            self.label.config(fg='black', bg='red')
        else:
            self.label.config(fg='white', bg='black')

    def enter(self):
        self.value.set(self.value.get() + 1)

    def exit(self):
        self.value.set(self.value.get() - 1)

    def reset(self):
        self.value.set(0)

counter = Counter('config')
