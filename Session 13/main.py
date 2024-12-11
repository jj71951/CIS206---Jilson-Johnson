"""
BMI Calculator Class Module
This module defines a BMI calculator class with methods for calculating BMI using both metric and US units.
It includes private methods for necessary unit conversions and adheres to Python coding conventions.
"""

# Constants for unit conversions
POUNDS_TO_KILOGRAMS = 0.453592
INCHES_TO_METERS = 0.0254
FEET_TO_INCHES = 12

class BMICalculator:
    """
    A class for calculating Body Mass Index (BMI).

    Methods:
        calculate_bmi_metric(weight_kg: float, height_m: float) -> float:
            Calculates BMI using metric units.

        calculate_bmi_us(weight_lb: float, height_ft: int, height_in: int) -> float:
            Calculates BMI using US units.
    """

    def __init__(self):
        pass

    def calculate_bmi_metric(self, weight_kg: float, height_m: float) -> float:
        """
        Calculates BMI using metric units.

        Args:
            weight_kg (float): Weight in kilograms.
            height_m (float): Height in meters.

        Returns:
            float: Calculated BMI.
        """
        return weight_kg / (height_m ** 2)

    def calculate_bmi_us(self, weight_lb: float, height_ft: int, height_in: int) -> float:
        """
        Calculates BMI using US units.

        Args:
            weight_lb (float): Weight in pounds.
            height_ft (int): Height in feet.
            height_in (int): Additional height in inches.

        Returns:
            float: Calculated BMI.
        """
        weight_kg = self._pounds_to_kilograms(weight_lb)
        total_inches = self._feet_to_inches(height_ft) + height_in
        height_m = self._inches_to_meters(total_inches)
        return weight_kg / (height_m ** 2)

    def _pounds_to_kilograms(self, pounds: float) -> float:
        """
        Converts pounds to kilograms.

        Args:
            pounds (float): Weight in pounds.

        Returns:
            float: Weight in kilograms.
        """
        return pounds * POUNDS_TO_KILOGRAMS

    def _feet_to_inches(self, feet: int) -> int:
        """
        Converts feet to inches.

        Args:
            feet (int): Height in feet.

        Returns:
            int: Height in inches.
        """
        return feet * FEET_TO_INCHES

    def _inches_to_meters(self, inches: float) -> float:
        """
        Converts inches to meters.

        Args:
            inches (float): Height in inches.

        Returns:
            float: Height in meters.
        """
        return inches * INCHES_TO_METERS

if __name__ == "__main__":
    # Main program
    print("Welcome to the BMI Calculator!")

    calculator = BMICalculator()

    unit_system = input("Enter 'metric' for metric units or 'us' for US units: ").strip().lower()

    if unit_system == "metric":
        weight_kg = float(input("Enter your weight in kilograms: "))
        height_m = float(input("Enter your height in meters: "))
        bmi = calculator.calculate_bmi_metric(weight_kg, height_m)
    elif unit_system == "us":
        weight_lb = float(input("Enter your weight in pounds: "))
        height_ft = int(input("Enter your height in feet: "))
        height_in = int(input("Enter additional inches: "))
        bmi = calculator.calculate_bmi_us(weight_lb, height_ft, height_in)
    else:
        print("Invalid unit system selected.")
        exit()

    print(f"Your calculated BMI is: {bmi:.2f}")
