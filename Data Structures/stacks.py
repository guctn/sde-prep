# STACKS - LAST IN FIRST OUT (LIFO)
stk = []

# Append to the top of the stack - O(1)
stk.append(5)
stk.append(4)
stk.append(10)

print(stk)
# out: [5, 4, 10]

# Pop from stack - O(1)
# it's good to keep track of what you pop

x = stk.pop()

print(x)
# out: 10
print(stk)
# out: [5, 4]

# Peek, what's on the top? - O(1)
print(stk[-1])
# out: 4

# Ask if the stack is empty - O(1)
# before you ever run pop is important to check if it's empty
# in order to not return an error 
if stk:
    print(True)

