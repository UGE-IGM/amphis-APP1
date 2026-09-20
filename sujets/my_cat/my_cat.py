while True:
    try:
        line = input()
    except EOFError:
        break
    print(line)
