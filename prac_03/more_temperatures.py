import random
out_file = open("temps_input.txt", 'w')

for i in range(0,15):
    temps = random.uniform(-200,200)
    out_file.write(str(temps)+ "\n")