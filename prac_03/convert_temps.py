out_file = open("temps_input.txt", 'r')
out_file2 = open("temps_output.txt",'w')

fahrenheit = out_file.readlines()
for i in fahrenheit:
    celsius = 5 / 9 * (float(i) - 32)
    out_file2.write(str(celsius) +"\n")