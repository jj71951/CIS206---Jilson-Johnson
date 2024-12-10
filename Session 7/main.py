def load_names(file_path):
  """Load names from the given file."""
  try:
      with open(file_path, 'r') as file:
          names = {line.strip() for line in file}
      return names
  except FileNotFoundError:
      print("Error: Input file not found.")
      return set()

def main():
  # Load names from names.txt
  names_file = "names.txt"
  output_file = "nofound.txt"
  names = load_names(names_file)

  if not names:
      return

  print("Loaded names from file.")

  # Prepare the output file for writing not found names
  with open(output_file, 'w') as not_found_file:
      while True:
          user_input = input("Enter a name (or type 'exit' to quit): ").strip()
          if user_input.lower() == 'exit':
              print("Exiting the program.")
              break
          elif user_input in names:
              print(f"{user_input} is found in the file.")
          else:
              print(f"{user_input} is not found. Writing to {output_file}.")
              not_found_file.write(user_input + '\n')

if __name__ == "__main__":
  main()
