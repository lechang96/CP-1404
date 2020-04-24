import random

number_per_line = 6
Min = 1
Max = 45


def main():
    times = int(input("How many quick picks do you want? "))
    for i in range(times):
        quick_picks = []
        for j in range(number_per_line):
            number = random.randint(Min,Max)
            while number in quick_picks:
                number = random.randint(Min,Max)
            quick_picks.append(number)
        quick_picks.sort(reverse=False)
        print(" ".join("{}".format(number) for number in quick_picks))

main()