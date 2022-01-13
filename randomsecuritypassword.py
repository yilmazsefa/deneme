#RandomSecurityPassword

import string
from random import choice

characters = string.ascii_letters + string.punctuation + string.digits

a=1

while a>0:
    password = "".join(choice(characters) for x in range(0,8))
    print(password)
    a-=1
