'''
ReRollDie:
    Simulate die
'''
import random
def rand5(): # Simulate a 5 sided die with a 7 sided die
    roll = random.randint(0,7)
    if roll <= 5: # only output if between 1 - 5
        return roll
    else:
        rand5()

def rand7():
    while True: # Simulate a 7 sided die with a 5 sided die
        roll1 = random.randint(0,5)
        roll2 = random.randint(0,5)
        outcome_number = (roll1-1) * 5 + (roll2-1) + 1 # numbers between 1 - 25

        if outcome_number > 21: # only if in the range is the roll fine
            continue

        return outcome_number % 7 + 1



