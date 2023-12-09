def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if validateFirstTwoLetters(s) and validatePlateLength(s) and validateNumbersEndsThePlate(s) and validateCharsAndNumbers(s):
        return True
    return False

def validateFirstTwoLetters(s):
    for letter in s[0:2]:
        if letter in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
            return False
    return True

def validatePlateLength(s):
    if len(s) < 2 or len(s) > 6:
        return False
    return True

def validateNumbersEndsThePlate(s):
    firstNumber = ""
    if any(char.isdigit() for char in s):
        numbers = ""
        for char in s:
            if char.isdigit():
                numbers += char

        if numbers[0] == "0":
            return False
        firstNumber += numbers[0]

        strAfterFirstNumber = s.split(firstNumber)[1]

        for char in strAfterFirstNumber:
            if not char.isdigit():
                return False

    return True

def validateCharsAndNumbers(s):
    punctuation_list = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~', ' ']
    if any(char in punctuation_list for char in s):
        return False
    return True

main()
