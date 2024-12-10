def calculate_bmi(weight, height):
  """
  Calculate the BMI (Body Mass Index).

  Parameters:
      weight (float): Weight in pounds.
      height (float): Height in inches.

  Returns:
      float: The calculated BMI.
  """
  return (weight / (height ** 2)) * 703

def display_bmi_table():
  """
  Display a BMI table with weights from 100 to 250 pounds (in 10-pound increments)
  and heights from 58 to 76 inches (in 2-inch increments).
  """
  print("\nBMI Table:")
  print(f"{'Weight (lbs)':<15}{'58 in':>8}{'60 in':>8}{'62 in':>8}{'64 in':>8}{'66 in':>8}{'68 in':>8}{'70 in':>8}{'72 in':>8}{'74 in':>8}{'76 in':>8}")
  print("-" * 95)
  for weight in range(100, 251, 10):
      row = f"{weight:<15}"
      for height in range(58, 77, 2):
          bmi = calculate_bmi(weight, height)
          row += f"{bmi:>8.1f}"
      print(row)

def main():
  """
  Main program to calculate BMI based on user input or display the BMI table.
  Allows the user to input height and weight repeatedly or terminate the program.
  """
  print("Welcome to the BMI Calculator!")
  print("Enter your weight in pounds and height in inches to calculate your BMI.")
  print("Type 'table' to view the BMI table or 'exit' to quit the program.\n")

  while True:
      user_input = input("Enter weight (lbs), height (in), or 'table'/'exit': ").strip().lower()

      if user_input == "exit":
          print("Exiting the program. Goodbye!")
          break
      elif user_input == "table":
          display_bmi_table()
      else:
          try:
              weight, height = map(float, user_input.split(","))
              if weight <= 0 or height <= 0:
                  print("Error: Weight and height must be positive numbers.")
                  continue
              bmi = calculate_bmi(weight, height)
              print(f"Your BMI is: {bmi:.2f}")
              if bmi < 18.5:
                  print("BMI Category: Underweight")
              elif 18.5 <= bmi <= 24.9:
                  print("BMI Category: Normal weight")
              elif 25 <= bmi <= 29.9:
                  print("BMI Category: Overweight")
              else:
                  print("BMI Category: Obesity")
          except ValueError:
              print("Error: Please enter valid inputs in the format 'weight,height' (e.g., 150,68).")

if __name__ == "__main__":
  main()
