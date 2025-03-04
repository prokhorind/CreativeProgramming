# 1. Creating a dictionary
person = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# 2. Accessing values using keys
name = person['name']
age = person['age']
print(f"Name: {name}, Age: {age}")

# 3. Adding and Modifying Key-Value Pairs
person['occupation'] = 'Engineer'  # Adding new key-value
person['age'] = 26  # Modifying an existing value
print(f"Updated person: {person}")

# 4. Removing Key-Value Pairs
del person['city']  # Removing a key-value pair
occupation = person.pop('occupation')  # Removing and getting the value
print(f"Updated person after removal: {person}")
print(f"Removed occupation: {occupation}")

# 5. Iterating through a dictionary
print("Iterating through the dictionary:")
for key, value in person.items():
    print(f"{key}: {value}")

# 6. Checking if a key exists
if 'name' in person:
    print(f"Name exists: {person['name']}")
else:
    print("Name not found.")

# 7. Nested Dictionaries
students = {
    'Alice': {'age': 25, 'grade': 'A'},
    'Bob': {'age': 22, 'grade': 'B'}
}
print(f"Alice's grade: {students['Alice']['grade']}")

