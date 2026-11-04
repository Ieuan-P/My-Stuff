import random
# ===== FUNCTION DEFINITIONS =====

def display_intro():
    pass # ===== Code here =====
    print (f"=== Treasure Hunt Adventure ===\nExplore 3 locations and collect random gold!")
def choose_location():
    pass # ===== Code here =====
    return input("Choose a location (cave / forest / beach)").lower()
def explore_location(loc):
    pass # ===== Code here =====
    if loc == "cave":
        return random.randint(5,8)
    elif loc == "forest":
        return random.randint(1,10)
    elif loc == "beach":
        return random.randint(0,20)
    else:
        return 0
def display_location_result(loc, g_found):
    pass # ===== Code here =====
    print (f"You explored the {loc} and found {g_found} gold!")
def display_final_result(total_g):
    pass # ===== Code here =====
    if total_g >= 20:
        print (f"Total Gold: {total_g}\nYou Win! Rich Explorer!")
    else:
        print (f"Total gold: {total_g}\nYou Lose! Try Again!")
# ===== MAIN PROGRAM =====

total_gold = 0

display_intro()

for i in range(3):
    location = choose_location()
    gold_found = explore_location(location)
    total_gold += gold_found
    display_location_result(location, gold_found)

display_final_result(total_gold)