for i in range(1, 21, 2):  # print odd numbers from 1 to 20
    print(i, end=' ')
print()

for i in range(0, 110, 10):  # count in 10s from 0 to 100
    print(i, end=' ')
print()

for i in range(20, 0, -1):  # count down from 20 to 1
    print(i, end=' ')
print()

number = int(input("Enter a number:"))   # ask for a number then print that many stars  all on one line
for i in range(number):
    print('*', end=' ')
print()

for i in range(1, number + 1):  # print n lines of increasing stars
    print('*' * i)
