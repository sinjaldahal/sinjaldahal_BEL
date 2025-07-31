'''
with open("grocery.txt", "r") as f:
    lines = f.readlines()

print("\nGROCERY RECORDS:\n")
for line in lines:
    print(line.strip())

'''

f = open("grocery.txt", "r")

print("\nGROCERY RECORDS:\n")
line = ""
while True:
    char = f.read(1)
    if not char:
        if line != "":
            print(line)
        break
    if char == "\n":
        print(line)
        line = ""
    else:
        line += char

f.close()
