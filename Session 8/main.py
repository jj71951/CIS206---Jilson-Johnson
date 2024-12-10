def load_customers(filename):
  """
  Reads the customer data from the file and returns a list of tuples.
  Each tuple contains (CompanyName, ContactName, PhoneNumber).
  """
  customers = []
  try:
      with open(filename, 'r') as file:
          for line in file:
              parts = line.strip().split('|')
              if len(parts) == 3:
                  customers.append(tuple(parts))
      return customers
  except FileNotFoundError:
      print(f"Error: The file '{filename}' was not found.")
      return []

def display_sorted_customers(customers, sort_key):
  """
  Displays customers sorted by the specified key.
  sort_key: 0 for CompanyName, 1 for ContactName.
  """
  sorted_customers = sorted(customers, key=lambda x: x[sort_key].lower())
  if sort_key == 0:
      print("Company Name | Contact Name | Phone Number")
      for customer in sorted_customers:
          print(f"{customer[0]} | {customer[1]} | {customer[2]}")
  elif sort_key == 1:
      print("Contact Name | Company Name | Phone Number")
      for customer in sorted_customers:
          print(f"{customer[1]} | {customer[0]} | {customer[2]}")

def search_customers(customers, search_key, field_index):
  """
  Searches for customers based on the search key.
  field_index: 0 for CompanyName, 1 for ContactName.
  """
  results = [cust for cust in customers if search_key.lower() in cust[field_index].lower()]
  if not results:
      print("No matching records found.")
  else:
      for customer in results:
          print(f"Company Name: {customer[0]}")
          print(f"Contact Name: {customer[1]}")
          print(f"Phone Number: {customer[2]}")
          print("-" * 30)

def display_menu():
  """
  Displays the menu of options.
  """
  print("\n1. Display customers sorted by company name")
  print("2. Display customers sorted by contact name")
  print("3. Search customers by company name")
  print("4. Search customers by contact name")
  print("5. Exit")

def main():
  """
  Main program loop.
  """
  filename = "northwind_customers.txt"
  customers = load_customers(filename)

  if not customers:
      return

  while True:
      display_menu()
      try:
          choice = int(input("Enter your choice: "))
          if choice == 1:
              display_sorted_customers(customers, sort_key=0)
          elif choice == 2:
              display_sorted_customers(customers, sort_key=1)
          elif choice == 3:
              search_key = input("Enter company name or part of it: ")
              search_customers(customers, search_key, field_index=0)
          elif choice == 4:
              search_key = input("Enter contact name or part of it: ")
              search_customers(customers, search_key, field_index=1)
          elif choice == 5:
              print("Exiting the program. Goodbye!")
              break
          else:
              print("Invalid choice. Please enter a number between 1 and 5.")
      except ValueError:
          print("Invalid input. Please enter a number.")

if __name__ == "__main__":
  main()
