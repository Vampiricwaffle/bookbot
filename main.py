def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(file_contents)
        words = file_contents.split()
        print(f"There are {len(words)} words in this book")
        chars_dict = get_chars_dict(file_contents)
        # print(chars_dict)
        sorted_letters = sort_letters(chars_dict)
        for item in sorted_letters:
            print(f"the '{item['char']}' character was found {item['num']} times")

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_on(dict):
    return dict["num"]

def sort_letters(text):
    list = []
    for char, count in text.items():
        if char.isalpha():
            char_info = {'char': char, 'num': count}
            list.append(char_info)
    
    list.sort(reverse=True, key=sort_on)
    return list
# def character_amount(text):
    # lower_case = text.lower()
    # alphabet = "qwertyuiopasdfghjklzxcvbnm"
    # count = {}
    # for letter in alphabet:
    #     count[f'letter_{letter}'] = 0
    #     for i in lower_case:
    #         count[f'letter_{letter}'] += 1
    #     print(f"the '{letter}' character was found {count[f'letter_{letter}']} times")
main()