import re

def find_location_of_word(text, word):
    match = re.search(r'\b' + word + r'\b', text)
    if match:
        return match.start(), match.end()
    return None

# Test case
text = 'The quick brown fox jumps over the lazy dog.'
word = 'fox'
print(find_location_of_word(text, word))  # (16, 19)
