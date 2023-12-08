def main():
    userInput = input("Expression: ")
    print(calculate(userInput))

def calculate(userInput):
    inputs = processUserInput(userInput)
    num1, operator, num2 = float(inputs[0]), inputs[1], float(inputs[2])

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return round(num1 * num2, 1)
    else:
        return round(num1 / num2, 1)


def processUserInput(userInput):
    return userInput.split(" ")

main()