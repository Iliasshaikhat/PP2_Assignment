import json

source = json.loads(input())
patch = json.loads(input())

def apply_patch(src, pch):
    for key, value in pch.items():
        if value is None:
            # удалить ключ если есть
            src.pop(key, None)
        elif key in src and isinstance(src[key], dict) and isinstance(value, dict):
            # если оба значения — словари, применяем рекурсивно
            apply_patch(src[key], value)
        else:
            # иначе заменяем или добавляем
            src[key] = value
    return src

result = apply_patch(source, patch)

print(json.dumps(result, separators=(",", ":"), sort_keys=True))