#!/usr/bin/env python
""" Script for RPi-based entrance counter.
 Configuration file is ./config.py """

__author__ = 'Sergey Lutskovsky'
__contact__ = 'sergius.lutskovsky@gmail.com'

import sys
import os
import atexit
import RPi.GPIO as GPIO
from datetime import *

if sys.version_info[0] < 3:
    from Tkinter import *
else:
    from tkinter import *

from config import *


@atexit.register
def cleanup():
    GPIO.cleanup()
    total.close()


def change_value(*not_used_args):
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


def increase(not_used_arg):
    value.set(value.get() + 1)
    log('in')


def decrease(not_used_arg):
    value.set(value.get() - 1)
    log('out')


def reset(not_used_arg):
    value.set(0)
    log('reset')


def log(message):
    cur_time = datetime.now().replace(microsecond=0).isoformat(' ')
    line = '{};{}\n'.format(cur_time, message)
    logfile.write(line)


def setup_pins(pin, callback, bouncetime=default_bouncetime):
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    callback_func = globals()[callback]
    GPIO.add_event_detect(pin, GPIO.RISING, callback=callback_func, bouncetime=bouncetime)

try:
    with open('total') as total:
        initial = total.readline()
        initial = int(initial)
except (IOError, ValueError):
    initial = 0
finally:
    total = open('total', 'w+', 0)

GPIO.setmode(GPIO.BCM)

for settings in pins:
    setup_pins(*settings)

root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.overrideredirect(fullscreen)
root.geometry("%dx%d+0+0" % (w, h))

value = IntVar()
value.trace('w', change_value)
label = Label(root, font=("Helvetica", fontsize), textvariable=value)
label.place(relx=0.5, rely=0.5, anchor=CENTER)

value.set(initial)

today = date.today().isoformat()
logfile_name = today + '.log'
logfile_name = os.path.join(log_dir, logfile_name)
logfile = open(logfile_name, 'a+', 0)

root.mainloop()
