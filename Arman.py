import random

def get_loot():
    loot_table = {
        "Common": 0.6,  # 60% ықтималдық
        "Uncommon": 0.25,  # 25%
        "Rare": 0.1,  # 10%
        "Legendary": 0.05  # 5%
    }
    return random.choices(list(loot_table.keys()), weights=loot_table.values())[0]

print(get_loot())  # Мысалы, "Common" немесе "Legendary"
