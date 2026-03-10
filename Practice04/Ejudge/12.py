import json

obj1 = json.loads(input())
obj2 = json.loads(input())

differences = []

def compare(v1, v2, path=""):
    if isinstance(v1, dict) and isinstance(v2, dict):
        keys = set(v1.keys()) | set(v2.keys())
        for key in keys:
            new_path = f"{path}.{key}" if path else key
            compare(
                v1.get(key, None),
                v2.get(key, None),
                new_path
            )
    else:
        if v1 != v2:
            differences.append((path, v1, v2))

compare(obj1, obj2)

if not differences:
    print("No differences")
else:
    differences.sort(key=lambda x: x[0])
    for path, old, new in differences:
        old_str = "<missing>" if old is None and path.split('.')[-1] not in obj1 else json.dumps(old, separators=(",", ":"))
        new_str = "<missing>" if new is None and path.split('.')[-1] not in obj2 else json.dumps(new, separators=(",", ":"))

        if old is None:
            old_str = "<missing>"
        if new is None:
            new_str = "<missing>"

        print(f"{path} : {old_str} -> {new_str}")