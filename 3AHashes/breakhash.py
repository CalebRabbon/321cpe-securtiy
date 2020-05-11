import bcrypt

password = b"Secrity"

hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print (hashed)
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print (hashed)
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print (hashed)
hashed = bcrypt.hashpw(password, bcrypt.gensalt())
print (hashed)
