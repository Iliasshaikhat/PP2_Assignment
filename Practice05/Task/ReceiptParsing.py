import re

# Exercise 1

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()
    
prices = re.findall(r"\d+\,\d+", text)

print(prices)
        
# Exercise 2

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

products = re.findall(r'(.+)\n\d+,\d+\s*x\s*\d+,\d+', text)

print(products)

# Exercise 3

import re

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

matches = re.findall(r'(\d+,\d+)\s*x\s*(\d+,\d+)', text)

total = 0
for qty, price in matches:
    qty = float(qty.replace(",", "."))
    price = float(price.replace(",", "."))
    total += qty * price

print(total)

# Exercise 4

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

match = re.search(r'\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}', text)

if match:
    print(match.group())
    
# Exercise 5

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

method = re.search(r'(Банковская карта|Наличные)', text)

if method:
    print(method.group())
    
# Exercise 6

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

receipt = re.search(r'Чек №(\d+)', text)

datetime = re.search(r'\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}', text)

payment = re.search(r'(Банковская карта|Наличные|Card|Cash)', text)

total = re.search(r'ИТОГО:\s*\n?([\d\s]+,\d{2})', text)

print(f'Name: {receipt.group()}')
print(f'Date: {datetime.group()}')
print(f'Payment: {payment.group()}')
print(f'Total: {total.group()}')
