portfolio = {}

def add_stock():
    symbol = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = float(input("Enter quantity: "))
    buy_price = float(input("Enter buy price: "))
    
    portfolio[symbol] = {
        "quantity": quantity,
        "buy_price": buy_price,
        "current_price": buy_price
    }
    
    print(f"{symbol} added to portfolio.")

def update_price():
    symbol = input("Enter stock symbol to update: ").upper()
    if symbol in portfolio:
        new_price = float(input("Enter current market price: "))
        portfolio[symbol]["current_price"] = new_price
        print(f"Updated {symbol} price to ₹{new_price}")
    else:
        print("Stock not found.")

def view_portfolio():
    print("\n------ PORTFOLIO ------")
    total_value = 0
    for symbol, data in portfolio.items():
        quantity = data["quantity"]
        buy_price = data["buy_price"]
        current_price = data["current_price"]
        stock_value = quantity * current_price
        total_value += stock_value
        
        print(f"\nStock: {symbol}")
        print(f"Quantity: {quantity}")
        print(f"Buy Price: ₹{buy_price}")
        print(f"Current Price: ₹{current_price}")
        print(f"Current Value: ₹{stock_value}")
    
    print(f"\nTotal Portfolio Value = ₹{total_value}")
    print("------------------------\n")

def menu():
    while True:
        print("1. Add Stock")
        print("2. Update Stock Price")
        print("3. View Portfolio")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_stock()
        elif choice == "2":
            update_price()
        elif choice == "3":
            view_portfolio()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice, try again.")

menu()

