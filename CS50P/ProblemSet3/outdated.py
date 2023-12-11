def main():

    monthsList = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        try:
            dateInput = input("Date: ")
            dateSplittedByBar = dateInput.split("/")
            if len(dateSplittedByBar) == 3:
                if 12 >= int(dateSplittedByBar[0]) >= 1 and 31 >= int(dateSplittedByBar[1]) >= 1:
                    print(f"{dateSplittedByBar[2].strip()}-{int(dateSplittedByBar[0]):02}-{int(dateSplittedByBar[1]):02}")
                    break
                else:
                    pass
            dateSplittedByComma = dateInput.split(",")
            if len(dateSplittedByComma) == 2:
                dateSplittedBySpace = dateSplittedByComma[0].split(" ")
                if 12 >= int(dateSplittedBySpace[1]) >= 1:
                    print(f"{dateSplittedByComma[1].strip()}-{int(monthsList.index(dateSplittedBySpace[0]) + 1):02}-{int(dateSplittedBySpace[1]):02}")
                    break
                else:
                    pass
            pass
        except ValueError:
            pass
        except EOFError:
            break

    print("\n", end="")

main()
