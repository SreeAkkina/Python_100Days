def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add, 
    "-": subtract,
    "*": multiply,
    "/": divide,
}

cont = "y"
count = 0

while cont == "y":
    if count == 0:
        num1 = float(input("Whats the first number? >>> "))
        num2 = float(input("What's the second number> >>> "))
        for symbol in operations:
            print(symbol)
        operations_symbol = input("Pick an operation >>>  ")

        calculation_function = operations[operations_symbol]
        answer = calculation_function(num1, num2)
        count += 1
    else:
        num2 = float(input("What's the next number> >>> "))
        operations_symbol = input("Pick an operation >>> ")

        calculation_function = operations[operations_symbol]
        num1 = answer
        answer = calculation_function(answer, num2)
    
    print(f"{num1} {operations_symbol} {num2} = {answer}")
    
    cont = input("Would you like to continue(y or n) or start a new calculation(c)? >>> ")
    
    if cont == "c":
        cont = "y"
        count = 0