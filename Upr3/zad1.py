# Прост stream cipher с видим keystream и проверка при декриптиране
# Няма нови импорти

def generate_stream(seed: int) -> int:
    # прост псевдослучаен генератор (примерен LCG)
    return (seed * 49 + 10) % 256

def keystream_from_key(key: bytes, n: int) -> bytes:
    # seed от първия байт на ключа (ако ключът е празен -> 0)
    seed = key[0] if len(key) > 0 else 0
    out = bytearray()
    for _ in range(n):
        seed = generate_stream(seed)
        out.append(seed)
    return bytes(out)

def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b))

def stream_cipher(data: bytes, key: bytes) -> bytes:
    ks = keystream_from_key(key, len(data))
    # показваме keystream-а в hex (по заявка)
    print("Keystream (hex):", ks.hex())
    return xor_bytes(data, ks)

# --- КРИПТИРАНЕ ---
key_input = input("Въведи ключ за криптиране: ")
msg_input = input("Въведи съобщение: ")

key = key_input.encode("utf-8")
plaintext = msg_input.encode("utf-8")

# при криптиране искаме да видим keystream-а — затова извикваме stream_cipher директно
keystream_for_display = keystream_from_key(key, len(plaintext))
print("Keystream (hex):", keystream_for_display.hex())

encrypted = xor_bytes(plaintext, keystream_for_display)
print("Криптирано (hex):", encrypted.hex())

# --- ДЕКРИПТИРАНЕ ---
key_input2 = input("Въведи ключ за декриптиране: ")
key2 = key_input2.encode("utf-8")

# при декриптиране не е нужно да принтираме keystream-а, но можем — тук не го правим повторно
decrypted_bytes = xor_bytes(encrypted, keystream_from_key(key2, len(encrypted)))

# ако декриптираното не е валиден UTF-8 -> смятаме че е грешен ключ
try:
    decrypted_text = decrypted_bytes.decode("utf-8")
    print("Декриптирано:", decrypted_text)
except UnicodeDecodeError:
    print("Грешен ключ – декриптираното не е валиден текст.")