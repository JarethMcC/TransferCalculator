fixed = []
height = []
fixedHeight = []

unfixed = open('FIFA21PlayerFile.txt', 'r', encoding='utf-8')
lines = unfixed.readlines()
for l in lines:
    fixed.append(l.strip().split(','))


for i in range(17125):
    height.append(fixed[i][3].strip('"').split('\''))
    
for i in range(17125):
        footConversion = float(height[i][0]) *  30.48
        inchConversion = float(height[i][1]) * 2.54
        totalConversion = inchConversion + footConversion
        fixedHeight.append(round(totalConversion))

writeFile = open('FixedHeight.txt', 'w')

for i in range(17125):
    writeFile.writelines(str(fixedHeight[i]))
    writeFile.writelines('\n')
    

