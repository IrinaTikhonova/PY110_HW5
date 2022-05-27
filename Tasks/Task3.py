from itertools import count


def wave_eternal(text: str) -> str:
    for i in count(0, 1):
        if i < len(text):
            if text[i] != " ":
                yield text[:i] + text[i].upper() + text[i + 1:]
        elif i > len(text):
            k = i % len(text)
            if text[-k] != " ":
                if k != 1:
                    yield text[:-k] + text[-k].upper() + text[-k + 1:]
                else:
                    yield text[:-k] + text[-k].upper()


if __name__ == '__main__':

    wave_ = wave_eternal("hello world")
    for _ in range(20):
        print(next(wave_))
