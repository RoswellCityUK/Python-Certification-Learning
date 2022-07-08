"""
Program is calculating charge for parcel regarding provided formula
"""


def calculate_parcel_price(distance, item_count):
    charge = 0
    cost_per_mile = 1.00
    cost_of_first_item = 5.00
    cost_per_item = 2.00

    charge += distance * cost_per_mile
    charge += cost_of_first_item + cost_per_item * (item_count - 1)

    return charge


price_to_pay = calculate_parcel_price(15, 10)
print(f"£{price_to_pay:.2f}")
