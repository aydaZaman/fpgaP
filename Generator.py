#import numpy as np
def frange(start, stop=None, step=None):
    # if set start=0.0 and step = 1.0 if not specified
    start = float(start)
    if stop == None:
        stop = start + 0.0
        start = 0.0
    if step == None:
        step = 1.0

    count = 0
    while True:
        temp = float(start + count * step)
        if step > 0 and temp >= stop:
            break
        elif step < 0 and temp <= stop:
            break
        yield temp
        count += 1

def y(x):
    return x**2-x**3

def floatoctal_convert(number, places = 3):
    result=""
    for i in range(8):
        number*=2
        if number<1:
            result=result+'0'
        else:
            result=result+'1'
            number-=1
    return result

with open("LUTval.txt","w") as file:

#    for i in np.arange(0, 256, 1/256):
    for i in frange(0,1,1/256):
#        print(i,y(i),floatoctal_convert(y(i)))
       file.write(floatoctal_convert(y(i)))
       file.write("\n")

with open("LUTval2.txt","w") as file:

#    for i in np.arange(0, 64, 1/64):
    for i in frange(0,1,1/64):

       file.write(floatoctal_convert(y(i)))
       file.write("\n")
#        file.write(y(i))
#        file.write("\n")
