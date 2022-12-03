file = open("day2_input.txt", "r")
data = file.read().split("\n")

PLAY_VALUES = {
    "X": 1,
    "Y": 2,
    "Z": 3
}

MATCH_VALUES = {
    "AX": 3,
    "AY": 6,
    "AZ": 0,
    "BX": 0,
    "BY": 3,
    "BZ": 6,
    "CX": 6,
    "CY": 0,
    "CZ": 3
}

US_VALUES = {
    "AX": "Z",
    "AY": "X",
    "AZ": "Y",
    "BX": "X",
    "BY": "Y",
    "BZ": "Z",
    "CX": "Y",
    "CY": "Z",
    "CZ": "X"
}


def getPlayValue(p_play):
    return PLAY_VALUES[p_play]


def getWinValue(p_them, p_us):
    return MATCH_VALUES[p_them + p_us]


def getScore(p_them, p_us):
    score = 0
    score += getPlayValue(p_us)
    score += getWinValue(p_them, p_us)
    return score


def getUs(p_them, p_play):
    return US_VALUES[p_them + p_play]


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
