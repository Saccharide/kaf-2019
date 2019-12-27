from hashlib import *
import itertools
import string
while True:
    for a in itertools.product(string.ascii_letters+string.digits,repeat=10):
        b=''.join(a)
        if "f1a9" in md5(sha1(b).hexdigest()).hexdigest():
            print md5(b).hexdigest(), b
            exit()
