import sys
import random
import string


def main():
    # mooodoore bad
    X = 11
    with open("testfile.txt", "w") as f:
        # Just some comment to get a commit
        f.write(''.join(random.choice(string.ascii_letters) for x in range(X)))


if __name__ == "__main__":
    main()