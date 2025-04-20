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
    first_number = float(input("What's the first number?: "))
    continue_calculating = True

    while continue_calculating:
        selected_operation = input("+\n-\n*\n/\nPick an operation: ")
        next_number = float(input("What's the next number?: "))

        for key in operations:
            if selected_operation == key:
                result = operations[key](first_number,next_number)
                print(f"{first_number} {selected_operation} {next_number} = {result}")
                if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower() == 'n':
                    continue_calculating = False
                    print("\n" * 3)
                else:
                    first_number = result
