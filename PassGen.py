import random

def generate_random_password(length=12, include_numbers=True, include_symbols=True):
  """Generates a random password of the given length.

  Args:
    length: The length of the password.
    include_numbers: Whether to include numbers in the password.
    include_symbols: Whether to include symbols in the password.

  Returns:
    A random password of the given length.
  """

  chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
  if include_numbers:
    chars += "0123456789"
  if include_symbols:
    chars += "!@#$%^&*()"

  password = ""
  for i in range(length):
    password += random.choice(chars)
  return password

def memorize_previous_passwords(password):
  """Memorizes a previous password.

  Args:
    password: The password to memorize.
  """

  # Create a list to store the previous passwords.
  previous_passwords = []

  # If the password is not already in the list, add it.
  if password not in previous_passwords:
    previous_passwords.append(password)

  # Return the list of previous passwords.
  return previous_passwords

def main():
  """Generates a random password based on user input and memorizes it."""

  # Prompt the user for the desired password length.
  password_length = int(input("Enter the desired password length: "))

  # Prompt the user for whether to include numbers in the password.
  include_numbers = input("Include numbers in the password? (y/n): ")
  if include_numbers == "y":
    include_numbers = True
  else:
    include_numbers = False

  # Prompt the user for whether to include symbols in the password.
  include_symbols = input("Include symbols in the password? (y/n): ")
  if include_symbols == "y":
    include_symbols = True
  else:
    include_symbols = False

  # Generate a random password based on the user's input.
  password = generate_random_password(password_length, include_numbers, include_symbols)

  # Memorize the generated password.
  memorize_previous_passwords(password)

  # Print the generated password to the console.
  print("Generated password:", password)

if __name__ == "__main__":
  main()
