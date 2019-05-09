"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("default_car", 180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
#    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    print('\n-next car-\n')

    my_limo = Car(0)
    my_limo.limo()
    my_limo.add_fuel(20)
    print("fuel =", my_limo.fuel)
    my_limo.drive(115)
    print('Odometer =', my_limo.odometer)

    print(my_limo)

    print("\n-car program starts here-\n")

    car_name_list = {}

    while True:
        try:
            print("menu:\nAdd car = A\nview car = V\nDrive car = D\nQuit = Q")
            menu_select = input("enter the menu item: ").lower()
            if menu_select == "a":
                new_car = 0
                car_name = input("enter the name of your car")
                car_fuel = int(input("enter the amount of fuel in the car"))
                new_car = Car(car_name, car_fuel)
                car_name_list[car_name] = new_car
                continue
            if menu_select == "v":
                row_no = 1
                for row in car_name_list:
                    print("{}. {}".format(row_no, row))
                continue

            if menu_select == "d":
                try:
                    row_no = 1
                    for row in car_name_list:
                        print("{}. {}".format(row_no, row))
                    car_choice = int(input("enter the number of the car you want to drive"))
                    how_far = int(input("enter how far you want to drive"))



                except ValueError:
                    print("invalid values try again")
                continue
            if menu_select == "q":
                break
            else:
                print("please enter a valid option")
        except ValueError:
            print("invalid values, try again")
    print("thank you")


main()
