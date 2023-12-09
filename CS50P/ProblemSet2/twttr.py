def main():
    userInput = input("Input: ")
    print(f"Output: {processInput(userInput)}")

def processInput(userInput):
    wordWithoutVowels = ""
    for letter in userInput:
        if letter not in ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]:
            wordWithoutVowels += letter
    return wordWithoutVowels

main()