import re

def find_lowercase_with_underscore(s):
    return bool(re.match('^[a-z]+(_[a-z]+)+$', s))

# Test cases
print(find_lowercase_with_underscore("aab_cbbbc"))  # True
print(find_lowercase_with_underscore("aab_Abbbc"))  # False
print(find_lowercase_with_underscore("Aaab_abbbc"))  # False
