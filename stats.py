def get_book_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        file_contents = f.read()
    return file_contents


def get_num_words(text):
    words = text.split()
    amount_items = len(words)
    return amount_items


def get_num_char(text):
    amount_char = len(text)
    return amount_char


def get_char_count(text):
    alphabet = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }
    text = text.lower()
    for char in text:
        if char in alphabet:
            alphabet[char] += 1
    return alphabet


def order_char_count(alphabet):
    alphabet_list = list(alphabet.items())
    sorted_list = sorted(alphabet_list, key=lambda x: x[1], reverse=True)
    return [f"{char}: {count}" for char, count in sorted_list]
