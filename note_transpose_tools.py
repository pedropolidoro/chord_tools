notenames = 'C,,D,,E,F,,G,,A,,B'.split(',')
accidentals = {'b' : -1, '#'  : 1, 'x': 2, 'X' : 2, '♯': 1, '♭' : -1}

def note2num(note):

    number = notenames.index(note[0])
    if note[1:]:
        # When chord name has accidental.
        for accidental_simbol in note[1:]:
            number += accidentals[accidental_simbol]
    return number


def num2note(num, accidental='#'):

    if not (name := notenames[num]):
        # When musical note has accidental.
        name = notenames[num - accidentals[accidental]] + accidental
    return name
