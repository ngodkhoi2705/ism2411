# Reflection
# 1. The most surprising thing about Python lists is how flexible they are: you can slice them, change them in place, and use negative indexes to count from the end. I expected something more rigid, like a fixed range of spreadsheet cells.

# 2. In a past job I had to total and filter daily sales by hand in Excel every week. With a Python list I could load the numbers once, filter the days above a target, and get the average in a few lines instead of redoing the formulas each time.

# Exercise 1
print("--- Exercise 1: Build the list ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# Exercise 2
print("--- Exercise 2: Index Practice ---")
print(inventory[0])
print(inventory[-1])
middle = len(inventory) // 2
print(inventory[middle])

# Exercise 3
print("--- Exercise 3: Slicing ---")
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# Exercise 4
print("--- Exercise 4: Modify ---")
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)

# Exercise 5
print("--- Exercise 5: Tuple Comparison ---")
coords = (40.7128, -74.0060)
try:
    coords[0] = 99
except TypeError as error:
    print(f"TypeError caught: {error}")
    print("Tuples protect coordinates from being changed by accident.")
print(coords)

# Exercise 6
print("--- Exercise 6: Average of Sales ---")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count
print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

# Exercise 7
print("--- Exercise 7: Accumulator Pattern ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []
for price in prices:
    discounted.append(round(price * 0.9, 2))
print(prices)
print(discounted)

# Exercise 8
print("--- Exercise 8: Filter ---")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)
print(high_sales)
print(f"Count: {len(high_sales)}")
print(f"Avg: {sum(high_sales) / len(high_sales):.2f}")