menu_catalog = {'pizza':250,'burger':180,'pasta':220,'sushi':400,'salad':120}

order_logs = [
    ("alice", ["pizza","burger","salad"], "Spice Hub"),
    ("bob", ["sushi","pasta"], "Zen Kitchen"),
    ("alice", ["burger","burger","pasta"], "Spice Hub"),
    ("charlie", ["pizza","sushi"], "Zen Kitchen"),
    ("bob", ["salad","pizza"], "Spice Hub"),
]

from collections import defaultdict

customer_spend = defaultdict(int)
restaurant_revenue = defaultdict(int)
item_freq = defaultdict(int)

total_value = 0

# Processing logs
for customer, items, restaurant in order_logs:
    order_total = sum(menu_catalog[item] for item in items)

    customer_spend[customer] += order_total
    restaurant_revenue[restaurant] += order_total
    total_value += order_total

    for item in items:
        item_freq[item] += 1

# Top customer
top_customer = max(customer_spend, key=customer_spend.get)

# Most ordered item
most_ordered = max(item_freq, key=item_freq.get)

# Average order value
avg_order_value = total_value / len(order_logs)

# Top 3 items
top_3_items = sorted(item_freq.items(), key=lambda x: x[1], reverse=True)[:3]


# ---- Output ----
print("Customer Spend:", dict(customer_spend))
print("Restaurant Revenue:", dict(restaurant_revenue))
print("Top Customer:", top_customer)
print("Most Ordered:", most_ordered)
print("Average Order Value:", avg_order_value)
print("Top 3 Items:", top_3_items)