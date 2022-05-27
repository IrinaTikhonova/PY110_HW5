import time


def time_from_pattern(time_, user_format):
    return time.strftime(user_format, time.gmtime(time_))


if __name__ == '__main__':
    print(time_from_pattern(time.time(), "%Y-%m-%d"))
