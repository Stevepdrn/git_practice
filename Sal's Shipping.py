### REVIEW AND SIMPLFY ! ###


def ground_shipping_cost(weight):
    if weight <= 2:
        return weight * 1.50 + 20.00
    elif weight > 2 and weight <= 6:
        return weight * 3.00 + 20.00
    elif weight > 6 and weight <= 10:
        return weight * 4.00 + 20.00
    else:
        return weight * 4.75 + 20.00


print(ground_shipping_cost(8.4))

premium_gr_shipping = 125.00


def drone_shipping_cost(weight):
    if weight <= 2:
        return weight * 4.50
    elif weight > 2 and weight <= 6:
        return weight * 9.00
    elif weight > 6 and weight <= 10:
        return weight * 12.00
    else:
        return weight * 14.25


print(drone_shipping_cost(1.5))


def cheapest_ship_method(weight):
    if ground_shipping_cost(weight) < drone_shipping_cost(weight) and ground_shipping_cost(weight) < premium_gr_shipping:
        return "You should ship using ground shipping, it will cost $" + str(ground_shipping_cost(weight))
    elif premium_gr_shipping < drone_shipping_cost(weight) and premium_gr_shipping < ground_shipping_cost(weight):
        return "You should ship using premium ground shipping, it will cost $" + str(premium_gr_shipping)
    else:
        return "You should ship using drone shipping, it will cost $" + str(drone_shipping_cost(weight))


print(cheapest_ship_method(17))
print(cheapest_ship_method(4.8))
print(cheapest_ship_method(41.5))
print(cheapest_ship_method(1.5))
