class Vehicle(object):

    category:str
    make:str
    model:str
    color:str
    year:int
    mileage:int
    VIN:str

    def __init__(self , make , model , color , year , mileage , VIN) -> None:
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.mileage = mileage
        self.VIN = VIN

    def __str__(self) -> str:
        parent = "\033[4mVehicle info:\033[0m\n"
        parent += "Make:" + self.get_make() + "\n"
        parent += "Model:" + self.get_model() + "\n"
        parent += "Color:" + self.get_color() + "\n"
        parent += "Year:" + str(self.get_year()) + "\n"
        parent += "Mileage:" + str(self.get_mileage()) + "\n"
        parent += "VIN:" + str(self.get_VIN()) + "\n"

        return parent


    #Get functions
    def get_category(self) -> str:
        return self.category

    def get_make(self) -> str:
        return self.make
    
    def get_model(self) -> str:
        return self.model
    
    def get_color(self) -> str:
        return self.color
    
    def get_year(self) -> int:
        return self.year
    
    def get_mileage(self) -> int:
        return self.mileage
    
    def get_VIN(self) -> str:
        return self.VIN
    
    def get_class_name(self):
        return self.__class__.__name__
    

    #Set functions
    def set_category(self, value):
        """Sets vehicle category.

        Args:
            value (str): category
        
        Raises:
            ValueError: If value entered is of type None.
            
        Returns:
            False: If value entered is invalid.
            True: If all values are entered within parameteres.
    
        """
        temp_input = ""

        try:
            if value == "" or value == None:
                print('\n\033[1mERROR:' , "Value cannot be empty" , '\033[0m\n')
                return False
            else:
                temp_input = str(value)
        
        except Exception as error:
            print('\n\033[1mERROR:' , error , '\033[0m\n')
            return False
                  
        else:
            if temp_input.lower() == "sedan" or temp_input.lower() == "truck":
                self.category = temp_input
                return True
            else:
                print('\n\033[1mERROR:' , "Invalid vehicle category. Options are: Sedan , Truck" , '\033[0m\n')

    def set_make(self, value):
        """Sets vehicle make.

        Args:
            value (str): make
        
        Raises:
            ValueError: If value entered is of type None.
            
        Returns:
            False: If value entered is invalid.
            True: If all values are entered within parameteres.
    
        """
        temp_input = ""

        try:
            if value == "" or value == None:
                print('\n\033[1mERROR:' , "Value cannot be empty" , '\033[0m\n')
                return False
            else:
                temp_input = str(value)
        
        except Exception as error:
            print('\n\033[1mERROR:' , error , '\033[0m\n')
            return False
                  
        else:
            self.make = temp_input
            return True
    
    def set_model(self, value):
        """Sets vehicle model.

        Args:
            value (str): model
        
        Raises:
            ValueError: If value entered is of type None.
            
        Returns:
            False: If value entered is invalid.
            True: If all values are entered within parameteres.
    
        """
        temp_input = ""

        try:
            if value == "" or value == None:
                print('\n\033[1mERROR:' , "Value cannot be empty" , '\033[0m\n')
                return False
            else:
                temp_input = str(value)
        
        except Exception as error:
            print('\n\033[1mERROR:' , error , '\033[0m\n')
            return False
                  
        else:
            self.model = temp_input
            return True
        
    def set_color(self, value):
        """Sets vehicle color.

        Args:
            value (str): color
        
        Raises:
            ValueError: If value entered is of type None.
            
        Returns:
            False: If value entered is invalid.
            True: If all values are entered within parameteres.
    
        """
        temp_input = ""

        try:
            if value == "" or value == None:
                print('\n\033[1mERROR:' , "Value cannot be empty" , '\033[0m\n')
                return False
            else:
                temp_input = str(value)
        
        except Exception as error:
            print('\n\033[1mERROR:' , error , '\033[0m\n')
            return False
                  
        else:
            self.color = temp_input
            return True
    
    def set_year(self, value):
        """Sets vehicle year.

        Args:
            value (int): year
        
        Raises:
            ValueError: If value entered is of type None.
            
        Returns:
            False: If value entered is invalid.
            True: If all values are entered within parameteres.
    
        """
        temp_input = 0

        try:
            if value == "" or value == None:
                print('\n\033[1mERROR:' , "Value cannot be empty" , '\033[0m\n')
                return False
            else:
                temp_input = int(value)
        
        except Exception as error:
            print('\n\033[1mERROR:' , error , '\033[0m\n')
            return False
                  
        else:
            if temp_input == 0:
                print('\n\033[1mERROR:' , "Value cannot be zero" , '\033[0m\n')
                return False
            elif len(temp_input) != 4 or temp_input > 2024:
                print('\n\033[1mERROR:' , "Invalid year input" , '\033[0m\n')
            else:
                self.year = temp_input
                return True

    def set_mileage(self, value):
        """Sets vehicle mileage.

        Args:
            value (int): mileage
        
        Raises:
            ValueError: If value entered is of type None.
            
        Returns:
            False: If value entered is invalid.
            True: If all values are entered within parameteres.
    
        """
        temp_input = 0

        try:
            if value == "" or value == None:
                print('\n\033[1mERROR:' , "Value cannot be empty" , '\033[0m\n')
                return False
            else:
                temp_input = int(value)
        
        except Exception as error:
            print('\n\033[1mERROR:' , error , '\033[0m\n')
            return False
                  
        else:
            if temp_input == 0:
                print('\n\033[1mERROR:' , "Value cannot be zero" , '\033[0m\n')
                return False
            self.mileage = temp_input
            return True

    def set_VIN(self, value):
        """Sets vehicle VIN.

        Args:
            value (str): VIN
        
        Raises:
            ValueError: If value entered is of type None.
            
        Returns:
            False: If value entered is invalid.
            True: If all values are entered within parameteres.
    
        """
        temp_input = ""

        try:
            if value == "" or value == None:
                print('\n\033[1mERROR:' , "Value cannot be empty" , '\033[0m\n')
                return False
            else:
                temp_input = str(value)
        
        except Exception as error:
            print('\n\033[1mERROR:' , error , '\033[0m\n')
            return False
                  
        else:
            if len(temp_input) != 17:
                print('\n\033[1mERROR:' , "Invalid VIN input" , '\033[0m\n')
            self.VIN = temp_input
            return True