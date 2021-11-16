import pyperclip
from time import sleep
from chord_transpose_tools import chord_sub
from os import system


system('')
clear_screen = lambda: print(end="\033[2J")


print('Copy the original text (ctrl + c). Waiting.') # 'Copie o texto original (Ctrl + c). Aguardando.' 
original_string = pyperclip.waitForNewPaste()
clear_screen()
msg = 'Enter the number of semitones to shift: ' # 'Informe o número de semitons a deslocar: '
while not (semitones := input(msg)).removeprefix('-').isdecimal():
    clear_screen()
    print('Only negative sign and numerals are allowed.') # 'Somente é permitido sinal de negativo e algarismos.'

clear_screen()
msg = 'Report the accidental to use: ' # 'Informe o acidente a utilizar: '
while not (accidental := input(msg)) in ('#', 'b'):
    clear_screen()
    print('Only allowed as accidental # or b') # 'Como acidente somente é permitido # ou b'

pyperclip.copy(chord_sub(original_string, int(semitones), accidental))
clear_screen()
print('Transposition was performed.\n' # 'Transposição realizada.\n'
    'Transposed version was stored in the clipboard.\n' # 'A versão transposta foi armazenada na área de transferência.\n'
    '(Use paste option or Ctrl + v)') # '(Utilize opção colar ou Ctrl + v)'
sleep(10)
