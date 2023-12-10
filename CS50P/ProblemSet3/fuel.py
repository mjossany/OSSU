def main():
    print(processFuelQuantity("Fraction: "))

def processFuelQuantity(prompt):
    while True:
        try:
            userInput = input(prompt)
            values = userInput.split("/")
            verifyIfXIsNotGreaterThanY(values)
            return calculateFuelPercentage(values)
        except (ValueError, ZeroDivisionError):
            pass

def verifyIfXIsNotGreaterThanY(values):
    if int(values[0]) > int(values[1]):
        raise ValueError

def calculateFuelPercentage(values):
    try:
        percentage = round((int(values[0]) / int(values[1])) * 100)
        if percentage <= 1:
            return "E"
        if percentage >= 99:
            return "F"
        return f"{percentage}%"
    except ValueError:
        raise ValueError
    except ZeroDivisionError:
        raise ZeroDivisionError

main()