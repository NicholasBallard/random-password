from string import ascii_lowercase, ascii_uppercase, digits, punctuation

import pyperclip
import numpy as np


def contains(i, x):
    return any([item in x for item in i])


def main(length):
    chars: list[str] = list(
        ascii_lowercase + ascii_uppercase + digits + punctuation
    )
    password = np.random.choice(chars, len)
    password = "".join(password)
    has_required_chars: bool = all([
        contains(ascii_lowercase, password),
        contains(ascii_uppercase, password),
        contains(digits, password),
        contains(punctuation, password),
    ])
    if not has_required_chars:
        main(length)
    return password


if __name__ == '__main__':
    import sys
    args = sys.argv
    password_length = 10 if not len(args) > 1 else int(args[-1])
    password = main(password_length)
    print(password)
    pyperclip.copy(password)
    print("password is copied to the clipboard")
