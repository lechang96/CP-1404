import random
out_file = open("results.txt", 'w')

def main():
    times = int(input("Please enter a number:"))
    for i in range(0,times):
        score = random.randint(0,100)
        if score < 0 or score >100:
            print("Invalid score")
        elif score >= 50 and score <= 90:
            out_file.write("{} is Passable\n".format(score))
        elif score > 90:
            out_file.write("{} is Excellent\n".format(score))
        else:
            out_file.write("{} is Bad\n".format(score))

main()