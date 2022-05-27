def wave(text: str) -> str:
    list_ = []
    for i in range(0, len(text)):
        if not text[i] == " ":
            result = text[:i] + text[i].upper() + text[i + 1:]
            list_.append(result)
    return "\n".join(list_)


if __name__ == '__main__':
    print(wave("hello world"))
