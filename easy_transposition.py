import pyperclip
from time import sleep
from chord_transpose_tools import chord_sub
from os import system
import languages.msg_english as msg


system('')
clear_screen = lambda: print(end="\033[2J")


print(msg.ctrl_c)
original_string = pyperclip.waitForNewPaste()
clear_screen()
while not (semitones := input(msg.num_semitones)).removeprefix('-').isdecimal():
    clear_screen()
    print(msg.fail_number)

clear_screen()
while not (accidental := input(msg.what_accidental)) in ('#', 'b'):
    clear_screen()
    print(msg.accidental_fail)

pyperclip.copy(chord_sub(original_string, int(semitones), accidental))
clear_screen()
print(msg.ctrl_v)
sleep(10)
