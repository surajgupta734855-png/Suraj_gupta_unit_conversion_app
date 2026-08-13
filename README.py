# Simple SI to CGS Unit Converter

def length():
    meter = float(input("Enter length in meters (m): "))
    cm = meter * 100
    print(f"{meter} m = {cm} cm")

def mass():
    kg = float(input("Enter mass in kilograms (kg): "))
    gram = kg * 1000
    print(f"{kg} kg = {gram} g")

def force():
    newton = float(input("Enter force in Newton (N): "))
    dyne = newton * 100000
    print(f"{newton} N = {dyne} dyne")

def energy():
    joule = float(input("Enter energy in Joules (J): "))
    erg = joule * 10000000
    print(f"{joule} J = {erg} erg")

def pressure():
    pascal = float(input("Enter pressure in Pascal (Pa): "))
    barye = pascal * 10
    print(f"{pascal} Pa = {barye} Ba (barye)")

while True:
    print("\n===== SI to CGS Unit Converter =====")
    print("1. Length (m → cm)")
    print("2. Mass (kg → g)")
    print("3. Force (N → dyne)")
    print("4. Energy (J → erg)")
    print("5. Pressure (Pa → Ba)")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        length()
    elif choice == "2":
        mass()
    elif choice == "3":
        force()
    elif choice == "4":
        energy()
    elif choice == "5":
        pressure()
    elif choice == "6":
        print("Thank you for using the Unit Converter!")
        break
    else:
        print("Invalid choice! Please try again.")
