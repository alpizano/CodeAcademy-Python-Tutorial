def test(arg):
    if (type(arg) == int or type(arg) == float):
        return abs(arg)
    else:
        return "Nope"


def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if (city == "Charlotte"):
        return 183
    elif (city == "Tampa"):
        return 220
    elif (city == "Pittsburgh"):
        return 222
    elif (city == "Los Angeles"):
        return 475


def rental_car_cost(days):
    total = days * 40
    if (days >= 7):
        total = total - 50
    elif (days >= 3):
        total = total - 20
    return total


def trip_cost(city, days, spending_money):
    sum = rental_car_cost(days) + hotel_cost(days - 1) + plane_ride_cost(city) + spending_money
    return sum


print (trip_cost("Los Angeles", 5, 600))