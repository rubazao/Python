
stuff = {'rope': 1,
         'torch': 6,
         'gold coin': 42,
         'dagger': 1,
         'arrow': 12}


def display_inventory(inventory: dict):
    print('\nInventory:')
    item_total = 0
    for k, v in inventory.items():
        item_total += v
        print(f'{v} {k}')
    print(f'Total number of items: {item_total}')


display_inventory(stuff)


def add_to_inventory(inventory: dict, added_items: list):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
display_inventory(inv)
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
