notenames = 'C,,D,,E,F,,G,,A,,B'.split(',')
accidentals = {'b' : -1, '#'  : 1, 'x': 2, 'X' : 2}

def note2num(note):
    number = notenames.index(note[0])
    if not note[1:]:
        return number
    for x in note[1:]:
        number += accidentals[x]
    #number %= 12
    return number

def num2note(num, accidental='#'):
    # num %= 12
    # assert accidental in ('b', '#')
    # assert 0 <= num < 12
    if not (name := notenames[num]):
        name = notenames[num - accidentals[accidental]] + accidental
    return name
