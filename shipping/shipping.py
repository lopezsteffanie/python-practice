# Creates variable for weight of package
weight = 41.5

# Ground Shipping
if weight <= 2.00:
  ground_cost = weight * 1.50 + 20.00
elif weight <= 6.00:
  ground_cost = weight * 3.00 + 20.00
elif weight <= 10.00:
  ground_cost = weight * 4.00 + 20.00
else:
  ground_cost = weight * 4.75 + 20.00

ground_premium_cost = 125.00

# Drone Shipping
if weight <= 2.00:
  drone_cost = weight * 4.50
elif weight <= 6.00:
  drone_cost = weight * 9.00
elif weight <= 10.00:
  drone_cost = weight * 12.00
else:
  drone_cost = weight * 14.25

# Checks price for each shipping method
print("Ground Shipping: $",ground_cost)
print("Ground Shipping Premium: $",ground_premium_cost)
print("Drone Shipping: $",drone_cost)