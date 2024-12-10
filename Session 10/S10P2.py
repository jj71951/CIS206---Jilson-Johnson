import re

def match_ab(s):
    return bool(re.match('ab*', s))

# Test cases
print(match_ab("ab"))  # True
print(match_ab("abc"))  # True
print(match_ab("a"))  # True
print(match_ab("abb"))  # True
