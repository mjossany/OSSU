def main():
    timeInput = input("What time is it?: ")
    timeConverted = convert(timeInput)

    if 7.0 <= timeConverted <= 8.0:
        print("breakfast time")
    elif 12.0 <= timeConverted <= 13.0:
        print("lunch time")
    elif 18.0 <= timeConverted <= 19.0:
        print("dinner time")
    else:
        print("")

def convert(timeInput):
    twelveFormat = timeInput.split(" ")

    if len(twelveFormat) > 1:
        hours, minutes = timeInput.split(":")
        print(hours, minutes)
        minutesFormatted = minutes.split(" ")[0]

        match twelveFormat[1]:
            case "a.m.":
                return round((((float(hours) * 60) + float(minutesFormatted)) / 60), 2)
            case _:
                return round((((float(int(hours) + 12) * 60) + float(minutesFormatted)) / 60), 2)

    hours, minutes = timeInput.split(":")
    return round((((float(hours) * 60) + float(minutes)) / 60), 2)

if __name__ == "__main__":
    main()