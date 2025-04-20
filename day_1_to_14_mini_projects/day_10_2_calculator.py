# Simple calculator solution through dictionaries

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations= {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

while True:
    try:
        print("\nNew calculation.")
        first_number = float(input("What's the first number?:\n--->> "))
    except ValueError:
        print("Wrong input. I only work with numbers. Please enter a number.")
    else:
        is_continue_calculating = True
        while is_continue_calculating:
            selected_operation = input("Pick an operation:\n+\n-\n*\n/\n--->> ")
            while selected_operation not in "+-*/":
                print('This is not operation or is not supported. Pick an operation from list below or "exit": "+", "-", "*" or "/"')
                selected_operation = input("Pick a supported operation:\n--->> ")

            is_correct_number = False
            while not is_correct_number:
                try:
                    next_number = float(input("What's the next number?: "))
                except ValueError:
                    print("Wrong input 2. I only work with numbers. Please enter a number.")
                else:
                    is_correct_number = True
                    result = operations[selected_operation](first_number, next_number)
                    print(f"{first_number} {selected_operation} {next_number} = {result}")
                    continue_or_not = input(f"Type 'yes' to continue calculating with {result}, or type 'no' to start a new calculation:\n--->> ").lower()
                    if continue_or_not == "yes":
                        first_number = result
                    elif continue_or_not == "no":
                        print("\n" * 3)
                        is_continue_calculating = False
                    else:
                        print('Wrong input. You had to enter "yes" or "no"')
                        is_continue_calculating = False
