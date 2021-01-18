from Crypto.PublicKey import RSA
import joblib

key_pair = RSA.generate(bits=3072, e=65537)

print(f"n={hex(key_pair.n)} \ne={hex(key_pair.e)} \nd={hex(key_pair.d)} \nq={hex(key_pair.q)} \np={hex(key_pair.p)}")

pub_key_pem = key_pair.publickey().export_key()
joblib.dump(pub_key_pem, "pub_key")

private_key_pem = key_pair.export_key()
joblib.dump(private_key_pem, "private_key")

print(pub_key_pem)
print(private_key_pem)
