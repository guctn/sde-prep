# Strings are immutable in Python, which means that once a string is created, it cannot be changed. 
# Any operation that modifies a string will create a new string instead of modifying the original one.
# so everything is O(n)

# Append to end of string - O(n) bc creates another string

a = "hello"
b = a + "z"
print(b)           # -> helloz

# Check if something is in string - O(n) bc it needs to iterate through the entire string
if 'e' in b:
    print(True)
else:
    print(False)    # True

# Accessing a specific position - O(1) 
print(b[2])         # -> l