# Raj has five friends
friends = ["Aman", "Riya", "Sahil", "Neha", "Arjun"]

# Dictionary to store birthdays
birthdays = {}

print("Enter the birthdays for Raj's five friends.")

# Ask and store
for name in friends:
    date = input(f"Enter {name}'s birthday (e.g., 12/08/2010): ")
    birthdays[name] = date

# Print the birthdays
print("\n--- Birthdays List ---")
for name, date in birthdays.items():
    print(f"{name}: {date}")

print("\nBest of luck!")
