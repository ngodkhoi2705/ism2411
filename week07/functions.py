# Self-Assessment

# Q1: The first bug I spotted was the missing colon in the for loop. I found it from the traceback, which pointed at line 10. The IndexError was harder, so I needed an explanation before I saw the <= problem. I'm better at reading syntax errors than logic errors, so next time I'll print i inside the loop first.

# Q2: apply_discount(price, tier) takes a price and a tier name as a string. It returns the price after the discount: 15% off for "gold", 10% for "silver", 5% for "bronze", and no discount for anything else. A colleague could use it without reading the body.

# Q3: I used Claude to explain the error messages from broken_sales.py and to check my functions against the instructions. It also showed me the fixes, so it shortcut some of my own debugging.

# Exercise 1

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}")
print(f"Tax on $250 at 8%: ${tax2:.2f}")

# Exercise 2

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver" :
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

original_price = 200
for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3

def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax

print(f"final_price(200, 0.07, 'gold') = ${final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4

orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, rate, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# Exercise 5
# Bug 1: the loop had total = sale, which replaced total with the current sale on every pass, so the result was just the last sale instead of the sum. Fix: change it to total = sale + total so each sale gets added to the total.
# Bug 2: the for loop was missing a colon at the end of the line. Fix: add ":" after "for sale in sales".
# Bug 3: the while loop used i <= len(sales), so i went one past the last index and caused an IndexError. Fix: change <= to <.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total = sale + total
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# Exercise 6

x = 100
def double_it():
    x = 999
    return x * 2 
print(x)
print(double_it())
print(x)