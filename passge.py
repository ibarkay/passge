import string
import random
import sys

log = ('''
 ______                 ______       
(_____ \               / _____)      
 _____) )___  ___  ___| /  ___  ____ 
|  ____/ _  |/___)/___) | (___)/ _  )
| |   ( ( | |___ |___ | \____/( (/ / 
|_|    \_||_(___/(___/ \_____/ \____)
                                      
password generator v0.0  by    ibarkay
       run with -h for Help
''')
help = ('''
run with number (default = 9) :
syntax  : python passge.py 10''')

def random_password_generator(leny):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
    size = 1
    leny = leny
    return ''.join(random.choice(chars) for x in range(size, leny))


if __name__ == '__main__':
    try:
        print("\033[1;32;32m" + log + "\033[m")
        ui = 9
        if len(sys.argv) > 1:
            if "-h" in sys.argv[1]:
                print("\033[1;32;32m" + help + "\033[m")
            else:
                ui = int(sys.argv[1])
        print('Password : '+ random_password_generator(int(ui)+1))
    except:
        print('Error')
