#  stock portfolio traker

stock_prices = {
    "AAPL": 150,
    "TSLA": 250,
    "GOOGL": 275,
    "MSFT": 120,
    "AMZN": 140
}

# Dictionary to store user's stock and quantity
portfolio = {}

print("📊 Enter your stock portfolio (type 'done' when finished):")

# Input loop
while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print(f"❌ '{stock}' not found in stock price list.")
        continue
    try:
        qty = int(input(f"Enter quantity of {stock}: "))
        if qty <= 0:
            print("⚠️ Quantity must be positive.")
            continue
        portfolio[stock] = portfolio.get(stock, 0) + qty
    except ValueError:
        print("⚠️ Invalid number. Please enter an integer.")

# Display results
print("\n🧾 Your Portfolio Summary:")
total_investment = 0
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares × ₹{price} = ₹{value}")

print(f"\n💰 Total Investment Value: ₹{total_investment}")