class Paypal:
    def send(self, amount):
        print(f"Sending amount {amount}")

class RazorPay:
    def make_payment(self,amount):
        print(f"Make payment {amount}")

class PaymentProvider:
    def __init__(self, provider):
        self.provider = provider
    
    def pay(self, amount):
        if isinstance(self.provider, Paypal):
            self.provider.send(amount)
        elif isinstance(self.provider , RazorPay):
            self.provider.make_payment(amount)

p = PaymentProvider(Paypal())

p.pay(2000)
