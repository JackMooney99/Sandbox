'''Jack Mooney'''

def get_name():
    print("What is your name: ")
    name = input()

    return name


def main():
    name = get_name()
    letters = print_every_2nd_letter(name, 2)
    print("Letters are: {}".format(letters))


def print_every_2nd_letter(name, n):
    s = ''
    if len(name) != 0:
        for i in range(1, len(name)):
            if (i + 1) % n == 0:
                s += name[i]
        return s

    else:
        return "Error. Your name length is 0."


if __name__ == "__main__":
    main()