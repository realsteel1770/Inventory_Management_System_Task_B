import random
import csv 

def daily_sales(available_items, inventory_records, current_day):
    restocked_amount = 0 
    sold_units = random.randint(0, 200)
    if current_day % 7 != 0:
        available_items -= sold_units  
        inventory_records.append([current_day, sold_units,restocked_amount, available_items])

    return available_items
