"""
Animation program. Back-on-forth, zigzag pattern until the user stops it by
pressing Ctrl-C.


"""
from time import sleep
from sys import exit

indent = 0  # How many spaces to indent.
indent_increasing = True  # Wheter the indentation is increasing or not

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        sleep(0.1)  # Pause before next line.

        if indent_increasing:
            # increase the number of spaces.
            indent += 1
            if indent == 20:
                # Change direction
                indent_increasing = False
        else:
            # Decrease the number of spaces:
            indent -= 1
            if indent == 0:
                # Change direction.
                indent_increasing = True
except KeyboardInterrupt:
    exit()
