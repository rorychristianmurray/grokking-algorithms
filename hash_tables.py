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

## caching example
cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data

## hashes are good for

# modeling relationships from one thing to another thing
# filtering out duplicates
# caching/memoizing data instead of relying
# on computation or the server

## Hash tables have a big O time of:

## Average case:
# O(1) for insert, search, and delete

## Worst case:
# O(n) for insert, search, and delete

## To avoid collisions, we need
# a low load factor
# a good hash function