import pyperclip
from time import sleep
from chord_transpose_tools import chord_sub
from os import system


system('')
clear_screen = lambda: print(end="\033[2J")


print('Copy the original text (ctrl + c). Waiting.')
original_string = pyperclip.waitForNewPaste()
clear_screen()
msg = 'Enter the number of semitones to shift: '
while not (semitones := input(msg)).removeprefix('-').isdecimal():
    clear_screen()
    print('Only negative sign and numerals are allowed.')

clear_screen()
msg = 'Report the accidental to use: '
while not (accidental := input(msg)) in ('#', 'b'):
    clear_screen()
    print('Only allowed as accidental # or b')

pyperclip.copy(chord_sub(original_string, int(semitones), accidental))
clear_screen()
print('Transposition was performed.\n'
    'Transposed version was stored in the clipboard.\n'
    '(Use paste option or Ctrl + v)')
sleep(10)
