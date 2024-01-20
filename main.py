def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    number_words = get_words(text)

    chars_dict = get_chars_dict(text)
    chars_sorted_list = format_report(chars_dict)

    print(f"--- Begin report of {path} ---")
    print(f"{number_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")


def format_report(num_chars_dict):
    result = []
    for char in num_chars_dict:
        result.append({"char": char, "num": num_chars_dict[char]})

    return sorted(result, key=lambda x: x['char'])


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for char in text:
        lowered = char.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


main()
