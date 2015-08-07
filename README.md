# entrance_counter

Script for RPi-based entrance counter.
Configuration file is ./config.py.

Each entrance and exit is detected via GPIO and logged in a file, total number of people inside is shown in a fullscreen window.

If the total number raises above the limit, the window switches to the red background.

The total is continuously saved in a separate file and reloaded at the next start.
