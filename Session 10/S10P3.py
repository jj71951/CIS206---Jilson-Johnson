import re

def match_ab_one_or_more(s):
    return bool(re.match('ab+', s))

# Test cases
print(match_ab_one_or_more("ab"))  # True
print(match_ab_one_or_more("abc"))  # True
print(match_ab_one_or_more("a"))  # False
print(match_ab_one_or_more("abb"))  # True
