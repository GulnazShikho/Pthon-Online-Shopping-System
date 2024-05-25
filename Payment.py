class Payment:
    def process_payment(self):
        raise NotImplementedError("Subclasses must implement process_payment method.")


class CreditCardPayment(Payment):
    def process_payment(self):
        print("Credit card payment processed successfully.")


class PaypalPayment(Payment):
    def process_payment(self):
        print("PayPal payment processed successfully.")

