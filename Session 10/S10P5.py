import re

def match_start_word(s):
    return bool(re.match(r'\b\w+\b', s))

# Test cases
print(match_start_word("The quick brown fox jumps over the lazy dog."))  # True
print(match_start_word(" The quick brown fox jumps over the lazy dog."))  # False
