def display_menu():
    print("view - View country name")
    print("add - Add a country")
    print("del - Delete a country")
    print("exit - Exit program")
    print()

def view(countries):
    for keys in countries:
        print(keys + "\t")
    while True:
        enter_code = input("Enter country code: ")
        try:
            country = countries[enter_code]
            print("Country:", country)
        except KeyError as ke:
            print("Code not found.", ke)
        if input("Would you like to view another country?").lower() == "y":
            continue
        else:
            print("OK. Moving on")
            break

def add(countries):
    while True:
        add_code = input("Enter country code: ")
        add_code = add_code.upper()
        if add_code in countries:
            country = countries.get(add_code)
            print(add_code, "is already being used by", country)
        else:
            add_name = input("Enter country name: ")
            countries[add_code] = add_name
            print(add_name, "was added")
            if input("Would you like to add another country?").lower() == "y":
                continue
            else:
                print("OK. Moving on")
                break

def del_countries(countries):
    while True:
        del_code = input("Enter country code: ")
        if del_code in countries:
            name = countries.pop(del_code)
            print(name, "was deleted")
        else:
            print("There is no country with this code.")
        if input("Would you like to delete another country?").lower() == "y":
            continue
        else:
            print("OK. Moving on")
            break

def main():
    countries = {"CA": "Canada",
                     "US": "United States",
                     "MX": "Mexico"}

    display_menu()

    while True:
        command = input("Command: ")
        if command.lower() == "view":
            view(countries)
        elif command.lower() == "add":
            add(countries)
        elif command.lower() == "del":
            del_countries(countries)
        elif command.lower() == "exit":
            print("Too bad m8. Bye")
            break
        else:
            print("Invalid command. Try again")

main()

if __name__ == "__main__":
    main()