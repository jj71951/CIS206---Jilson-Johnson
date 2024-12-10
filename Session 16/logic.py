import json
import Vehicle
import Sedan
import Truck

def main():
    inventory = []
    quit = False

    #Read JSON file and turn into python dictionary (Load)
    inventory = get_inventory("inventory.json")

    #Menu

    while not quit:
        print("\nCar Inventory Management \033[3m(By Elaine, Jilson, and Leo)\033[0m")
        print("1. Add Vehicle")
        print("2. Update Vehicle")
        print("3. Show Inventory")
        print("4. Delete Vehicle")
        print("5. Quit")

        try:
            choice = int(input("Option: "))

        except Exception as error:
            print('\n\033[1mERROR:' , error , '\033[0m\n')
        
        else:
            if choice == 1:
                #1. Add Vehicle
                try:
                    new_vehicle = add_vehicle(add())
                
                except Exception as error:
                    print('\n\033[1mERROR:' , error , '\033[0m\n')
                
                else:
                    inventory.append(new_vehicle)
            elif choice == 2:
                #2. Update Vehicle
                inventory = update_car(inventory)
            elif choice == 3:
                #3. Show inventory
                for car in inventory:
                    print(car)
            elif choice == 4:
                #4. Delete Vehicle
                inventory = delete_car(inventory)
            elif choice == 5:
                print("Exiting... Goodbye!")
                quit = True
            else:
                print('\n\033[1mERROR:' , "Invalid choice. Please enter a number between 1 and 5." , '\033[0m\n')

    #end -> Save inventory
    save_inventory("inventory.json" , inventory)

    return 1

#Load inventory
def get_inventory(file_name):
    stock = []

    #Read json data from file
    with open(file_name) as file:
        data = json.load(file)
        data = data["Cars"]

        #Get VIN numbers to iterate thru keys
        vehicle_VIN_list = list(data.keys())
    

    for VIN in vehicle_VIN_list:
        if data[VIN]["category"].lower() == "sedan":
            new_vehicle = Sedan.Sedan(data[VIN]["make"] , data[VIN]["model"] , data[VIN]["color"] ,
                                data[VIN]["year"] , data[VIN]["mileage"] , VIN,
                                data[VIN]["performance_tires"] , data[VIN]["hybrid_engine"] , data[VIN]["abs_ready"])
            new_vehicle.category = "Sedan"
        elif data[VIN]["category"].lower() == "truck":
            new_vehicle = Truck.Truck(data[VIN]["make"] , data[VIN]["model"] , data[VIN]["color"] ,
                                data[VIN]["year"] , data[VIN]["mileage"] , VIN,
                                data[VIN]["offroad_tires"] , data[VIN]["diesel_engine"] , data[VIN]["pickup_body"] ,
                                data[VIN]["HP"])
            new_vehicle.category = "Truck"

        stock.append(new_vehicle)
    
    return stock

#Menu option Add Car
def add_vehicle(package):
    #Write data to json file
    if package[0].lower() == "sedan":
        if len(package) != 10:
            raise ValueError("Invalid qty. of parameters for Sedan. Please try again")
        else:
            package = package[1:]
            new_vehicle = Sedan.Sedan(*package)
    elif package[0].lower() == "truck":
        if len(package) != 11:
            raise ValueError("Invalid qty. of parameters for Sedan. Please try again")
        else:
            package = package[1:]
            new_vehicle = Truck.Truck(*package)
    else:
        raise ValueError("Invalid vehicle category, valid categories are: Sedan , Truck. Please try again.")

    return new_vehicle

#Menu option Update Car
def update_car(inventory):
    found = False
    go_back = False
    vin_lookup = ""
    it = 0
    key = ""
    try:
        vin_lookup = input("Enter VIN of vehicle to update: ")
    
    except Exception as error:
        print('\n\033[1mERROR:' , error , '\033[0m\n')
    
    else:
        vin_lookup = vin_lookup.lower()

        for car in inventory:
            if vin_lookup == car.get_VIN().lower():
                vin_lookup = car.get_VIN()
                found = True
                break
            else:
                it += 1
        
        if not found:
            print('\n\033[1mERROR:' , "VIN: " + vin_lookup  + " could not be found!", '\033[0m\n')
        else:
            while not go_back:
                print("What would you like to update about " + vin_lookup + " ?")
                print("1. Make")
                print("2. Model")
                print("3. Color")
                print("4. Year")
                print("5. Mileage")
                print("6. Go back\n")

                try:
                    choice = int(input("Option: "))
                
                except Exception as error:
                    print('\n\033[1mERROR:' , error , '\033[0m\n')
                
                else:
                    if   choice == 1:
                        key = "make"
                        new_value = getMake()
                        inventory[it].set_make(new_value.capitalize())
                        go_back = True
                    elif choice == 2:
                        key = "model"
                        new_value = getModel()
                        inventory[it].set_model(new_value.capitalize())
                        go_back = True
                    elif choice == 3:
                        key = "color"
                        new_value = getColor()
                        inventory[it].set_color(new_value.capitalize())
                        go_back = True
                    elif choice == 4:
                        key = "year"
                        new_value = getYear()
                        inventory[it].set_year(new_value)
                        go_back = True
                    elif choice == 5:
                        key = "mileage"
                        new_value = getMileage()
                        inventory[it].set_mileage(new_value)
                        go_back = True
                    elif choice == 6:
                        print()
                        go_back = True
            if key != "":
                print(key.capitalize() , "Successfully updated to" , new_value , "for" , vin_lookup)
    
    return inventory

def delete_car(inventory):
    found = False
    vin_lookup = ""
    it = 0
    try:
        vin_lookup = input("Enter VIN of vehicle to delete: ")
    
    except Exception as error:
        print('\n\033[1mERROR:' , error , '\033[0m\n')
    
    else:
        vin_lookup = vin_lookup.lower()

        for car in inventory:
            if vin_lookup == car.get_VIN().lower():
                vin_lookup = car.get_VIN()
                found = True
                break
            else:
                it += 1
        
        if not found:
            print('\n\033[1mERROR:' , "VIN: " + vin_lookup  + " could not be found!", '\033[0m\n')
        else:
            del inventory[it]
            print("Vehicle with VIN: " + vin_lookup.upper() + " successfully deleted.")
    return inventory
    
#Final step before closing program
def save_inventory(file_name , inventory:Vehicle):
    #Convert list of objects into nested dictionary as in json file
    
    Cars = {}
    Cars_packer = {}
    Cars_packer["Cars"] = Cars


    for car in inventory:
        if car.get_class_name().lower() == "sedan":
            Cars[car.get_VIN().upper()] = {"category":car.get_class_name(),
                                    "make":car.get_make(),
                                    "model":car.get_model(),
                                    "color":car.get_color(),
                                    "year":car.get_year(),
                                    "mileage":car.get_mileage(),
                                    "performance_tires":car.get_performanceTires(),
                                    "hybrid_engine":car.get_hybrid_engine(),
                                    "abs_ready":car.get_abs_ready()}
        elif car.get_class_name().lower() == "truck":
            Cars[car.get_VIN().upper()] = {"category":car.get_class_name(),
                                    "make":car.get_make(),
                                    "model":car.get_model(),
                                    "color":car.get_color(),
                                    "year":car.get_year(),
                                    "mileage":car.get_mileage(),
                                    "offroad_tires":car.get_offroad_tires(),
                                    "diesel_engine":car.get_diesel_engine(),
                                    "pickup_body":car.get_pickup_body(),
                                    "HP":car.get_HP()}
        else:
            print('\n\033[1mERROR:' , "Aborting save process. Invalid vehicle category found" , '\033[0m\n')
            print("Error: " + str(car.get_class_name()))


    with open(file_name , "w") as file:
        json.dump(Cars_packer , file , indent = 2)


#all get... functions are used to enter a vehicle's information
def getCategory():
    valid = False
    while not valid:
        make = input("Please enter the category: ")

        if make == "":
            print("Please enter a category.")
        elif make.lower() != "sedan" and make.lower() != "truck":
            print("Please enter a valid category.")
        else:
            valid = True
    return make

def getMake():
    valid = False
    while not valid:
        make = str(input("Please enter the make: "))
        if make == "":
            print("Please enter a valid make.")
        else:
            valid = True
    return make

def getModel():
    valid = False
    while not valid:
        model = str(input("Please enter the model: "))
        if model == "":
            print("Please enter a valid model.")
        else:
            valid = True
    return model

def getColor():
    valid = False
    while not valid:
        color = str(input("Please enter the color: "))
        if color == "":
            print("Please enter a valid color.")
        else:
            valid = True
    return color

def getYear():
    valid = False
    while not valid:
        try:
            year = int(input("Please enter the year: "))

        except Exception as error:
            print('\n\033[1mERROR:' , error , '\033[0m\n')
            
        else:
            if year == 0:
                print("Please enter a valid year.")
            else:
                valid = True
    return year


def getMileage():
    valid = False
    while not valid:
        try:
            mileage = int(input("Please enter the mileage: "))

        except Exception as error:
            print('\n\033[1mERROR:' , error , '\033[0m\n')

        else:
            if mileage < 0:
                print("Please enter a valid mileage.")
            else:
                valid = True
    
    return mileage

def getVIN():
    valid = False
    while not valid:
        vin = str(input("Please enter the vin: "))
        if vin == "":
            print("Please enter a valid vin.")
        else:
            valid = True
    return vin

def get_sedan_attrs():
    valid_tires = False
    valid_engine = False
    valid_abs = False
    while not valid_tires:
        performance_tires = str(input("Does the vehicle have Performance Tires? (y/n): "))

        if performance_tires == "":
            print("Please enter an answer.")
        elif performance_tires == "y" or performance_tires == "Y":
            performance_tires = True
            valid_tires = True
        elif performance_tires == "n" or performance_tires == "N":
            performance_tires = False
            valid_tires = True
        else:
            print("Error: Please enter a valid answer.")

    while not valid_engine:
        hybrid_engine = str(input("Does the vehicle have a Hybrid Engine? (y/n): "))

        if hybrid_engine == "":
            print("Please enter an answer.")
        elif hybrid_engine == "y" or hybrid_engine == "Y":
            hybrid_engine = True
            valid_engine = True
        elif hybrid_engine == "n" or hybrid_engine == "N":
            hybrid_engine = False
            valid_engine = True
        else:
            print("Error: Please enter a valid answer.")

    while not valid_abs:
        abs_ready = str(input("Does the vehicle have an ABS System? (y/n): "))

        if abs_ready == "":
            print("Please enter an answer.")
        elif abs_ready == "y" or abs_ready == "Y":
            abs_ready = True
            valid_abs = True
        elif abs_ready == "n" or abs_ready == "N":
            abs_ready = False
            valid_abs = True
        else:
            print("Error: Please enter a valid answer.")
    
    return [performance_tires , hybrid_engine , abs_ready]


def get_truck_attrs():
    valid_tires = False
    valid_engine = False
    valid_pickup = False
    valid_HP = False
    while not valid_tires:
        offroad_tires = str(input("Does the vehicle have Offroad Tires? (y/n): "))

        if offroad_tires == "":
            print("Please enter an answer.")
        elif offroad_tires == "y" or offroad_tires == "Y":
            offroad_tires = True
            valid_tires = True
        elif offroad_tires == "n" or offroad_tires == "N":
            offroad_tires = False
            valid_tires = True
        else:
            print("Error: Please enter a valid answer.")

    while not valid_engine:
        diesel_engine = str(input("Does the vehicle have a Diesel Engine? (y/n): "))

        if diesel_engine == "":
            print("Please enter an answer.")
        elif diesel_engine == "y" or diesel_engine == "Y":
            diesel_engine = True
            valid_engine = True
        elif diesel_engine == "n" or diesel_engine == "N":
            diesel_engine = False
            valid_engine = True
        else:
            print("Error: Please enter a valid answer.")

    while not valid_pickup:
        pickup_body = str(input("Does the vehicle have a Pickup Body? (y/n): "))

        if pickup_body == "":
            print("Please enter an answer.")
        elif pickup_body == "y" or pickup_body == "Y":
            pickup_body = True
            valid_pickup = True
        elif pickup_body == "n" or pickup_body == "N":
            pickup_body = False
            valid_pickup = True
        else:
            print("Error: Please enter a valid answer.")
    
    while not valid_HP:
        try:
            HP = int(input("Enter Trcuk's Horsepower: "))

        except Exception as error:
            print('\n\033[1mERROR:' , error , '\033[0m\n')

        else:
            if HP > 0:
                valid_HP = True
            else:
                print("Error: Enter a valid value.")
    
    return [offroad_tires , diesel_engine , pickup_body , HP]


def add():
    addCategory = getCategory()
    addMake = getMake()
    addModel = getModel()
    addColor = getColor()
    addYear = getYear()
    addMileage = getMileage()
    addVIN = getVIN()

    output = [addCategory , addMake , addModel , addColor , addYear , addMileage , addVIN]

    if addCategory.lower() == "sedan":
        for attr in get_sedan_attrs():
            output.append(attr)
    elif addCategory.lower() == "truck":
        for attr in get_truck_attrs():
            output.append(attr)

    return output

#Run program
main()

    



