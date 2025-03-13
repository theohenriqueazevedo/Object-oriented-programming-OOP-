# Definition of the Car class
class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    # Method to display car information
    def display_info(self):
        print(f"Brand: {self.brand} | Year: {self.year}")


def main():
    # Creating objects (instances of the Car class)
    car1 = Car("Toyota", 2020)
    car2 = Car("Ford", 2018)

    # Calling the class method
    car1.display_info()
    car2.display_info()


if __name__ == "__main__":
    main()
