phone_book = {
    "1111111111": "Amal",
    "2222222222": "Mohammed",
    "3333333333": "Khadijah",
    "4444444444": "Abdullah",
    "5555555555": "Rawan",
    "6666666666": "Faisal",
    "7777777777": "Layla"}

def is_valid_number(number):
    count = 0
    for _ in number:
        count += 1
        if count != 10:
            return False

    for char in number:
        if char < '0' or char > '9':
            return False

    return True

def find_number_by_name():
    phone_number = input("Enter phone number: ")
    if is_valid_number(phone_number):
        for number in phone_book:
            if number == phone_number:
                print(phone_book[phone_number])
                return
        print('Sorry, the phone number is not found.')
    else:
        print('The phone number is invalid.')

def find_number_by_number():
    name = input("Enter the name: ")
    for number, owner in phone_book.items():
        if owner == name:
            print(number)
            return
    print('Sorry, the phone number is not found.')

def add_new_contact():
    new_name = input("Enter new name: ")
    new_number = input("Enter new number: ")
    if is_valid_number(new_number):
        phone_book[new_number] = new_name
        print('Contact added successfully.')
    else:
        print('The phone number is invalid.')


find_number_by_number()
find_number_by_name()
add_new_contact()
