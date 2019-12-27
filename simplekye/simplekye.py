from hashlib import *
import itertools
import string
while True:
    for a in string.ascii_letters+string.digits
        if "28"+3*string.digits in b or "28"+3*string.ascii_letters in b:
            hashed = sha256(b).hexdigest()
            if "80" in hashed:
                index = hashed.index("28")
                if index < len(hashed)-5:
                    if hashed[index+2] == hashed[index+3] == hashed[index+4]:
                        print b, hashed, hashed[index+2]
