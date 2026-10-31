import json

menu = {
    "Burger": 120,
    "Pizza": 250,
    "Sandwich": 100,
    "Pasta": 180,
    "Fried Rice": 150,
    "Shawarma": 130,
    "Juice": 60
}
DISCOUNT_LIMIT = 500
DISCOUNT_PERCENTAGE = 10
DELIVERY_CHARGE = 40
def calculate_total(items):
    total = 0
    for item, quantity in items.items():
        if item not in menu:
            print("Invalid menu item:", item)
            return None
        if not isinstance(quantity, int) or isinstance(quantity, bool) or quantity <= 0:
            print("Invalid quantity for:", item)
            return None
        total += menu[item] * quantity
    return total
def apply_discount(total):
    if total >= DISCOUNT_LIMIT:
        discount = total * DISCOUNT_PERCENTAGE / 100
    else:
        discount = 0
    return discount
def calculate_bill(total):
    discount = apply_discount(total)
    discounted_total = total - discount
    final_total = discounted_total + DELIVERY_CHARGE
    return discount, final_total
def process_orders(orders):
    processed_orders = []
    total_revenue = 0
    highest_order = None
    highest_value = 0
    for order in orders:
        order_id = order.get("order_id", "Unknown")
        items = order.get("items", {})
        print("\n")
        print("Order ID:", order_id)
        if not items:
            print("Invalid Order: Empty order")
            continue
        subtotal = calculate_total(items)
        if subtotal is None:
            print("Order rejected due to invalid items.")
            continue
        discount, final_total = calculate_bill(subtotal)
        print("Subtotal: Rs.", subtotal)
        print("Discount: Rs.", discount)
        print("Delivery Charge: Rs.", DELIVERY_CHARGE)
        print("Final Amount: Rs.", final_total)
        total_revenue += final_total
        processed_orders.append({
            "order_id": order_id,
            "subtotal": subtotal,
            "discount": discount,
            "delivery_charge": DELIVERY_CHARGE,
            "final_total": final_total
        })
        if final_total > highest_value:
            highest_value = final_total
            highest_order = order_id
    return processed_orders, total_revenue, highest_order, highest_value
def generate_report(processed_orders, revenue, highest_order, highest_value):
    with open("sales_report.txt", "w") as file:
        file.write("FOOD DELIVERY - DAILY SALES REPORT\n")
        file.write("\n")
        file.write("Total Orders Processed: " + str(len(processed_orders)) + "\n")
        file.write("Total Revenue: Rs. " + str(round(revenue, 2)) + "\n")
        file.write("Highest Value Order: " + str(highest_order) + "\n")
        file.write("Highest Order Value: Rs. " + str(round(highest_value, 2)) + "\n\n")
        file.write("ORDER DETAILS\n")
        file.write("\n")
        for order in processed_orders:
            file.write(
                "Order ID: " + str(order["order_id"]) +
                " | Total: Rs. " + str(round(order["final_total"], 2)) + "\n"
            )
    print("\nSales report generated successfully!")
def main():
    print("\nFOOD DELIVERY ORDER SYSTEM")
    print("\nAVAILABLE MENU")
    for item, price in menu.items():
        print(item, " - Rs.", price)
    try:
        with open("sample_orders.json", "r") as file:
            orders = json.load(file)
    except FileNotFoundError:
        print("Error: sample_orders.json not found.")
        return
    except json.JSONDecodeError:
        print("Error: Invalid JSON format.")
        return
    if not isinstance(orders, list):
        print("Error: Orders must be stored as a list.")
        return
    processed_orders, revenue, highest_order, highest_value = process_orders(orders)
    print("\nSALES SUMMARY")
    print("Total Orders Processed:", len(processed_orders))
    print("Total Revenue: Rs.", round(revenue, 2))
    print("Highest Value Order:", highest_order)
    print("Highest Order Value: Rs.", round(highest_value, 2))
    generate_report(
        processed_orders,
        revenue,
        highest_order,
        highest_value
    )
if __name__ == "__main__":
    main()