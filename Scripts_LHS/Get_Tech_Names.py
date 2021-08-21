f = open(r'D:\Mémoire\LHS_Test\EnergyScope\output_ref\technologies.txt', "r")
lines = f.readlines()
tech = [None]*104
for i in range (0,len(lines)-2) :
    line = lines[i+2].split()
    tech[i] = line[0]
    
print(tech)