# Print function
print("Pig Latin")

# Input
# Start coding here!
original = raw_input("Enter a word:")

# we need to ensure that the user actually typed something.
# original = raw_input("Enter a word:")
if len(original) > 0:
  print(original)
else:
  print("empty")

# Use and, is.alpha statement
original = raw_input("Enter a word:")
if len(original) > 0 and original.isalpha():
  print(original)
else:
  print("empty")

# Ay B C
pyg = 'ay'

# Word Up
#pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
else:
    print('empty')

# concatenate strings together
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
else:
    print('empty')

# Set new_word equal to the slice from the 1st index all the way to the end of new_word.
# Use [1:len(new_word)] to do this
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
else:
    print('empty')

# Last test
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
  word = original.lower()
  first = word[0]
  new_word = word + first + pyg
  new_word = new_word[1:len(new_word)]
  print('new_world')
else:
    print('empty')