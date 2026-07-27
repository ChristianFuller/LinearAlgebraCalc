import Calculator

def run():
    choice = 1
    while (choice == 1 or choice == 2):
        choice = int(input("\n\nWhat do you want to do?\n1. Use the Determinite Calculator?\n2. Use the Projection Calculator?\n3. Use Transformation Calculator\n4. Use the Eigenthings Calculator\n5.Quit\n"))
        if(choice == 1):
            Calculator.Determinites.run()
        elif(choice == 2):
            Calculator.Projection.run()
        elif(choice == 3):
            Calculator.Transformation.run()
        elif (choice == 4):
            Calculator.EigenThings.run()
        else:
            print("Quitting")
if __name__ == "__main__":
    run()