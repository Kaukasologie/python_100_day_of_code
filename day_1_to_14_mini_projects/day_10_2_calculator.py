# Simply calculator

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

while True:
    first_number = float(input("What's the first number?: "))
    continue_calculating = True

    while continue_calculating:
        operation = input("+\n-\n*\n/\nPick an operation: ")
        next_number = float(input("What's the next number?: "))
        result = ''

        if operation == "+":
            result = add(first_number, next_number)
        elif operation == "-":
            result = subtract(first_number, next_number)
        elif operation == "*":
            result = multiply(first_number, next_number)
        elif operation == "/":
            result = divide(first_number, next_number)
        else:
            print("Operator not correct")
            continue_calculating = False

        if type(result) == float:
            print(f"{first_number} {operation} {next_number} = {result}")

            if input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower() == 'n':
                continue_calculating = False
            else:
                first_number = result

    print("\n" * 3)
