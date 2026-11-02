# Lab 7

# Self Reflection Questions

# 1. The first bug I noticed was the missing colon in the for loop. I found it by reviewing the traceback. This showed me that I can identify basic syntax errors but need more practice with logic errors.
# 2. The apply_discount(price, tier) function takes an original price and membership tier, then returns the discounted price. Gold gets 15% off, silver 10%, and bronze 5%. A colleague could use it with a brief explanation.
# 3. AI Disclosure:
# I used ChatGPT to explain errors and debugging concepts. AI helped me better understand the errors rather than just giving me answers.

# --- Exercise 1 ---

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# Calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7% is ${tax1:.2f}") #    $7.00
print(f"Tax on $250 at 8% is ${tax2:.2f}") #    $20.00
print(f"Another tax: ${calculate_tax(150, 0.05):.2f}") #    $7.50

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price


# Calling the function

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"Price after {tier} discount: ${apply_discount(price, tier):.2f}")

# --- Exercise 3 ---

# Write it out manually first, then refactstor into a function

discounted = apply_discount(200, "gold")
tax = calculate_tax(discounted, 0.07)
after_tax = discounted + tax
print(f"After gold discount: ${discounted:.2f}")
print(f"After Tax: ${after_tax:.2f}")

# Refactored into a function
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, "gold", 0.07):.2f}")

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
   total = final_price(price, tier, 0.07)
   print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# --- Exercise 6 ---

x = 100 # apple Global Variable

def double_it():
    x = 999 # another apple (not the same one as before) # Local Variable # Use "Global" if you want to get the local variable
    return x * 2

print(x)
print(double_it())
print(x)


