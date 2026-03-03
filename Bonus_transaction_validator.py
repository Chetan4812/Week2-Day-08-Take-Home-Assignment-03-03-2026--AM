# transaction_validator.py
# Smart Transaction Validator – Rule-Based Fraud Detection

amount = float(input("Transaction amount (Rs): "))
category = input("Category (food/travel/electronics/other): ").lower()
hour = int(input("Hour of transaction (0-23): "))
daily_spent = float(input("Amount already spent today (Rs): "))
vip = input("Is VIP customer? (yes/no): ").lower()

# --- VIP Dynamic Limits (ternary operator used) ---
single_limit = 100000 if vip == "yes" else 50000
daily_limit = 200000 if vip == "yes" else 100000

food_limit = 10000 if vip == "yes" else 5000
electronics_limit = 60000 if vip == "yes" else 30000

# --- BLOCK RULES (Highest Priority) ---
if amount > single_limit:
    print("BLOCKED: exceeds single transaction limit")

elif daily_spent + amount > daily_limit:
    print("BLOCKED: exceeds daily spending limit")

elif category == "food" and amount > food_limit:
    print("BLOCKED: exceeds food category limit")

elif category == "electronics" and amount > electronics_limit:
    print("BLOCKED: exceeds electronics category limit")

# --- FLAG RULES ---
elif hour < 6 or hour > 23:
    print("FLAGGED: unusual transaction hour")

# --- APPROVED ---
else:
    print("APPROVED")