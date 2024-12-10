import re

def replace_punctuation(text):
    return re.sub(r'[ ,.]', ':', text)

# Test case
print(replace_punctuation('Python Exercises, PHP exercises.'))  # Python:Exercises::PHP:exercises:
