from Determinite_Calc import DeterminiteCalc
from Projection_Calc import ProjectionCalc

def run():
    choice = 1
    while (choice == 1 or choice == 2):
        choice = int(input("\n\nWhat do you want to do?\n1. Use the Determinite Calculator?\n2. Use the Projection Calculator?\n3.Quit\n"))
        if(choice == 1):
            DeterminiteCalc.run()
        elif(choice == 2):
            ProjectionCalc.run()
        else:
            print("Quitting")
if __name__ == "__main__":
    run()