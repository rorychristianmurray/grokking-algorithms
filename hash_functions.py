# a hash function is a function where you put in a string and get back a number

# a hash function maps strings to numbers

## contact lists are like hash tables

voted = {}

def check_voter(name):
    if not voted.get(name):
        voted[name] = True
        print("let them vote!")
    else:
        print("kick them out!")


check_voter("Rory")
check_voter("Abbey")
check_voter("Rory")