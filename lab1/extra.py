func = "y\n"

for y in range(9, -1, -1):
    func += "| " + " " * (y * 2) + "*\n"


func += "+" + "-" * 20 + "> x\n"

print(func)
