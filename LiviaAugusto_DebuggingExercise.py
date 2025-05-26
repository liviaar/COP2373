def calculate_discount(price, discount_rate):
    # Calculate the discount amount based on the price and discount rate.
    discount_amount = price * discount_rate
    return discount_amount


def apply_discount(price, discount_amount):
    # Apply the discount amount to the original price and return the new price.
    new_price = price - discount_amount
    return new_price


def main():
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05},
        {"name": "Computer", "price": "One thousand", "discount_rate": 0.01}
    ]

    for product in products:
        name = product["name"]
        price = product["price"]
        discount_rate = product["discount_rate"]

        # Handle string prices
        if type(price) == str:
            if price.isdigit():
                price = float(price)
            else:
                print(f"ERROR: Invalid input for {name} (price needs to be "
                      f"a number).\n")

        # Now check if price and discount_rate are both numbers
        if type(price) in [int, float] and type(discount_rate) in [int, float]:
            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

        print(f"Product: {product['name']}")
        print(f"Original Price: ${price}")
        print(f"Discount Amount: ${discount_amount}")
        print(f"Final Price: ${final_price}")
        print()


if __name__ == "__main__":
    main()
