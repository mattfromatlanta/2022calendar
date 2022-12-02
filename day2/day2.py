file = open("day2_input.txt", "r")
data = file.read().split("\n")


def getPlayValue(p_play):
    if p_play == 'X':
        return 1
    elif p_play == 'Y':
        return 2
    elif p_play == 'Z':
        return 3
    else:
        return 0


def getWinValue(p_them, p_us):
    # rock A,X paper B,Y scissors C,Z
    if p_them == 'A':
        if p_us == 'X':
            return 3
        elif p_us == 'Y':
            return 6
        elif p_us == 'Z':
            return 0
        else:
            return 0
    elif p_them == 'B':
        if p_us == 'X':
            return 0
        elif p_us == 'Y':
            return 3
        elif p_us == 'Z':
            return 6
        else:
            return 0
    elif p_them == 'C':
        if p_us == 'X':
            return 6
        elif p_us == 'Y':
            return 0
        elif p_us == 'Z':
            return 3
        else:
            return 0
    else:
        return 0


def getScore(p_them, p_us):
    score = 0
    score += getPlayValue(p_us)
    score += getWinValue(p_them, p_us)
    return score


def getUs(p_them, p_play):
    # X lose, Y draw, and Z win.
    if p_them == 'A':
        if p_play == 'X':
            return 'Z'
        elif p_play == 'Y':
            return 'X'
        elif p_play == 'Z':
            return 'Y'
        else:
            return -1
    elif p_them == 'B':
        if p_play == 'X':
            return 'X'
        elif p_play == 'Y':
            return 'Y'
        elif p_play == 'Z':
            return 'Z'
        else:
            return -1
    elif p_them == 'C':
        if p_play == 'X':
            return 'Y'
        elif p_play == 'Y':
            return 'Z'
        elif p_play == 'Z':
            return 'X'
        else:
            return -1
    else:
        return -1


def getRevisedScore(p_them, p_play):
    p_us = getUs(p_them, p_play)
    return getScore(p_them, p_us)


final_score = 0
for datum in data:
    line = datum.split(" ")
    them = line[0]
    us = line[1]
    final_score += getScore(them, us)
revised_score = 0
for datum in data:
    line = datum.split(" ")
    them = line[0]
    play = line[1]
    revised_score += getRevisedScore(them, play)

print('final score: ', final_score)
print('revised score: ', revised_score)
print("fin")