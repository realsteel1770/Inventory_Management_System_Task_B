import random
import csv 

def daily_sales(available_items, inventory_records, current_day):
    if current_day % 7 == 0:
        sold_units = 0  
        available_items = 2000  
    else:
        sold_units = random.randint(0, 200)
        sold_units = min(sold_units, available_items)  
        available_items -= sold_units  
    available_items = max(0, available_items)
    inventory_records.append([current_day, sold_units, 0, available_items])

    return available_items
