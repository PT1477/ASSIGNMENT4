
try:
    f1 = open("sample.txt", 'r')
    read_f = f1.read()
    print(read_f)
except FileNotFoundError:
    print("file can't open")
finally:
    print("by")
