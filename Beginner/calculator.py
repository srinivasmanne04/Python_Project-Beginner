while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        operator = input("Enter an opartor (+, -, *, /) or 'q' to quit: ")

        if operator == "q":
            print("Exiting calculator.......Bye!!!")
            break

        if operator == "+":
            result = a + b
        elif operator == "-":
            result = a - b
        elif operator == "*":
            result =  a * b
        elif operator == "/":
            if b != 0:
                result = a / b
            else:
                print("Error! Division by zero is not allowed")
        else:
            result = "Invalid operator"

        print(f"The result of {a} {operator} {b} is {result}")

    except ValueError:
        print("Invalid input, Please enter a valid integer")   