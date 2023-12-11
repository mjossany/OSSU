def main():

    shopListDict = {}

    while True:
        try:
            userInput = input()
            itemName = userInput.lower()
            if itemName in shopListDict:
                shopListDict[itemName] += 1
            else:
                shopListDict[itemName] = 1
        except EOFError:
            break

    print("\n", end="")

    sortedDict = dict(sorted(shopListDict.items()))

    for item in sortedDict:
        print(f"{sortedDict[item]} {item.upper()}")
main()
