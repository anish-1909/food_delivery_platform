raw_menu = "pizza:250 burger:180 pasta:220 pizza:250 sushi:400 burger:180 salad:120"
menu_catalog = {}
for item in raw_menu.split():
    name, price = item.split(':')
    menu_catalog[name] = int(price)
    

unique_items = set(menu_catalog.keys())
sorted_menu = sorted(menu_catalog.items(), key=lambda x: x[1])



def search(query):
    return [item for item in menu_catalog if query.lower() in item.lower()]


def price_range(min_p, max_p):
    return [item for item, price in menu_catalog.items() if min_p <= price <= max_p]




print("Menu:", menu_catalog)
print("Sorted:", sorted_menu)
print("Search 'a':", search('a'))
print("Price range 150-250:", price_range(150, 250))
