#Password Generator Project
import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
# Get user input
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
def password_gen_easy(num_letters, num_symbols, num_numbers):
    password_letters = ""
    password_symbols = ""
    password_numbers = ""

    # generate elements loop function
    def element_list_populate(element_count, element_type_list, element_list):
        for i in range(element_count):
            random_element_index = random.randint(0, len(element_type_list) - 1)
            random_element = element_type_list[random_element_index]
            element_list += random_element

    element_list_populate(num_letters, letters, password_letters)
    element_list_populate(num_symbols, symbols, password_symbols)
    element_list_populate(num_numbers, numbers, password_numbers)

    # Placed repeating code in function element_list_populate 
    # for i in range(0, num_letters):
    #     random_index_letters = random.randint(0, len(letters) - 1)
    #     password_letters.append(letters[random_index_letters])

    # for i in range(0, num_symbols):
    #     random_index_symbols = random.randint(0, len(symbols) - 1)
    #     password_letters.append(symbols[random_index_symbols])

    # for i in range(0, num_numbers):
    #     random_index_numbers = random.randint(0, len(numbers) - 1)
    #     password_letters.append(numbers[random_index_numbers])

    print("".join(password_letters))

    print("".join(password_symbols))

    print("".join(password_numbers))

print(password_gen_easy(nr_letters, nr_symbols, nr_numbers))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

def password_gen_hard(num_letters, num_symbols, num_numbers):
    letter_list = []
    symbol_list = []
    number_list = []

    def element_list_populate(element_count, element_type_list, element_list):
        for i in range(element_count):
            random_element_index = random.randint(0, len(element_type_list) - 1)
            random_element = element_type_list[random_element_index]
            element_list.append(str(random_element))

    element_list_populate(num_letters, letters, letter_list)
    element_list_populate(num_symbols, symbols, symbol_list)
    element_list_populate(num_numbers, numbers, number_list)

    # for i in range(0, num_letters):
    #   random_letter_index = random.randint(0, len(letters) - 1)
    #   random_letter = letters[random_letter_index]
    #   letter_list.append(str(random_letter))

    # for i in range(0, num_symbols):
    #   random_symbol_index = random.randint(0, len(symbols) - 1)
    #   random_symbol = symbols[random_symbol_index]
    #   symbol_list.append(str(random_symbol))

    # for i in range(0, num_numbers):
    #   random_number_index = random.randint(0, len(numbers) - 1)
    #   random_number = numbers[random_number_index]
    #   number_list.append(str(random_number))

    password_list = letter_list + symbol_list + number_list

    mixed_password = []

    for i in range(0, len(password_list)):
        random_index = random.randint(0, len(password_list) - 1)
        random_element = password_list[random_index]
        mixed_password.append(str(random_element))
        password_list.pop(random_index)

    generated_password = "".join(mixed_password)

    print(generated_password)

# print(password_gen_hard(nr_letters, nr_symbols, nr_numbers))