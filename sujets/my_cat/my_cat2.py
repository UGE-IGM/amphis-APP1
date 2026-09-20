from sys import argv

for i, arg in enumerate(argv):
    print(i, arg)

while True:
    try:
        line = input()
    except EOFError:
        break
    print(line)
