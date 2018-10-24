import os
import datetime


class Vehicle(object):

    def __init__(self, brand, model, total_km, last_maintenance):
        self.brand = brand
        self.model = model
        self.total_km = int(total_km)
        self.last_maintenance = last_maintenance

    def display_data(self):
        print "Brand: {}, Model: {}, Total kilometers: {}, Last service: {}".format(self.brand, self.model, self.total_km, self.last_maintenance)

    def add_kilometers(self, additional_kilometers):
        self.total_km += int(additional_kilometers)
        print "Total kilometers for {} {} set to: {} km".format(self.brand,
                                                                self.model,
                                                                self.total_km)

    def change_maintenance_date(self, new_maintenance_date):
        self.last_maintenance = new_maintenance_date
        print "Last service for {} {} set to: {} ".format(self.brand,
                                                          self.model,
                                                          self.last_maintenance)


class DatabaseAccess(object):
    vehicles = []

    def __init__(self, db_filename):
        self.db_filename = db_filename

    def initialize_file(self):
        if os.path.isfile(self.db_filename):
            with open(self.db_filename, "r") as file:
                vehicles_str = file.read()

            vehicles_str = vehicles_str.split("\n")

            for line in vehicles_str:
                if len(line) > 0:
                    self.vehicles.append(Vehicle(*line.split(";")))
            print "Database {} loaded!\n".format(self.db_filename)
        else:
            with open(self.db_filename, "a") as file:
                file.write("")
                print "New empty database created!\n"

        return self.vehicles

    def write_to_file(self):
        output_string = ""
        for vehicle in vehicle_list:
            output_string += "{};{};{};{}\n".format(str(vehicle.brand),
                                                    str(vehicle.model),
                                                    str(vehicle.total_km),
                                                    str(vehicle.last_maintenance))

        with open(self.db_filename, "w") as file:
            file.writelines(output_string)
        print "File: "+self.db_filename+" saved!\n"


class VehicleCollection(object):

    def __init__(self, vehicle_list):
        self.vehicle_list = vehicle_list

    def print_vehicles(self):
        for item in self.vehicle_list:
            item.display_data()

    def add_km(self, selected_no, kilometers):
        if selected_no > len(vehicle_list):
            print "Vehicle does not exist!"
        else:
            for n, vehicle in enumerate(vehicle_list):
                if selected_no == n+1:
                    vehicle.add_kilometers(kilometers)
                    # vehicle.total_km += kilometers  <== alternative or better/worse?

    def change_maintenance(self, selected_no, new_maintenance_date):
        if selected_no > len(vehicle_list):
            print "Vehicle does not exist!"
        else:
            for n, vehicle in enumerate(vehicle_list):
                if selected_no == n+1:
                    vehicle.change_maintenance_date(new_maintenance_date)
                    # vehicle.last_maintenance = new_maintenance_date <== alternative or better/worse?

    def print_vehicles_short(self):
        for n, vehicle in enumerate(vehicle_list):
            print str(n+1)+". " + vehicle.brand + ", " +  vehicle.model

    def add_vehicle(self, brand, model, total_km, last_maintenance):
        vehicle_list.append(Vehicle(brand, model, total_km, last_maintenance))
        print "Vehicle {} {} added succesfully!".format(brand, model)

    def delete_vehicle(selfs, selected_no):
        if selected_no > len(vehicle_list):
            print "Vehicle does not exist!"
        else:
            for n, vehicle in enumerate(vehicle_list):
                if selected_no == n + 1:
                    vehicle_list.pop(n)
                    print "Vehicle {} {} removed!".format(vehicle.brand,
                                                          vehicle.model)

    def get_vehicle_name_by_index(self, selected_no):
        if selected_no > len(vehicle_list):
            return ""
        else:
            for n, vehicle in enumerate(vehicle_list):
                if selected_no == n + 1:
                    return "{} {}".format(vehicle.brand, vehicle.model)


    def __len__(self):
        return len(self.vehicle_list)


def check_if_date(date_to_check):
    try:
        dmy = datetime.datetime.strptime(date_to_check, "%d.%m.%Y")
        if dmy > datetime.datetime.now():
            print "Date {} is future date!".format(date_to_check)
            return False
        else:
            return True
    except ValueError:
        print "Value \"{}\" is not a date!".format(date_to_check)
        return False

def check_if_string(string_to_check):
    if type(string_to_check) is str and len(string_to_check) > 1:
        return True
    else:
        print "Value \"{}\" is not valid, please try again!".format(string_to_check)
        return False


if __name__ == '__main__':
    print "Welcome to vehicle database."
    db_file = raw_input("Please enter database filename (or press enter): ")
    if len(db_file) == 0:
        db_file = "db.txt"

    db = DatabaseAccess(db_file)
    vehicle_list = db.initialize_file()
    collection = VehicleCollection(vehicle_list)

    menu_selection = 0

    while True:
        while menu_selection not in range(1,7):
            print "\nSelect option:\n" \
                  "1. Display all vehicles\n" \
                  "2. Add kilometers\n" \
                  "3. Change service date\n" \
                  "4. Add vehicle\n" \
                  "5. Delete vehicle\n" \
                  "6. Exit\n"
            try:
                menu_selection = int(raw_input("Please enter number: "))
                if menu_selection > 6:
                    print "Wrong choice, please try again\n"
            except ValueError:
                print "That is not a number!"

        if len(vehicle_list) == 0 and menu_selection not in (4,6):
            print "The database is empty. Please add a vehicle first!\n"
            menu_selection = 0

        if menu_selection == 1:
            collection.print_vehicles()

        if menu_selection == 2:
            selected_vehicle = 0
            kilometers = -1

            while True:
                collection.print_vehicles_short()
                try:
                    selected_vehicle = int(raw_input("Select a vehicle: "))
                except ValueError:
                    print "Wrong choice, please try again\n"
                    continue

                while True:
                    if len(collection.get_vehicle_name_by_index(selected_vehicle)) == 0:
                        break
                    else:
                        try:
                            kilometers = int(raw_input("Enter kilometers to add to {} : ".format(collection.get_vehicle_name_by_index(selected_vehicle))))
                            break
                        except ValueError:
                            print "Please enter a number"
                            continue

                collection.add_km(selected_vehicle, kilometers)
                break

        if menu_selection == 3:
            selected_vehicle = 0

            while True:
                collection.print_vehicles_short()
                try:
                    selected_vehicle = int(raw_input("Select a vehicle: "))
                except ValueError:
                    print "Wrong choice, please try again"
                    continue

                while True:
                    if len(collection.get_vehicle_name_by_index(selected_vehicle)) == 0:
                        break
                    else:
                        new_maintenance_date = raw_input("Enter last service date for {} (dd.MM.yyyy): ".format(collection.get_vehicle_name_by_index(selected_vehicle)))
                    if not check_if_date(new_maintenance_date):
                        continue
                    break

                if selected_vehicle == 0:
                    continue

                collection.change_maintenance(selected_vehicle, new_maintenance_date)
                break

        if menu_selection == 4:
            while True:
                brand = raw_input("Brand: ")
                if not check_if_string(brand):
                    continue
                else:
                    break
            while True:
                model = raw_input("Model: ")
                if not check_if_string(model):
                    continue
                else:
                    break
            while True:
                try:
                    total_km = raw_input("Total kilometers: ")
                    total_km = int(total_km) # 2 steps because string value is still used even if conversion to int fails
                except ValueError:
                    print "{} is not a valid number. Try again.".format(total_km)
                    continue
                else:
                    break
            while True:
                maintenance_date = raw_input("Last service date: ")
                if not check_if_date(maintenance_date):
                    continue
                else:
                    break

            collection.add_vehicle(brand.upper(), model.capitalize(), total_km, maintenance_date)

        if menu_selection == 5:
            selected_vehicle = 0

            while True:
                collection.print_vehicles_short()
                try:
                    selected_vehicle = int(raw_input("Select a vehicle to delete: "))
                except ValueError:
                    print "Wrong choice, please try again"

                if selected_vehicle == 0:
                    break

                collection.delete_vehicle(selected_vehicle)
                break

        if menu_selection == 6:
            db.write_to_file()
            print "Have a nice day!"
            break

        menu_selection = 0
