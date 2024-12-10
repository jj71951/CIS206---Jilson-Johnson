def run_length_decode(encoded_string: str) -> str:
  """
  Decodes a given RLE-encoded string back to its original format.

  Args:
      encoded_string (str): The RLE-encoded string to decode.

  Returns:
      str: The decoded string.
  """
  decoded = []
  i = 0

  while i < len(encoded_string):
      char = encoded_string[i]
      i += 1
      count = 0

      # Check if the next characters are numbers (count)
      while i < len(encoded_string) and encoded_string[i].isdigit():
          count = count * 10 + int(encoded_string[i])
          i += 1

      decoded.append(char * (count if count > 0 else 1))

  return ''.join(decoded)

def main():
  """
  Main function to check if input is RLE, decode or encode accordingly.
  """
  try:
      user_input = input("Enter a string: ")
      if any(char.isdigit() for char in user_input):
          # Already in RLE format
          decoded_string = run_length_decode(user_input)
          print("Decoded string:", decoded_string)
      else:
          # Not in RLE format
          encoded_string = run_length_encode(user_input)
          print("Encoded string:", encoded_string)
  except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()
