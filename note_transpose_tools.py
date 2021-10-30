notenames = 'C,,D,,E,F,,G,,A,,B'.split(',')
accidentals = {'b' : -1, '#'  : 1, 'x': 2, 'X' : 2, '♯': 1, '♭' : -1}

def note2num(note):

    number = notenames.index(note[0])
    if not note[1:]:
        return number
    for x in note[1:]:
        number += accidentals[x]
    return number


def num2note(num, accidental='#'):

    if not (name := notenames[num]):
        name = notenames[num - accidentals[accidental]] + accidental
    return name
