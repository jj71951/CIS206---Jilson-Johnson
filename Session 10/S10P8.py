import re

def search_for_words(text, words):
    return [word for word in words if re.search(r'\b' + word + r'\b', text)]

# Test case
text = 'The quick brown fox jumps over the lazy dog.'
words = ['fox', 'dog', 'horse']
print(search_for_words(text, words))  # ['fox', 'dog']
