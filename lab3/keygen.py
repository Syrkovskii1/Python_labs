import random

alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


def generate_block(digit):
    chars = []
    for i in range(4):
        random_char = random.choice(alph)
        chars.append(random_char)

    chars.append(digit)
    random.shuffle(chars)
    return ''.join(chars)


def generate_key(hex_input):
    hex_input = hex_input.strip()
    hex_input = hex_input.upper()

    if len(hex_input) != 5:
        raise ValueError('Нужно ввести ровно 5 символов!')

    valid_hex = '0123456789ABCDEF'
    for char in hex_input:
        if char not in valid_hex:
            raise ValueError('Символ ' + char + ' не является шестнадцатеричным!')

    
    dec_num = int(hex_input, 16)
    dec_str = str(dec_num)



    digit_1 = dec_str[0]
    digit_2 = dec_str[1]
    digit_3 = dec_str[2]

    tail = dec_str[-2:]

    block_1 = generate_block(digit_1)
    block_2 = generate_block(digit_2)
    block_3 = generate_block(digit_3)

    full_key = block_1 + '-' + block_2 + '-' + block_3 + ' ' + tail

    return full_key



#test_hex = '54CD1'
#print(test_hex)
#key = generate_key(test_hex)
#print(key)
