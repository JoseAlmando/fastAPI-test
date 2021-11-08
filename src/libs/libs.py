from cryptography.fernet import Fernet  

def encrypt_password(password):
    key = Fernet.generate_key()
    f = Fernet(key) 
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def decrypt_password(encrypted_password):
    key = Fernet.generate_key()
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password)
    return decrypted_password.decode()