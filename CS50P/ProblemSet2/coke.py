def main():
    amountDue = 50
    while amountDue > 0:
        print(f"Amount Due: {amountDue}")
        coinValue = input("Insert Coin: ")
        amountDue = processCoin(coinValue, amountDue)
    print(f"Change Owed: {amountDue - (2 * amountDue)}")

def processCoin(coinValue, amountDue):
    intCoinValue = int(coinValue)
    if intCoinValue not in [25, 10, 5]:
        return amountDue
    amountDue -= intCoinValue
    return amountDue

main()
