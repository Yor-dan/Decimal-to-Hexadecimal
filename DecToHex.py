import math

def decToHex():
    try:
        hex = ['A', 'B', 'C', 'D', 'E', 'F']
        dec = [10, 11, 12, 13, 14, 15]
        result = []
        convert = []
        finished = False
        x = int(input("\nEnter a decimal number: "))
        while not finished:
           y = x % 16
           x = math.floor(x / 16)
           result.append(y)
           if x % 16 == x:
               finished = True
               result.append(x % 16)
        
        for i in reversed(result):
            if i in dec:
                index = dec.index(i)
                i = hex[index]
                convert.append(i)
            else:
                convert.append(i)
        
        print("\nHexadecimal equivalent: ",end="")                
        for i in convert:
            print(i,end="")
        
    except ValueError:
        print("Invalid Input!")
        
decToHex()