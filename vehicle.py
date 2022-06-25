# M3 Lab

# Creating a Super class.
class Vehicle():
    # Creating the type attribute here then passing it.
    def __init__(self):
        self.type = input('What type of vehicle?:')


class Automobile(Vehicle):
    # Inititalizing the variables with user input.
    def __init__(self):
        super().__init__()

        self.year = input('What year is your vehicle?:')
        self.make = input('What is your make?: ')
        self.model = input('What is your model?: ')
        self.doors = input('How many doors?: ')
        self.roof = input('Solid roof/ Sunroof / Other?: ')

    # This generates the final output.
    def create(self):
        return(
            print(f' Vehicle type: {self.type} \n', f'Year: {self.year} \n', f'Model: {self.model} \n',
                  f'Make: {self.make} \n', f'Number of Doors: {self.doors} \n', f'Type of roof: {self.roof}')
        )


# Initilizing the class
vehicle_info = Automobile()

# Calling the function that outputs the info.
vehicle_info.create()
