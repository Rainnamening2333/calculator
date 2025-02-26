while True:
    print('Hi user')
    op = input('Pick an operation (1:Addition, 2:Subtraction, 3:Multiplication, 4:Division, 5:Exit, 6:Power, 7:Square Root, 8:Modulus): ')
    
    # Input check
    if op == '5':
        print('Goodbye!')
        break

    # Checking for correctness of transaction entry
    if not op.isdigit() or int(op) > 8:
        print('Incorrect operation, try again')
        continue
    
    op = int(op)
    
    # Entering numbers
    try:
        num1 = float(input('Enter the first number: '))
        num2 = float(input('Enter the second number: '))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        continue
    
    # Operation execution
    if op == 1:
        print(f"Result: {num1 + num2}")
    elif op == 2:
        print(f'Result: {num1 - num2}')
    elif op == 3:
        print(f'Result: {num1 * num2}')
    elif op == 4:
        try:
            print(f'Result: {num1 / num2}')
        except ZeroDivisionError:
            print('Division by zero is not allowed')
    elif op == 6:
        print(f'Result: {num1 ** num2}')
    elif op == 7:
        if num1 >= 0 and num2 >= 0:
            print(f'Result: {round(num1 ** 0.5, 2)}, {round(num2 ** 0.5, 2)}')
        else:
            print('Square root is not defined for negative numbers')
    elif op == 8:
        try:
            print(f'Result: {num1 % num2}')
        except ZeroDivisionError:
            print('Modulus by zero is not allowed')
    else:
        print('Invalid operation selected. Please choose a valid option (1-8)')

