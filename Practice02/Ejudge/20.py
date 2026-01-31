
n = int(input())


document = {}


for _ in range(n):
    parts = input().split()
    cmd = parts[0]
    
    if cmd == "set":
        key = parts[1]
        value = parts[2]
        document[key] = value
    
    elif cmd == "get":
        key = parts[1]
        if key in document:
            print(document[key])
        else:
            print(f"KE: no key {key} found in the document")
