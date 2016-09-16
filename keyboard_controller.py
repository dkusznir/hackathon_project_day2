import sys
import tty
import termios
from msvcrt import getch

def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)

while True:
    key = ord(getch())

    if key == 17:
        break
    elif key == 65:
        print "up arrow"
    elif key == 66:
        print "down arrow"
    elif key == 67:
        print "right arrow"
    elif key == 68:
        print "left arrow"
