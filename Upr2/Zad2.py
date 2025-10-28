ALPHABET = [
    "А","Б","В","Г","Д","Е","Ж","З","И","Й",
    "К","Л","М","Н","О","П","Р","С","Т","У",
    "Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ь","Ю","Я"
]

MOD = 31
SPACE = " "

def char_to_num(ch: str):
    ch = ch.upper()
    if ch == SPACE:
        return 0
    if ch in ALPHABET:
        return ALPHABET.index(ch) + 1
    return None

def num_to_char(n: int):
    n %= MOD
    if n == 0:
        return SPACE
    return ALPHABET[n - 1]

def caesar_encrypt(text: str, k: int) -> str:
    out = []
    for ch in text:
        n = char_to_num(ch)
        if n is None:
            out.append(ch)
        else:
            out.append(num_to_char((n + k) % MOD))
    return "".join(out)

def caesar_decrypt(text: str, k: int) -> str:
    return caesar_encrypt(text, -k)

if __name__ == "__main__":
    msg = "НИЕ СМЕ СТУДЕНТИ ОТ ТУ СОФИЯ"
    k = 2
    encrypted = caesar_encrypt(msg, k)
    print("Original:", msg)
    print("Encrypted:", encrypted)
    print("Decrypted:", caesar_decrypt(encrypted, k))