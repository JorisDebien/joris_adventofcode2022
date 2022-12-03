total_score = 0
opposing_plays = []
outcomes = []
your_plays = []

opposing_rock = "A"
opposing_paper = "B"
opposing_scissors = "C"

your_rock = "X"
your_paper = "Y"
your_scissors = "Z"

rock_score = 1
paper_score = 2
scissors_score = 3

win_score = 6
draw_score = 3
lose_score = 0

outcome_lose = "X"
outcome_draw = "Y"
outcome_win = "Z"


def select_plays(opposing_plays, outcomes):
    i = 0
    while i < len(opposing_plays):
        if outcomes[i] == outcome_lose:
            if opposing_plays[i] == opposing_rock:
                your_plays.append(your_scissors)
            elif opposing_plays[i] == opposing_paper:
                your_plays.append(your_rock)
            elif opposing_plays[i] == opposing_scissors:
                your_plays.append(your_paper)
        elif outcomes[i] == outcome_draw:
            if opposing_plays[i] == opposing_rock:
                your_plays.append(your_rock)
            elif opposing_plays[i] == opposing_paper:
                your_plays.append(your_paper)
            elif opposing_plays[i] == opposing_scissors:
                your_plays.append(your_scissors)
        elif outcomes[i] == outcome_win:
            if opposing_plays[i] == opposing_rock:
                your_plays.append(your_paper)
            elif opposing_plays[i] == opposing_paper:
                your_plays.append(your_scissors)
            elif opposing_plays[i] == opposing_scissors:
                your_plays.append(your_rock)
        i += 1


def score_shape(your_play):
    # shape score
    if your_play == your_rock:
        return rock_score
    elif your_play == your_paper:
        return paper_score
    elif your_play == your_scissors:
        return scissors_score

def score_rock(your_play):
    if your_play == your_rock:
        return draw_score
    elif your_play == your_paper:
        return win_score
    elif your_play == your_scissors:
        return lose_score

def score_paper(your_play):
    if your_play == your_rock:
        return lose_score
    elif your_play == your_paper:
        return draw_score
    elif your_play == your_scissors:
        return win_score   

def score_scissors(your_play):
    if your_play == your_rock:
        return win_score
    elif your_play == your_paper:
        return lose_score
    elif your_play == your_scissors:
        return draw_score

def rock_paper_scissors(opposing_play, your_play):
    if opposing_play == opposing_rock:
        outcome_score = score_rock(your_play)
    elif opposing_play == opposing_paper:
        outcome_score = score_paper(your_play)
    elif opposing_play == opposing_scissors:
        outcome_score = score_scissors(your_play)

    result = score_shape(your_play) + outcome_score
    return result


with open(r"C:\Users\joris\Documents\GitHub\joris_adventofcode2022\2022_2\2022_2_input.txt") as file:
    for line in file:
        opposing_plays.append(line.split()[0]) 
        outcomes.append(line.split()[1])

select_plays(opposing_plays, outcomes)

i = 0
while i < len(opposing_plays): 
    total_score += rock_paper_scissors(opposing_plays[i], your_plays[i])
    i += 1

print(total_score)