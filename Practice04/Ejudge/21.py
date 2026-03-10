import importlib

q = int(input())

for _ in range(q):
    module_path, attr = input().split()

    try:
        module = importlib.import_module(module_path)
    except ImportError:
        print("MODULE_NOT_FOUND")
        continue

    if not hasattr(module, attr):
        print("ATTRIBUTE_NOT_FOUND")
    else:
        value = getattr(module, attr)
        if callable(value):
            print("CALLABLE")
        else:
            print("VALUE")