#!/usr/bin/env python
"""
"""

__author__ = 'Sergey Lutskovsky'
__contact__ = 'sergius.lutskovsky@gmail.com'

import sys
import atexit
import importlib
from datetime import *

if(sys.version_info[0]<3):
    from Tkinter import *
else:
    from tkinter import *

import config

totalfile = 'total'

def change_value(name, index, mode):
    val = value.get()

    if val > config.limit:
        label.config(fg='black', bg='red')
    else:
        label.config(fg='white', bg='black')
    total.write(str(val))


def enter():
    value.set(value.get() + 1)
    log('in')

def exit():
    value.set(value.get() - 1)
    log('out')

def reset():
    value.set(0)
    log('reset')

def log(message):
    time = datetime.now().isoformat(' ')
    line = '{};{}\n'.format(time, message)
    logfile.write(line)


try:
    with open(totalfile) as total:
        initial = total.readline()
        initial = int(initial)
except IOError, ValueError:
    initial = 0
finally:
    total = open(totalfile, 'w+', 0)

root=Tk()

value = IntVar()
value.trace('w', change_value)
label = Label(root, textvariable=value)
label.pack()

value.set(initial)

today = date.today().isoformat()
logfile = open(today + '.log', 'a+', 0)

in_1=Button(root,text='in 1', command=enter)
in_1.pack()

in_2=Button(root,text='in 2', command=enter)
in_2.pack()

out_1=Button(root,text='out 1', command=exit)
out_1.pack()

reset=Button(root,text='reset', command=reset)
reset.pack()

root.mainloop()