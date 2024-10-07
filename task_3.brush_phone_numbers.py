import re

def normalize_phone(phone_number):
    # remove all but numbers and "+"
    cleaned_number = re.sub(r'\D', '', phone_number)
    
    if cleaned_number.startswith('380'):
        return f'+{cleaned_number}'
    
    if phone_number.strip().startswith('+'):
        return f'+{cleaned_number}'
    
    return f'+38{cleaned_number}'

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Brushed phone munbers:", sanitized_numbers)
