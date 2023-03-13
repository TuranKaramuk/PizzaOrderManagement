import csv
import datetime


class Topping:
    """Super class for sauce"""

    def __init__(self, component):
        self.component = component
        self.cost = ""
        self.description = ""

    def get_cost(self):
        """ Return total cost sauce and pizza """
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        """ Return description sauce and pizza """
        return self.component.get_description() + " " + Pizza.get_description(self)


class Pizza:
    """Main class for Pizza"""

    def __init__(self) -> None:
        """Initialize the Pizza class"""
        self.cost = ""
        self.description = ""

    def get_description(self) -> str:
        """Return Pizza description"""
        return self.description

    def get_cost(self) -> str:
        """Return Pizza cost"""
        return self.cost


class Margherita(Pizza):
    """Margherita pizza class created from Pizza main class"""

    def __init__(self) -> None:
        super(Margherita, self).__init__()
        self.description = "Margherita"
        self.cost = 15


class Classic(Pizza):
    """Margherita pizza class created from Pizza main class"""

    def __init__(self) -> None:
        super(Classic, self).__init__()
        self.description = "Classic"
        self.cost = 20


class TurkishPizza(Pizza):
    """Margherita pizza class created from Pizza main class"""

    def __init__(self) -> None:
        super(TurkishPizza, self).__init__()
        self.description = "Turkish Pizza"
        self.cost = 50


class PlainPizza(Pizza):
    """Margherita pizza class created from Pizza main class"""

    def __init__(self) -> None:
        super(PlainPizza, self).__init__()
        self.description = "Plain Pizza"
        self.cost = 10


class Olive(Topping):
    """ Olie Class """
    def __init__(self, pizza) -> None:
        super(Olive, self).__init__(pizza)
        self.cost = 10
        self.description = self.__class__.__name__


class Mushroom(Topping):
    """ Mushroom Class"""
    def __init__(self, pizza) -> None:
        super(Mushroom, self).__init__(pizza)
        self.cost = 17
        self.description = self.__class__.__name__


class GoatCheese(Topping):
    """ Goat Cheese Class"""
    def __init__(self, pizza) -> None:
        super(GoatCheese, self).__init__(pizza)
        self.cost = 27
        self.description = self.__class__.__name__


class Meat(Topping):
    """ Meat Class """
    def __init__(self, pizza) -> None:
        super(Meat, self).__init__(pizza)
        self.cost = 47
        self.description = self.__class__.__name__


class Onion(Topping):
    """ Onion class """
    def __init__(self, pizza) -> None:
        super(Onion, self).__init__(pizza)
        self.cost = 16
        self.description = self.__class__.__name__


class Corn(Topping):
    """ Corn class """
    def __init__(self, pizza) -> None:
        super(Corn, self).__init__(pizza)
        self.cost = 8
        self.description = self.__class__.__name__


def main():
    """ Main function for Pizza Order Management"""

    with open(
        r"C:\Users\TURANKA\Desktop\Development\PizzaOrderManagement\Menu.txt",
        "r",
        encoding="utf-8",
    ) as f:
        print(f.read())
    pizza = int(input("Please select a pizza: "))
    topping = int(input("Please select topping: "))

    match pizza:
        case 1:
            pizza = Classic()
        case 2:
            pizza = Margherita()
        case 3:
            pizza = TurkishPizza()
        case 4:
            pizza = PlainPizza()

    match topping:
        case 11:
            topping_pizza = Olive(pizza)
        case 12:
            topping_pizza = Mushroom(pizza)
        case 13:
            topping_pizza = GoatCheese(pizza)
        case 14:
            topping_pizza = Meat(pizza)
        case 15:
            topping_pizza = Onion(pizza)
        case 16:
            topping_pizza = Corn(pizza)

    cost = topping_pizza.get_cost()
    description = topping_pizza.get_description()

    name = input("Please enter your name: ")
    identity_number = input("Please enter your indentity number: ")
    credit_card_number = input("Please enter your credit card number: ")
    credit_card_pass = input("Please enter your credit card pass: ")

    # Creating order Dictionary
    order_dict = {
        "Name": name,
        "Identity Number": identity_number,
        "Credit Card Number": credit_card_number,
        "Credit Card Pass": credit_card_pass,
        "Description": description,
        "Cost": cost,
        "Time": datetime.datetime.now(),
    }

    # define row names for csv file
    row_names = [
        "Name",
        "Identity Number",
        "Credit Card Number",
        "Credit Card Pass",
        "Description",
        "Cost",
        "Time",
    ]

    # Writing database file with headers
    with open("Orders_Database.csv", "a", newline="", encoding="utf-8") as csvfile:
        dict_writer = csv.DictWriter(csvfile, fieldnames=row_names)

        dict_writer.writeheader()
        dict_writer.writerow(order_dict)


if __name__ == "__main__":
    main()
