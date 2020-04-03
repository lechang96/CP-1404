#1
name = input("Please enter your name:")
out_file = open("name.txt", 'w')
out_file.write(name)

#2
out_file = open("name.txt", 'r')
print("Your name is {}.".format(out_file.readline()))

#3
out_file = open("numbers.txt", 'r')
firstNum = int(out_file.readline())
secondNum = int(out_file.readline())
print(firstNum+secondNum)

#4
sum = 0
out_file = open("numbers.txt", 'r')
for line in out_file:
    sum += int(line.strip())
print(sum)

