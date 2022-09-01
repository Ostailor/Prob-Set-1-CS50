def main():
    hour = input("What time is it? ")

    if 7 <= convert(hour) <= 8:
        print("breakfast time")
    elif 12 <= convert(hour) <= 13:
        print("lunch time")
    elif 18 <= convert(hour) <= 19:
        print("dinner time")


def convert(time):
    hours, minutes = time.split(":")

    return float(hours) + (float(minutes) / 60)


if __name__ == "__main__":
    main()
