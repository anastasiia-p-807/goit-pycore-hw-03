import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000 or quantity < 1 or quantity > (max - min + 1):
        return []

    random_numbers = set()
    while len(random_numbers) < quantity:
        random_numbers.add(random.randint(min, max))
    
    sorted_numbers = sorted(random_numbers)
    return sorted_numbers


lottery_numbers = get_numbers_ticket(16, 279, 6)
print("Lotery numbers:", lottery_numbers)