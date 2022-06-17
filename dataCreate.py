"""
File: dataCreate.py
Author: Tristen Miller
generates a 'data.txt' file with an XYZ matrix
"""

__author__ = "Tristen Miller"
__version__ = "0.1.0"
__license__ = "MIT"

def createData(x,y,z):
    print(x,y,z)
    print(range(x))
    f = open("data.txt",'w')
    #create an XYZ matrix:
    f.write('[')
    for i in range(z+1):
        for j in range(y+1):
            for k in range(x+1):
                f.write(str(k)+","+str(j)+","+str(i))
                if i==z and j==y and k==x:
                    break
                f.write('\n')
    f.write(']')    

    f.close()
    return

def main():
    x,y,z =input("Enter X Y Z dimensions ").split()
    x=int(x)
    y=int(y)
    z=int(z)
    createData(x,y,z)

if __name__ == "__main__":
    main()