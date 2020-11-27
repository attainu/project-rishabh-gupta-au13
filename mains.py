import time
from menus import*
import parkinglots as parkinglots


if __name__ == "__main__":
    print("ENTER 1 FOR FILE INPUT OR 2 FOR COMMAND LINE INPUT ")
    i = int(input(""))
    if i == 1:
        f = open("inputs.txt", "r")
        while(1):
            time.sleep(2)
            x = f.readline()
            if len(x) == 0:
                break
            print(x)
        f.close()
        f = open("outputs.txt", "r")
        time.sleep(2)
        print("THE OUTPUT OF FOLLOWING QUERIES")
        while(1):
            time.sleep(2)
            x = f.readline()
            if len(x) == 0:
                break
            print(x)
    else:
        print("WELCOME TO THE PARKING SLOT PROGRAM")
        Size = int(input("How much car can it hold? "))
        print(f"CREATE PARKING LOT {Size}")
        Parking = parkinglots.Parking_lot(Size)
        Menu()
        time.sleep(4)
        while True:

            Options = input()

            if Options == "1":
                Reg_no = input("ENTER REGISTRATION NUMBER  ")
                Color = input("ENTER THE COLOUR ")

                Parking.park_car(Reg_no, Color)

            elif Options == "2":
                Reg_no = input("Please Enter the registration number: ")

                print(
                    f"Your car with Reg_no - {Reg_no} is exited from slot no. {Parking.Exit(Reg_no)}")

            elif Options == "3":
                Reg_no = input(
                    "Please Enter the registration number of your car: ")
                Parking.slot_of_car_by_Reg_no(Reg_no)

            elif Options == "4":
                Color = input("Please type the color of the car: ").lower()
                Parking.slots_of_cars_by_color(Color)

            elif Options == "5":
                print(f"The nearest empty slot is: {Parking.get_slot()}")

            elif Options.lower() == "quit" or Options.lower() == "exit":

                break

            else:
                print("Invalid choice, please select a valid option from the Menu")
