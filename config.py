limit = 530
fontsize = 500
log_dir = 'log'
fullscreen = False # if True then the title bar is hidden

# Bouncetime (in milliseconds) is the delay before accepting new input on the same channel.
# You can set up a default bouncetime and an individual bouncetime for each channel (optional).
default_bouncetime = 200

# Pin - GPIO pin number; effect - 'increase', 'decrease' or 'reset';
# bouncetime - bouncetime for this pin (if omitted, default_bouncetime is used)
pins = (
    # (pin, effect, bouncetime)
    (23, 'increase', 300),
    (16, 'decrease'),
    (25, 'reset')
)