from password_utils import hash_password, verify_password

# Original password
password = "Ahmed@123"
password1 = "Ahmed@123"
# Generate hash
hashed = hash_password(password)
hashed1=hash_password(password1)
print("Original Password:", password)
print("Hashed Password:", hashed)
print("Hashed Password 1:", hashed1)

# Verify correct password
result = verify_password(password, hashed)

print("Correct Password:", result)

# Verify incorrect password
wrong_result = verify_password("Wrong@123", hashed)

print("Wrong Password:", wrong_result)

print(hashed==hashed1)

