import json
from datetime import datetime
from tax_rules_manager import get_tax_rate, update_tax_structures

SALES_FILE = "sales.json"


def load_sales():
    """Load sales data from JSON file."""
    try:
        with open(SALES_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_sales(sales):
    """Save sales data to JSON file."""
    with open(SALES_FILE, "w") as file:
        json.dump(sales, file, indent=2)


def calculate_invoice(customer_name, country_code, items):
    """
    Calculate sales invoice for a customer.
    Each item: {"ItemName": str, "ItemRate": float, "ItemQuantity": int}
    """
    sales = load_sales()
    today = datetime.now().strftime("%Y-%m-%d")

    for item in items:
        item_name = item["ItemName"]
        item_rate = float(item["ItemRate"])
        item_qty = int(item["ItemQuantity"])
        item_amount = item_rate * item_qty

        tax_rate = get_tax_rate(item_rate, country_code)
        tax_amount = item_amount * (tax_rate / 100)
        total_amount = item_amount + tax_amount

        sales.append({
            "TransactionDate": today,
            "CustomerName": customer_name,
            "CountryCode": country_code,
            "ItemName": item_name,
            "ItemRate": item_rate,
            "ItemQuantity": item_qty,
            "ItemAmount": item_amount,
            "TaxAmount": tax_amount,
            "TotalAmount": total_amount
        })

    save_sales(sales)
    print(f"Invoice added for {customer_name} ({country_code})")


def show_all_sales():
    """Display all sales records."""
    sales = load_sales()
    if not sales:
        print("No sales records found.")
        return

    print("\n--- All Sales Records ---")
    for record in sales:
        print(f"""
        Date: {record['TransactionDate']}
        Customer: {record['CustomerName']}
        Country: {record['CountryCode']}
        Item: {record['ItemName']}
        Rate: {record['ItemRate']}
        Qty: {record['ItemQuantity']}
        Amount(before tax): {record['ItemAmount']}
        Tax: {record['TaxAmount']}
        Total(after tax): {record['TotalAmount']}
        ----------------------------------
        """)


def add_new_transaction():
    """Allow user to add new transaction interactively."""
    customer_name = input("Enter Customer Name: ")
    country_code = input("Enter Country Code: ").upper()

    items = []
    while True:
        item_name = input("Item Name: ")
        item_rate = float(input("Item Rate: "))
        item_qty = int(input("Item Quantity: "))
        items.append({
            "ItemName": item_name,
            "ItemRate": item_rate,
            "ItemQuantity": item_qty
        })

        more = input("Add another item? (y/n): ").lower()
        if more != "y":
            break

    calculate_invoice(customer_name, country_code, items)


def menu():
    """Main interactive menu."""
    while True:
        print("""
        - TAX MASTER MENU -
        1. Show All Sales
        2. Add New Transaction
        3. Update Tax Structure
        4. Exit
        """)
        choice = input("Enter choice: ")

        if choice == "1":
            show_all_sales()
        elif choice == "2":
            add_new_transaction()
        elif choice == "3":
            update_tax_structures()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    menu()
