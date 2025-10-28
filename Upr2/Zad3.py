def letter_to_num(ch: str) -> int:
    return ord(ch.upper()) - ord('A')

def num_to_letter(n: int) -> str:
    return chr((n % 26) + ord('A'))

def trithemius_encrypt(text: str, key: str) -> str:
    text = text.upper()
    key = key.upper()
    cipher = []

    for i, ch in enumerate(text):
        p = letter_to_num(ch)
        k = letter_to_num(key[i % len(key)])
        c = (p + i + k) % 26
        cipher.append(num_to_letter(c))

    return "".join(cipher)


message = "SETSRELATIONSANDFUNCTIONS"
key = "PROGRAM"
ciphertext = trithemius_encrypt(message, key)

print("Original:", message)
print("Key:", key)
print("Encrypted:", ciphertext)