from Crypto.Cipher import AES
import base64
import os

def pad(s):
    return s + (AES.block_size - len(s) % AES.block_size) * chr(AES.block_size - len(s) % AES.block_size)

def unpad(s):
    return s[:-ord(s[len(s)-1:])]

def encrypt(raw, key):
    raw = pad(raw)
    iv = os.urandom(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(iv + cipher.encrypt(raw.encode()))

def decrypt(enc, key):
    enc = base64.b64decode(enc)
    iv = enc[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(enc[AES.block_size:])).decode()

# Example usage
if __name__ == "__main__":
    key = os.urandom(32)  # AES-256 key
    message = "Sensitive data that needs encryption"
    encrypted_message = encrypt(message, key)
    print("Encrypted:", encrypted_message)
    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypted:", decrypted_message)
