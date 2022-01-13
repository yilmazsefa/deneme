#RandomSecurityPassword

import string
from random import choice

characters = string.ascii_letters + string.punctuation + string.digits

password = "".join(choice(characters) for x in range(0,8))
print(password)
