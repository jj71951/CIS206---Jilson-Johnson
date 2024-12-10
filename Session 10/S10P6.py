import re

def match_word_containing_z(s):
    return bool(re.search(r'\b\w*z\w*\b', s))

# Test cases
print(match_word_containing_z("The quick brown fox jumps over the lazy dog."))  # False
print(match_word_containing_z("Python Exercises."))  # False
