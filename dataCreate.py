f = open("data.txt",'w')
#create an XYZ matrix:
f.write('[')
for z in range(10):
    for y in range(10):
        for x in range(10):
            f.write(str(x)+","+str(y)+","+str(z))
            f.write('\n')
f.write(']')    

f.close()