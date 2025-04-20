# Simple calculator with verification of correct data entry

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

def enter_correct_number():
    number = input("Enter a number for calculation:\n--->> ")
    try:
        number = float(number)
    except ValueError:
        print("Wrong input. I only work with numbers. Please enter a number.\n")
        return enter_correct_number()
    else:
        return number

def enter_correct_operation():
    operation = input('Pick an operation: "+", "-", "*", "/".\n--->> ')
    if operation in "+-*/":
        return operation
    else:
        print('This is not operation or is not supported. Please enter one of the following operations: "+", "-", "*" or "/"\n')
        return enter_correct_operation()

def yes_or_no():
    answer = input('"yes" or "no": --->> ').lower()
    if answer == "yes":
        return True
    elif answer == "no":
        return False
    else:
        print('Wrong input. Please enter only "yes" or "no".')
        return yes_or_no()


operations= {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

is_start_new = True
while is_start_new:
    print("\nStart calculation. Enter first number.")
    first_number = enter_correct_number()

    is_continue_calculating = True
    while is_continue_calculating:
        selected_operation = enter_correct_operation()

        print("Enter next number.")
        next_number = enter_correct_number()

        result = operations[selected_operation](first_number, next_number)  #!!!
        print(f"{first_number} {selected_operation} {next_number} = {result}")

        print(f'\nIf you want continue with {result} type "yes", or type "no" to start a new calculation.')
        if yes_or_no():
            first_number = result
        else:
            print(f"\nThe result of calculations is {result}")
            is_continue_calculating = False

    print("\nWant to start new calculations?")
    if yes_or_no():
        print("\n" * 5)
    else:
        is_start_new = False
        print("Bye!")
