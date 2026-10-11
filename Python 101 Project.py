phone_book = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"}

def is_valid_number(number): # Define a function to check if a phone number is valid
    count = 0
    for _ in number:
        count += 1
        if count != 10:
            return False         # Return False and stop the function

    for char in number:
        if char < '0' or char > '9':
            return False

    return True                 # Return True if all validation checks pass

def find_number_by_name():
    phone_number = input("Enter phone number: ")
    if is_valid_number(phone_number):             # Check if the entered phone number is valid
        for number in phone_book:
            if number == phone_number:
                print(phone_book[phone_number])        # Print the name associated with the phone number
                return                                 # Stop the function after finding the name
        print('Sorry, the phone number is not found.')
    else:
        print('The phone number is invalid.')

def find_number_by_number():
    name = input("Enter the name: ")
    for number, owner in phone_book.items():             # Loop through dictionary keys and values
        if owner == name:
            print(number)
            return                                        # Stop the function after finding the number
    print('Sorry, the phone number is not found.')

def add_new_contact():
    new_name = input("Enter new name: ")
    new_number = input("Enter new number: ")
    if is_valid_number(new_number):                       # Check if the new phone number is valid
        phone_book[new_number] = new_name                 # Add the new phone number as a key and the name as its value
        print('Contact added successfully.')
    else:
        print('The phone number is invalid.')


find_number_by_number()
find_number_by_name()
add_new_contact()
