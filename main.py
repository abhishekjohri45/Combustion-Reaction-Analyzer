"""
Combustion Reaction Analyzer
Author: Abhishek Johri
"""

import math
import matplotlib.pyplot as plt

# Heat of combustion (kJ/mol)
heat_data = {
    "CH4": 890, "C2H6": 1560, "C3H8": 2220,
    "C4H10": 2877, "C5H12": 3509, "C6H14": 4163,
    "C7H16": 4817, "C8H18": 5471
}

# -------- Parse hydrocarbon formula --------
def parse_formula(formula):
    if len(formula) == 0 or formula[0] != "C" or "H" not in formula:
         return None, None

    h_pos = formula.find("H")
    c_text = formula[1:h_pos]
    h_text = formula[h_pos+1:]

    try:
        if c_text == "":
            carbon = 1
        

    
        else:
            carbon = int(c_text)
     
       

        hydrogen = int(h_text)

        return carbon, hydrogen

    except:
       return None, None


while True:

    print("\n" + "="*55)
    print("        COMBUSTION REACTION ANALYZER")
    print("="*55)

    print("1. Balance Equation")
    print("2. Calculate Molar Mass")
    print("3. Stoichiometry")
    print("4. Heat Released")
    print("5. Plot Heat Graph")
    print("6. Save Result to File")
    print("7. Exit")

    choice = input("\nEnter choice: ")

    if choice == "7":
        print("Goodbye!")
        break

    formula = input("\nEnter hydrocarbon (ex: CH4, C2H6, C8H18): ").strip()

    carbon, hydrogen = parse_formula(formula)

    if carbon is None:
        print("Invalid hydrocarbon formula.")
        continue

    molar_mass = carbon*12.01 + hydrogen*1.008

    # Balance
    if choice == "1":

        fuel = 1
        oxygen = carbon + hydrogen/4
        co2 = carbon
        h2o = hydrogen/2

        factor = 1
        if oxygen != int(oxygen):
            factor = 2

        fuel *= factor
        oxygen *= factor
        co2 *= factor
        h2o *= factor

        print("\nBalanced Equation:")
        print(f"{int(fuel)}{formula} + {int(oxygen)}O2 -> "
              f"{int(co2)}CO2 + {int(h2o)}H2O")

    # Molar Mass
    elif choice == "2":

        print("\nCarbon atoms :", carbon)
        print("Hydrogen atoms :", hydrogen)
        print(f"Molar Mass = {molar_mass:.2f} g/mol")

    # Stoichiometry
    elif choice == "3":

        mass = float(input("Enter fuel mass (g): "))

        moles = mass / molar_mass

        oxygen_moles = moles * (carbon + hydrogen/4)
        co2_moles = moles * carbon
        h2o_moles = moles * (hydrogen/2)

        oxygen_mass = oxygen_moles * 32
        co2_mass = co2_moles * 44
        h2o_mass = h2o_moles * 18

        print(f"\nFuel moles = {moles:.3f}")
        print(f"Oxygen required = {oxygen_mass:.2f} g")
        print(f"CO2 formed = {co2_mass:.2f} g")
        print(f"H2O formed = {h2o_mass:.2f} g")

    # Heat
    elif choice == "4":

        if formula not in heat_data:
            print("Heat data available only up to C8H18.")
            continue

        mass = float(input("Enter fuel mass (g): "))

        moles = mass / molar_mass
        heat = moles * heat_data[formula]

        print(f"\nHeat Released = {heat:.2f} kJ")

    # Graph
    elif choice == "5":

        if formula not in heat_data:
            print("Heat data unavailable.")
            continue

        masses = [10,20,30,40,50,60,70,80,90,100]
        heats = []

        for m in masses:
            mol = m / molar_mass
            heats.append(mol * heat_data[formula])

        plt.plot(masses, heats, marker="o")
        plt.xlabel("Fuel Mass (g)")
        plt.ylabel("Heat Released (kJ)")
        plt.title(f"Heat vs Fuel Mass ({formula})")
        plt.grid()
        plt.show()

    # Save result
    elif choice == "6":

        file = open("results.txt","a")
        file.write(f"Fuel: {formula}\n")
        file.write(f"Molar Mass: {molar_mass:.2f}\n")
        file.write("-"*30 + "\n")
        file.close()

        print("Saved to results.txt")

    else:
        print("Invalid choice.")
