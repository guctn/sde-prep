# Hash Tables
# input: 'greg'  -> to store it we need to hash (hash function) it
# 'greg' -> hash function -> 1234 % 5 (hash value and reminder of 5 to get the index) -> 4 (index)
# 'gre' -> hash function -> 1235 % 5 (hash value and reminder of 5 to get the index) -> 0 (index)
# 0 | 'gre' |
# 1 | 
# 2 | 
# 3 | 
# 4 | 'greg' | 

# sometimes we can have collisions, which means that two different keys can have the same hash value.
# then there are two approaches:
# 1. Separate Chaining: we can store the colliding elements in a linked list at the same index.
# 0 | 'gre' |
# 1 | 
# 2 | 
# 3 | 
# 4 | 'greg' -> 'gret' -> linked list

# 2. Open Addressing: we can find the next available index to store the colliding element.
# 0 | 'gre' 
# 1 | 'gret' 
# 2 | 
# 3 | 
# 4 | 'greg' 

# Hash tables purpose:
# Implement a Set (unique elements) and a Map (key-value pairs)

# What are Hashable types in Python?
# Every immutable structure like intergers, floats, strings and tulples
# Not hashable types: lists, sets, dictionaries, and other mutable types
# The reason why, it's because a string for example will always be the same and return the same hash value after the hash function
# however, if used a mutable type like a list, the hash value can change if the list is modified
# and then changes everything

# Hashsets
s = set()       # it can't have duplicates
print(s)        # -> set()

# Add elements to the set - O(1) on average
s.add(1)
s.add(2)
s.add(2)
s.add(3)
print(s)        # -> {1, 2, 3}

# Lookup if item in set - O(1) on average
if 1 in s:
    print(True)
else:
    print(False)

# Remove item from set - O(1)
#s.remove(4)     # returns an error
s.remove(3)     # -> {1, 2}

# It can detect unique elements
string = 'aaaaaaaabbbbbbbbccccceeeeeeeeeeddddd'
sett = set(string)  # -> {'a', 'b', 'c', 'e', 'd'}
# O(S) (string size) -> iterates through the entire string to check the letter

# Hashmaps - Dictionaries
d = {'greg': 1, 'steve': 2, 'rob': 3}
print(d)    # -> {'greg': 1, 'steve': 2, 'rob': 3}

# Addig a new key and valeu in dict - O(1)
d['gusta'] = 4
print(d)    # -> {'greg': 1, 'steve': 2, 'rob': 3, 'gusta': 4}

