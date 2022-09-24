thicknessFactor = 0.5

diameter = int(input('diameter (even): '))
thickness = diameter * thicknessFactor
for i in range(diameter + 1):
    for j in range(diameter + 1):
        if (i-diameter//2)**2 + (j-diameter//2)**2 - thickness <= (diameter/2)**2 <= (i-diameter//2)**2 + (j-diameter//2)**2 + thickness:
            print('**', end="")
        else:
            print('  ', end="")
    print('')
