from faker import Faker

import pickle

fake = Faker("RU_ru")

# dict_of_possible_data = {
#     "Простой профиль": fake.simple_profile(),
#     "Имя и фамилия": fake.name(),
#     "Номер телефона": fake.phone_number(),
#     "Профессия": fake.job(),
#     "Адрес": fake.address()
# }


def user_generator(k: int) -> dict:
    list_of_users = {}
    for i in range(1, k):
        list_of_users[i] = fake.name(), fake.phone_number(), fake.job()
    return list_of_users


if __name__ == '__main__':
    list_of_users = user_generator(10)

    filename = "Cписок пользователей.txt"
    with open(filename, "wb") as f:
        pickle.dump(list_of_users, f)

    with open(filename, "rb") as f:
        new = pickle.load(f)
