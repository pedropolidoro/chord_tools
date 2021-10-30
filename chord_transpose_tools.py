import re
from note_transpose_tools  import note2num, num2note

with open('chord_regex.txt', 'r', encoding='UTF-8') as file_obj:
    chord_re = file_obj.read()

chord_re = re.compile(chord_re, re.X)

def cv_chord(match_obj, dislocate):
    fundamental, other, bass = match_obj.groups()
    # remove None values
    if not bass:
        bass = ''
    if not other:
        other = ''
    fundamental = (note2num(fundamental) + dislocate) % 12
    fundamental = num2note(fundamental)
    if bass:
        bass = (note2num(bass) + dislocate) % 12
        bass = num2note(bass)
        bass = '/' + bass # because regex remove the "/"
    return fundamental + other + bass

def chord_sub(string, dislocate):
    return chord_re.sub(lambda x: cv_chord(x, dislocate), string)
