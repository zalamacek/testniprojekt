class Cars:
    def __init__(self, brand, model, kilometers, service):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers
        self.service = service

    def get_full_name(self):
        return self.brand + " " + self.model

def list_all_cars(cars):
    for index, car in enumerate(cars):
        print "ID: " + str(index)
        print car.get_full_name()
        print car.kilometers
        print car.service
        print ""

    if not cars:
        print "You don't have any cars in your list."

def add_new_car(cars):
    brand = raw_input("Please enter the brand: ")
    model = raw_input("Please enter the model: ")
    kilometers = raw_input("Please enter the kilometers: ")
    service = raw_input("Please enter the date of last service: ")

    new = Cars(brand=brand, model=model, kilometers=kilometers, service=service)
    cars.append(new)

    print ""
    print new.get_full_name() + " was successfully added to your list."

def edit_cars(cars):
    print "Select the number of the car you'd like to edit:"

    for index, car in enumerate(cars):
        print str(index) + ") " + car.get_full_name()

    print ""
    selected_id = raw_input("Which car would you like to edit? (enter ID number): ")
    selected_car = cars[int(selected_id)]

    new_kilometers = raw_input("Please enter the kilometers for %s: " % selected_car.get_full_name())
    selected_car.kilometers = new_kilometers

    print ""
    print "Kilometers updated."

    new_service = raw_input("Please enter the date of the last service for %s: " % selected_car.get_full_name())
    selected_car.service = new_service

    print ""
    print "Date updated."


def delete_car(cars):
    print "Select the number of the car you'd like to delete:"

    for index, car in enumerate(cars):
        print str(index) + ") " + car.get_full_name()

    print ""
    selected_id = raw_input("Which car would you like to delete? (enter ID number): ")
    selected_car = cars[int(selected_id)]

    cars.remove(selected_car)
    print ""
    print "Car was successfully removed from your contact list."

def main():
    print "Welcome to your Car Park"

    passat = Cars(brand="Volkswagen", model="Passat", kilometers="20.000", service="1.2.2016")
    clio = Cars(brand="Renault", model="Clio", kilometers="60.000", service="5.8.2016")
    carrera = Cars(brand="Porsche", model="Carrera", kilometers="30.000", service="1.11.2016")
    astra = Cars(brand="Opel", model="Astra", kilometers="120.000", service="17.9.2016")
    cars = [passat, clio, carrera, astra]

    while True:
        print ""
        print "Please choose one of these options:"
        print "a) See all your cars"
        print "b) Add a new car"
        print "c) Edit a car"
        print "d) Delete a car"
        print "e) Quit the program."
        print ""

        selection = raw_input("Enter your selection (a, b, c, d or e): ")
        print ""

        if selection.lower() == "a":
            list_all_cars(cars)
        elif selection.lower() == "b":
            add_new_car(cars)
        elif selection.lower() == "c":
            edit_cars(cars)
        elif selection.lower() == "d":
            delete_car(cars)
        elif selection.lower() == "e":
            print "Thank you for using the Car List. Goodbye!"
            break
        else:
            print "Sorry, I didn't understand your selection. Please try again."
            continue


if __name__ == "__main__":
    main()


