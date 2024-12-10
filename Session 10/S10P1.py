import re

def contains_only_certain_chars(string):
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    return bool(pattern.match(string))

print(contains_only_certain_chars("ABCDEFabcdef123450"))  # True
print(contains_only_certain_chars("*&%@#!}{"))          # False
