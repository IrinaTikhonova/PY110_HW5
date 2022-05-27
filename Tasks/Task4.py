def get_strong_string(str_: str):
    data = str_.split()
    dict_of_results = {}
    for word in data:
        word_strong = 0
        for ch in word:
            if ch.isalpha():
                word_strong += ord(ch)

        dict_of_results[word_strong] = word
    max_val = max(dict_of_results.items())
    return f"Слово {max_val[1]} победило, набрав {max_val[0]} баллов"


if __name__ == '__main__':
    print(get_strong_string("самое сильное слово в строке"))
