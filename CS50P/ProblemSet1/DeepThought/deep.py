def main():
    userInput = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    print(checkIf42(userInput))

def checkIf42(input):
    trimmedInput = input.strip().lower()
    match trimmedInput:
        case "42" | "forty-two" | "forty two":
            return "Yes"
        case _:
            return "No"

main()