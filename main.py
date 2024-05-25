import Products
import Payment


# Creating an instance of Electronics
laptop = Products.Electronics("Laptop", 1500, 10, "2 years")
print(f"Name: {laptop.get_name()}")
print(f"Price: {laptop.get_price()}")
print(f"Quantity: {laptop.get_quantity()}")
print(f"Warranty Period: {laptop.get_warranty()}")

# Creating an instance of Clothing
shirt = Products.Clothing("Shirt", 30, 50, "L")
print(f"Name: {shirt.get_name()}")
print(f"Price: {shirt.get_price()}")
print(f"Quantity: {shirt.get_quantity()}")
print(f"Size: {shirt.get_size()}")

# Exemplary usage of Payment classes
credit_card_payment = Payment.CreditCardPayment()
credit_card_payment.process_payment()

paypal_payment = Payment.PaypalPayment()
paypal_payment.process_payment()
