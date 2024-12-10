def run_length_encode_with_escape(input_string: str) -> str:
  """
  Encodes a string using RLE with escape sequences for numbers and `#`.

  Args:
      input_string (str): The input string to encode.

  Returns:
      str: The RLE-encoded string with escape sequences.
  """
  if not input_string.isalpha() and '#' not in input_string:
      raise ValueError("Input must be alphabetic or contain # symbols.")

  encoded = []
  count = 1

  for i in range(1, len(input_string)):
      if input_string[i] == input_string[i - 1]:
          count += 1
      else:
          char = input_string[i - 1]
          if char.isdigit() or char == '#':
              char = f"#{char}"
          encoded.append(char + (str(count) if count > 1 else ""))
          count = 1

  # Add the last character group
  last_char = input_string[-1]
  if last_char.isdigit() or last_char == '#':
      last_char = f"#{last_char}"
  encoded.append(last_char + (str(count) if count > 1 else ""))

  return '##00' + ''.join(encoded)

def run_length_decode_with_escape(encoded_string: str) -> str:
  """
  Decodes an RLE-encoded string with escape sequences.

  Args:
      encoded_string (str): The RLE-encoded string with escape sequences.

  Returns:
      str: The decoded string.
  """
  if not encoded_string.startswith('##00'):
      raise ValueError("Encoded string must start with ##00.")

  decoded = []
  i = 4  # Skip the initial '##00'

  while i < len(encoded_string):
      char = encoded_string[i]
      if char == '#':
          i += 1
          char = encoded_string[i]
      i += 1
      count = 0

      while i < len(encoded_string) and encoded_string[i].isdigit():
          count = count * 10 + int(encoded_string[i])
          i += 1

      decoded.append(char * (count if count > 0 else 1))

  return ''.join(decoded)

def main():
  """
  Main function to handle encoding/decoding with escape sequences.
  """
  try:
      user_input = input("Enter a string: ")
      if user_input.startswith('##00'):
          decoded_string = run_length_decode_with_escape(user_input)
          print("Decoded string:", decoded_string)
      else:
          encoded_string = run_length_encode_with_escape(user_input)
          print("Encoded string:", encoded_string)
  except ValueError as e:
      print(f"Error: {e}")

if __name__ == "__main__":
  main()
