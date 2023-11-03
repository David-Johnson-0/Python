from sympy import symbols, Eq, solve

def calculate_volume_from_molarity():
    print("Volume Calculation Program")
    print("Enter the molarity and liters of solute to calculate the volume of the solution.")
    
    try:
        molarity = float(input("Enter the molarity (in mol/L or M): "))
        liters_of_solute = float(input("Enter the liters of solute: "))
        molarity2 = float(input("Enter second molarity (in mol/L or M): "))
        liters_of_solute2 = float(input("Enter second liters of solute: "))
    except ValueError:
        print("Invalid input. Please enter numerical values for molarity and liters of solute.")
        return
    
    # Calculate the volume of the solution
    volume_of_solution = liters_of_solute * molarity
    print(volume_of_solution)
    volume_of_solution2 = liters_of_solute2 * molarity2
    print(volume_of_solution2)
    
    total_volume = volume_of_solution2-volume_of_solution if volume_of_solution2 > volume_of_solution else volume_of_solution-volume_of_solution2

    print(f"The volume of the solution is {(total_volume) * 1000:.2f} mils (mL).")

def balance_equation(equation):
    # Split the equation into reactants and products
    reactants, products = equation.split("->")

    reactant_compounds = reactants.split('+')
    product_compounds = products.split('+')

    # Create a list of symbols for the coefficients
    coefficients = [symbols(f'x{i}') for i in range(len(reactant_compounds) + len(product_compounds))]

    # Create equations based on conservation of mass
    equations = []

    for compound in reactant_compounds:
        elements = compound.split()
        equation = Eq(coefficients[-1], 1)
        for element in elements:
            symbol, count = element_parse(element)
            equation += coefficients[symbol] * count
        equations.append(equation)

    for compound in product_compounds:
        elements = compound.split()
        equation = Eq(coefficients[-1], 1)
        for element in elements:
            symbol, count = element_parse(element)
            equation += coefficients[symbol + len(reactant_compounds)] * count
        equations.append(equation)

    # Solve the system of equations
    solutions = solve(equations)

    # Find a valid solution
    for solution in solutions:
        if all(solution[coeff] > 0 for coeff in solution):
            coefficients_solution = [solution[coeff] for coeff in coefficients]
            return dict(zip(coefficients, coefficients_solution))

    return None

def element_parse(element):
    symbol = element
    count = 1
    if element[0].isalpha():
        symbol = element[0]
        if element[1:].isdigit():
            count = int(element[1:])
    return symbol, count

def runStoich():
    equation = input("Enter the chemical equation: ")
    balanced_coefficients = balance_equation(equation)

    if balanced_coefficients:
        for coeff, value in balanced_coefficients.items():
            print(f"{coeff} = {value}")
    else:
        print("No valid solution found. This equation may not be balanceable.")
    return
