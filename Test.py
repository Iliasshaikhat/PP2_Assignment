import re

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
