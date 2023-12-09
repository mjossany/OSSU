def main():
    userInput = input("camelCase: ")
    print(printUserInputInSnakeCase(userInput))

def printUserInputInSnakeCase(userInput):
    inputInSnakeCase = ""
    for letter in userInput:
        if letter.isupper():
            inputInSnakeCase += "_" + letter.lower()
        else:
            inputInSnakeCase += letter
    return inputInSnakeCase

main()
