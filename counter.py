#!/usr/bin/env python
""" My work ;)))
Dedicated to my lovely wife"""

__author__ = 'Sergey Lutskovsky'
__contact__ = 'sergius.lutskovsky@gmail.com'

import sys
import atexit
import RPi.GPIO as GPIO
from datetime import *

if sys.version_info[0]<3:
    from Tkinter import *
else:
    from tkinter import *

from config import *

def change_value(name, index, mode):
    val = value.get()

    if val > limit:
        label.config(fg='black', background='red')
        root.config(background='red')
    else:
        label.config(fg='white', background='black')
        root.config(background='black')

    total.seek(0)
    total.write(str(val))
    total.truncate()


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
    with open('total') as total:
        initial = total.readline()
        initial = int(initial)
except (IOError, ValueError):
    initial = 0
finally:
    total = open('total', 'w+', 0)

#for pin in enter_pins:
#    GPIO.add_event_detect(pin, GPIO.RISING, callback=enter())


root=Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(1)
root.geometry("%dx%d+0+0" % (w, h))

value = IntVar()
value.trace('w', change_value)
label = Label(root, font=("Helvetica", fontsize), textvariable=value)
label.place(relx=0.5, rely=0.5, anchor=CENTER)

value.set(initial)

today = date.today().isoformat()
logfile = open(today + '.log', 'a+', 0)

buttons_window = Toplevel()

in_1=Button(buttons_window,text='in 1', command=enter)
in_1.pack()

in_2=Button(buttons_window,text='in 2', command=enter)
in_2.pack()

out_1=Button(buttons_window,text='out 1', command=exit)
out_1.pack()

reset=Button(buttons_window,text='reset', command=reset)
reset.pack()

root.mainloop()