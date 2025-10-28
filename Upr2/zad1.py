import hashlib

f = open("parola.txt")
password = f.read()
f.close()

binary_password = password.encode()

md5_hash = hashlib.md5(binary_password).hexdigest()
sha256_hash = hashlib.sha256(binary_password).hexdigest()
sha512_hash = hashlib.sha512(binary_password).hexdigest()

f = open("heshiranaParola.txt", "w")
f.write(f"MD5: {md5_hash}\nSHA256: {sha256_hash}\nSHA512: {sha512_hash}\n")
f.close()