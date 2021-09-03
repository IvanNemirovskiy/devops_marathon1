import hashlib

def md5_hash(arg):
    m = hashlib.md5(arg.encode())
    hax_dig = m.hexdigest()
    print(f"Original string is: {arg}")
    print(f"md5 hash generated is \n{hax_dig}")

def sha1_hash(arg1):
    m1 = hashlib.sha1(arg1.encode())
    hex_dig1 = m1.hexdigest()
    print(f"Original string is: {arg1}")
    print(f"md5 hash generated is \n{hex_dig1}")