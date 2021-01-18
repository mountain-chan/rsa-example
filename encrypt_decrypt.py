import binascii

import joblib
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

pub_key = RSA.importKey(joblib.load("pub_key"))
private_key = RSA.importKey(joblib.load("private_key"))

str_msg = 'Xin Chào Bạn'
msg = bytes(str_msg, "utf-8")

encryptor = PKCS1_OAEP.new(pub_key)
encrypted = encryptor.encrypt(msg)
print("Encrypted:", encrypted)
# print("Encrypted:", binascii.hexlify(encrypted))

decryption = PKCS1_OAEP.new(private_key)
decrypted = decryption.decrypt(encrypted)
print('Decrypted:', decrypted.decode())
