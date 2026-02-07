import csv
import os
import numpy as np

# Build safe file path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(BASE_DIR, "orders.csv")

# Create empty lists
order_id        = []
customer_id     = []
restaurant_id   = []
delivery_time   = []
total_amount    = []
discount_applied = []
feedback_rating = []

# Read CSV
with open(file_path, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    print("CSV Columns:", reader.fieldnames)

    for row in reader:
        order_id.append(row["order_id"])
        customer_id.append(row["customer_id"])
        restaurant_id.append(row["restaurant_id"])
        delivery_time.append(row["delivery_time"])
        total_amount.append(float(row["total_amount"]))
        discount_applied.append(float(row["discount_applied"]))
        feedback_rating.append(float(row["feedback_rating"]))

# ────────────────────────────────────────────────
#   Now the data is loaded → do calculations here
# ────────────────────────────────────────────────

total_amount_np  = np.array(total_amount)
discount_np      = np.array(discount_applied)
rating_np        = np.array(feedback_rating)

net_amount = total_amount_np - discount_np

print("\nFinancial Summary:")
print("Total Revenue:       ₹", round(net_amount.sum(), 2))
print("Average Order Value: ₹", round(net_amount.mean(), 2))
print("Max Order Value:     ₹", round(net_amount.max(), 2))
print("Min Order Value:     ₹", round(net_amount.min(), 2))

high_value_orders = net_amount[net_amount >= 500]
print("High value orders (≥ ₹500) count:", len(high_value_orders))

# Fixed: you probably wanted sum of revenue, not count of orders
good_orders_mask = rating_np > 4
print("Revenue from well-rated orders (> 4): ₹", round(net_amount[good_orders_mask].sum(), 2))
print("Number of well-rated orders:         ", good_orders_mask.sum())

# Optional: quick overview
print("\nOrder IDs:", order_id)
print("Customers:", customer_id)
print("Restaurants:", restaurant_id)
print("Delivery Time:", delivery_time)
print("Total Amount:", total_amount)
print("Discount Applied:", discount_applied)
print("Ratings:", feedback_rating)