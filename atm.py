'''
    `atm.py`

    ATM Problem Generator
    Information System Security and IT Laws class, IT KMITL.
    by Teerapat Kraisrisirikul

    Getting Started
    - Just run this code file.
    - Global variable(s) can be edited to your liking.
'''

from random import randint

DISPLAY_COLUMNS = 5

def main():
    ''' Main Function '''
    print()
    print('- ATM Problem Generator -'.center(25))
    print('by Teerapat K.'.center(25))

    while True:
        print()
        print('[NOTICE] Input ATM code number base, must be from 10 to 36.')
        base = int(input('(Input) '))

        if base >= 10:
            break
        
        print()
        print('[ERROR] Number base must be at least 10. Please try again.')
    
    print()
    print('[NOTICE] Input ATM card amount, more cards, more accurate.')
    card_amount = int(input('(Input) '))

    personal_code = ''.join([alphabetical(randint(0, base - 1)) for _ in range(4)])
    atm_real_code = [('%04i' % randint(0, 9999))
                     for _ in range(card_amount)]
    atm_encoded_code = [encode(i, personal_code, base=base) for i in atm_real_code]

    print()
    print('[NOTICE] Here are {} encoded ATM codes.'.format(len(atm_encoded_code)))
    print()
    display(atm_encoded_code, col=DISPLAY_COLUMNS)
    print()
    print('[NOTICE] Now start decoding. Input the answer below.')
    print('[NOTICE] If you want to give up, just type \'give up\' in the answer box.')

    while True:
        print()
        answer = input('(Answer) ').strip().upper()
        if answer.strip().lower() == 'give up':
            print('[NOTICE] You gave up.')
            break
        elif answer == personal_code:
            print('[NOTICE] Correct answer!')
            break
        else:
            print('[NOTICE] Wrong Answer!')

    print()
    print('The answer (personal code) is {}.'.format(personal_code))
    print()
    print('Here are {} decoded ATM codes.'.format(len(atm_real_code)))
    print()
    display(atm_real_code, col=DISPLAY_COLUMNS)
    print()


def display(atm_code_list, col=5):
    ''' Display ATM code in columns '''
    for i in range(len(atm_code_list)):
        print(atm_code_list[i], end='\t' * (i % col != (col - 1)) + '\n' * (i % col == (col - 1)))

def alphabetical(num):
    ''' Converts number to alphabetical format, supports hexadecimal. '''
    return '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[num]


def encode(data, key, base=16):
    ''' Encode '''
    return ''.join([encode_digit(data[i], key[i], base=base) for i in range(len(data))])


def encode_digit(data, key, base=16):
    ''' Encode a single digit '''
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:base]
    return digits[(digits.index(data) - digits.index(key)) % base]


def decode(data, key, base=16):
    ''' Decode '''
    return ''.join([decode_digit(data[i], key[i], base=base) for i in range(len(data))])


def decode_digit(data, key, base=16):
    ''' Decode a single digit '''
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:base]
    return digits[(digits.index(data) + digits.index(key)) % base]


main()
