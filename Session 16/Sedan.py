from Vehicle import *

class Sedan(Vehicle):
    performanceTires:bool
    hybrid_engine:bool
    abs_ready:bool

    def __init__(self , make , model , color , year , mileage , VIN , performanceTires , hybrid_engine , abs_ready):
        """
        Initializes Sedan object, contains __init__ from Vehicle:
            
            Raises:
                ValueError: If one or more arguments are not entered or are type None
        """
        super().__init__(make , model , color , year , mileage , VIN)
        try:
            self.performanceTires = performanceTires
            self.hybrid_engine = hybrid_engine
            self.abs_ready = abs_ready

        except:
            raise ValueError("One or more values were not entered correctly, please fill all fields.")
    
    def __str__(self):
        parent = super().__str__()
        child  = "Performance Tires: " + str(self.performanceTires) + '\n'
        child += "Hybrid Engine: " + str(self.hybrid_engine) + '\n'
        child += "ABS System Y/N: " + str(self.abs_ready) + '\n'

        output = parent + child

        return output

    def get_performanceTires(self) -> str:
        return str(self.performanceTires)
    
    def get_hybrid_engine(self) -> str:
        return str(self.hybrid_engine)
    
    def get_abs_ready(self) -> str:
        return str(self.abs_ready)