import json
import re
import sys

data = json.loads(input())
q = int(input())

# функция разбора пути
def parse_query(query):
    # разделяем по точкам, но сохраняем [index]
    parts = re.findall(r'[^.\[\]]+|\[\d+\]', query)
    return parts

for _ in range(q):
    query = input().strip()
    current = data
    valid = True

    for part in parse_query(query):
        if part.startswith("["):
            # индекс массива
            if not isinstance(current, list):
                valid = False
                break
            index = int(part[1:-1])
            if index < 0 or index >= len(current):
                valid = False
                break
            current = current[index]
        else:
            # доступ к словарю
            if not isinstance(current, dict) or part not in current:
                valid = False
                break
            current = current[part]

    if valid:
        print(json.dumps(current, separators=(",", ":")))
    else:
        print("NOT_FOUND")