
# Сумма чисел по модулю, стоящих на чётных и нечётных позициях 
BLUE = '\u001b[44m'
RED = '\u001b[41m'
RESET = '\u001b[0m'

sum_n = 0
sum_v = 0

K = [float(x) for x in open('sequence.txt')]
#print(len(K))

for x in range(0,len(K)):
    if x%2 == 1:
        sum_n = sum_n + abs(K[x])
    else:
        sum_v = sum_v + abs(K[x])
sum_all = sum_n + sum_v



percent_n = round((sum_n / sum_all) * 100, 3)
percent_v = round((sum_v / sum_all) * 100, 3)


s = 50
bar_n = int(round((percent_n / 100) * s))
bar_v = int(round((percent_v / 100) * s))

print(f"Нечётные {RED}{' ' * bar_n}{RESET} {percent_n}%")
print(f"Чётные   {BLUE}{' ' * bar_v}{RESET} {percent_v}%")