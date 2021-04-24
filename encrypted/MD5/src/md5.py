import hashlib


salt = "randomstring"
passwd = "123456"
print(hashlib.md5((salt+passwd).encode('utf-8')).hexdigest())
