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
    if minutes.find("a.m.") == 3 or minutes.find("p.m.") == 3:
        if minutes.split(" ")[1] == "p.m." and hours == "12":
            minutes = minutes.split(" ")[0]
            return float(hours) + float(minutes) / 60
        if minutes.split(" ")[1] == "a.m." and hours == "12":
            minutes = minutes.split(" ")[0]
            return (float(hours) - 12) + float(minutes) / 60
        if minutes.split(" ")[1] == "a.m.":
            minutes = minutes.split(" ")[0]
            return float(hours) + float(minutes) / 60
        elif minutes.split(" ")[1] == "p.m.":
            minutes = minutes.split(" ")[0]
            return float(hours) * 12 + float(minutes) / 60
    else:
        return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()
