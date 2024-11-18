import csv

def restock_inventory(available_items, inventory_records, current_day):
    sold_units = 0 
    if current_day == 0:
        restock_amount = 2000
        available_items = 2000
        inventory_records.append([current_day, sold_units, restock_amount, available_items])
        
    elif current_day % 7 == 0: 
        restock_amount = 2000 - available_items
        available_items += restock_amount
        inventory_records.append([current_day, sold_units, restock_amount, available_items, ])  

    return available_items

