RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
RESET = '\u001b[0m'

 
def flag():
    
    height = 9
    width = int(height * 1.5 * 2)

    stripe_size = height // 3

    for i in range(height):
        if i < stripe_size:
            color = RED
        elif i < stripe_size * 2:
            color = WHITE
        else:
            color = BLUE
            
        print(f"{color}{' ' * width}{RESET}")


if __name__ == "__main__":
    flag()