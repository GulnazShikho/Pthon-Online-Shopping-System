class Product:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.__price = price
        self.__quantity = quantity

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_quantity(self):
        return self.__quantity

    def set_quantity(self, quantity):
        self.__quantity = quantity


class Electronics(Product):
    def __init__(self, name, price, quantity, warranty_period):
        super().__init__(name, price, quantity)
        self.__warranty_period = warranty_period

    def get_warranty(self):
        return self.__warranty_period

    def set_warranty(self, warranty_period):
        self.__warranty_period = warranty_period


class Clothing(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.__size = size

    def get_size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size




