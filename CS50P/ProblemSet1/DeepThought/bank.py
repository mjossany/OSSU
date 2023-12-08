def main():
    employeeGreeting = input("Greeting: How you doing? ")
    print(greetingCheck(employeeGreeting))

def greetingCheck(employeeGreeting):
    processedGreeting = processGreeting(employeeGreeting)

    if processedGreeting == "hello" or processedGreeting == "hello,":
        return "$0"
    elif processedGreeting[0] == "h":
        return "$20"
    else:
        return "$100"

def processGreeting(employeeGreeting):
    return employeeGreeting.strip().split()[0].lower()

main()