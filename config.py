__author__ = 'sergey'

limit = 5
fontsize = 500
log_dir = 'log'
fullscreen = False # if True window title bar is hidden

numbering_mode = GPIO.BCM # GPIO.BCM or GPIO.BOARD

# Bouncetime (in milliseconds) is the delay before accepting new input on the same channel.
# You can set up a single default bouncetime and individual bouncetime for single channels (optional).
default_bouncetime = 200

# Pin - number according to numbering_mode; effect - 'increase', 'decrease' or 'reset';
# bouncetime - bouncetime for this pin (if omitted, default_bouncetime is used)
pins = (
    # (pin, effect, bouncetime)
    (23, 'increase', 300),
    (16, 'decrease'),
    (25, 'reset')
)