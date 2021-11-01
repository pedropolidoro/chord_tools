import re
from note_transpose_tools  import note2num, num2note

with open('chord_regex.txt', 'r', encoding='UTF-8') as file_obj:
    chord_re = file_obj.read()

chord_re = re.compile(chord_re, re.X)

def cv_chord(match_obj : re.Match, dislocate, accidental='#'):
    """Performs the transposition of a single chord,
    dislocate represents the amount of semitones shifted."""
    
    fundamental, other, bass = match_obj.groups()
    # remove None values
    if not bass:
        bass = ''
    if not other:
        other = ''
    fundamental = (note2num(fundamental) + dislocate) % 12
    fundamental = num2note(fundamental, accidental)
    if bass:
        bass = (note2num(bass) + dislocate) % 12
        bass = num2note(bass, accidental)
        bass = '/' + bass # because regex remove the "/"
    return fundamental + other + bass

def chord_sub(string, dislocate, accidental='#'):
    """Transposes all the chords in a string
    that may contain more than just chords."""
    
    return chord_re.sub(lambda x: cv_chord(x, dislocate, accidental), string)
