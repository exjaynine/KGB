import time

from gimpfu import *

#This opens up the command prompt on windows. Why? I have no idea
#But at least it DOES what I intended for it to do. GIMP python-fu doesn't seem to
#like argument-less functions. But I'll keep experimenting to see what else works.
def TheTime(img, layer):
    gimp.message("HI THERE!")



register(
        "PrintCurrentTime",
        "Print the current time",
        "Print the current time",
        "Me",
        "Me",
        "2001",
        "<Image>/File/Timer",
        "*",
        [],
        [],
        TheTime)

main()
