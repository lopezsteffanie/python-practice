# Toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# Prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Number of $2 slices
num_two_dollar_slices = prices.count(2)

# Number of pizzas we sell
num_pizzas = len(toppings)
#print("We sell", num_pizzas, "different kinds of pizza!")

#Pizza topings and prices
pizza_and_prices = [[2, "pepperoni"], [6, "pineapple"], [1, "cheese"], [3, "sausage"], [2, "olives"], [7, "anchovies"], [2, "mushrooms"]]

pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]

priciest_pizza = pizza_and_prices[-1]

# Someone bought most expensive pizza, so let's remove it
pizza_and_prices.pop()

# Insert new Peppers Pizza in correct order
pizza_and_prices.insert(4, [2.5, "peppers"])
#print(pizza_and_prices)

# Sell 3 cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)