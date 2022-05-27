def the_inside_out_string(string_: str) -> str:
    if len(string_) % 2 == 0:
        result = string_[len(string_) // 2 - 1::-1] + string_[:len(string_) // 2 - 1:-1]
    else:
        result = string_[len(string_) // 2 - 1::-1] + string_[len(string_) // 2] + string_[:len(string_) // 2:-1]
    return result


if __name__ == '__main__':
    print(the_inside_out_string("synchronization"))
