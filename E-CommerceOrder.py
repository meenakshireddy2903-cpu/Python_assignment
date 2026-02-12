import logging
logging.basicConfig(
    filename="order.log",
    level = logging.INFO,
    format="%(asctime)s - %(levelname)s -%(message)s"
)

class Order:
    platform = "Myntra"
    tax_percentage = 5  
    def __init__(self, cust_name, prod_name, quantity, price_per_item):
        self.cust_name = cust_name
        self.prod_name = prod_name
        self.quantity = quantity
        self.price_per_item = price_per_item
        self.order_status = False
    def place_order(self):
        self.order_status = True
        logging.info("Order placed successfully by %s", self.cust_name)

    def cancel_order(self):
        self.order_status = False
        logging.info("Order cancelled for %s", self.cust_name)

    def calculate_total_price(self):
        base_amount = self.quantity * self.price_per_item
        tax_amount = (base_amount * Order.tax_percentage) / 100
        final_amount = base_amount + tax_amount

        logging.info("Base Amount: %s", base_amount)
        logging.info("Tax Amount: %s", tax_amount)
        logging.info("Total Payable Amount: %s", final_amount)

    @classmethod
    def update_tax_percentage(cls, new_tax):
        cls.tax_percentage = new_tax
        logging.info("Tax percentage updated to: %s", cls.tax_percentage)


order1 = Order("Meenakshi", "Shirts", 2, 2000)

order1.place_order()
order1.calculate_total_price()

Order.update_tax_percentage(2)

order1.calculate_total_price()
order1.cancel_order()
