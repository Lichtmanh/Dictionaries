# Class Test
# Sample code to demonstrate dictionary objects

boss_monster = {"Strength":50, "Points":100, "Coins":10}
print(boss_monster)
boss_monster["Weapon"] = "Sword"
print(boss_monster)
del boss_monster["Weapon"]
print(boss_monster)
for key, value in boss_monster.items():
    print(f"The key is {key} and the value is {value}")
