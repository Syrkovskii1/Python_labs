WHITE = '\u001b[47m'
RESET = '\u001b[0m'

def yzor():
    height = 5
    repeats = 3
    period = 4

    total_x = period * repeats + 1

    for y in range(height): #0-8
        
        for x in range(total_x): 
            
            pos = x % period
            
            if pos < height:
                y1 = pos
            else:
                y1 = period - pos

            y2 = (height - 1) - y1
        
            if y == y1 or y == y2:
                print(f"{WHITE}  {RESET}", end='')
            else:
                print('  ', end='')

        print()  

yzor()