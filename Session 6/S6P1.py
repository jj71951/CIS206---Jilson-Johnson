def run_length_encode(input_string: str) -> str:
  """
  Encodes a given string using Run-Length Encoding (RLE).

  Args:
      input_string (str): A string of alphabetic characters to encode.

  Returns:
      str: RLE encoded string where consecutive identical characters are replaced 
           by the character followed by their count (if greater than 1).
  """
  if not input_string.isalpha():
      raise ValueError("Input must contain only alphabetic characters.")

  encoded = []
  count = 1

  for i in range(1, len(input_string)):
      if input_string[i] == input_string[i - 1]:
          count += 1
      else:
          encoded.append(input_string[i - 1] + (str(count) if count > 1 else ""))
          count = 1

  # Add the last character group
  encoded.append(input_string[-1] + (str(count) if count > 1 else ""))

  return ''.join(encoded)

def main():
  """
  Main function to get user input and display RLE-encoded output.
  """
  try:
      user_input = input("Enter a string of alphabetic characters: ")
      encoded_string = run_length_encode(user_input)
      print("Encoded string:", encoded_string)
  except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()
