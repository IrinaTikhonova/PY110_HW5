def binary_to_decimal(list_of_numbers: list) -> int:
    return int("".join([str(x) for x in list_of_numbers]), base=2)


if __name__ == '__main__':
    print(binary_to_decimal([0, 1, 1, 0]))
