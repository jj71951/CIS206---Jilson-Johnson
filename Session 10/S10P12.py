import re

def find_words_a_e(s):
    return re.findall(r'\b[aeAE]\w*\b', s)

# Test case
text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
print(find_words_a_e(text))  # ['example', 'ArrayList', 'a', 'elements', 'elements', 'added', 'ArrayList', 'ArrayList']
