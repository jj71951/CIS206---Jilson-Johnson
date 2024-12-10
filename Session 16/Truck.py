from Vehicle import *

class Truck(Vehicle):
    offroad_tires:bool
    diesel_engine:bool
    pickup_body:bool
    HP:float

    def __init__(self , make , model , color , year , mileage , VIN , offroad_tires , diesel_engine , pickup_body , HP):
        """
        Initializes Sedan object, contains __init__ from Vehicle:
            
            Raises:
                ValueError: If one or more arguments are not entered or are type None
        """
        super().__init__(make , model , color , year , mileage , VIN)
        try:
            self.offroad_tires = offroad_tires
            self.diesel_engine = diesel_engine
            self.pickup_body = pickup_body
            self.HP = HP

        except:
            raise ValueError("One or more values were not entered correctly, please fill all fields.")

    def __str__(self):
        parent = super().__str__()
        child  = "Offroad Tires: " + str(self.offroad_tires) + '\n'
        child += "Diesel Engine: " + str(self.diesel_engine) + '\n'
        child += "Pickup body: " + str(self.pickup_body) + '\n'
        child += "Horse Power: " + str(self.HP) + '\n'

        output = parent + child

        return output

    def get_offroad_tires(self) -> str:
        return str(self.offroad_tires)
    
    def get_diesel_engine(self) -> str:
        return str(self.diesel_engine)
    
    def get_pickup_body(self) -> str:
        return str(self.pickup_body)
    
    def get_HP(self) -> str:
        return str(self.HP)