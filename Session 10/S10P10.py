def replace_spaces(text):
  text = text.replace(' ', '_')
  return text.replace('_', ' ')

# Test cases
print(replace_spaces("Regular Expressions"))  # Regular_Expressions
print(replace_spaces("Code_Examples"))  # Code Examples
