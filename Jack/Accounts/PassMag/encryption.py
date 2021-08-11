from Cryptodome.Cipher import AES
import hashlib
import json
from secrets import token_bytes
from base64 import b64encode, b64decode


def encryptPassword(masterpassword):
    try:
        with open("003.bat00xxx.bin", "r+") as file:
            data = file.read()
        salt = token_bytes()
        PrivateKey = hashlib.scrypt(masterpassword.encode('utf-8'), salt=salt, n=2**14,  r=8, p=1, dklen=32)
        # cipher config
        cipher_config = AES.new(PrivateKey, AES.MODE_GCM)
        # return dictonary with the encrypted text
        cipher_text, tag = cipher_config.encrypt_and_digest(bytes(data, 'utf-8'))
        encryptionComponents = {
            'saltttt': b64encode(cipher_text).decode('utf-8'),
            'salttt': b64encode(salt).decode('utf-8'),
            'saltt': b64encode(cipher_config.nonce).decode('utf-8'),
            'salt': b64encode(tag).decode('utf-8'),
        }
        with open("config.json", "w") as config_file:
            json.dump(encryptionComponents, config_file)
    except Exception as e:
        print("\n❌❌❌ ErRoR OcCuRrEd 👉 Can't Encrypt Data  ❌❌❌")

def decryptPassword(masterpassword):
    try:
        with open("Jack/Accounts/PassMag/config.json", "rb") as config_file:
            data = json.load(config_file)
        salt = b64decode(data['salttt'])
        cipher_text = b64decode(data['saltttt'])
        nonce = b64decode(data['saltt'])
        tag = b64decode(data['salt'])
        private_key = hashlib.scrypt(masterpassword.encode('utf-8'),salt=salt, n=2**14, p=1, r=8, dklen=32)
        cipher = AES.new(private_key, AES.MODE_GCM, nonce=nonce)
        decrypted = cipher.decrypt_and_verify(cipher_text, tag)
        return decrypted.decode()
    except Exception as e:
        print("\n❌❌❌ ErRoR OcCuRrEd 👉 Can't Decrypt Data ❌❌❌")
