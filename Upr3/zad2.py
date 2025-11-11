s_table = {
    '0': '3', '1': '4', '2': '1', '3': '2',
    '4': '0', '5': '9', '6': '7', '7': '6',
    '8': '5', '9': '8', 'A': 'D', 'B': 'C',
    'C': 'F', 'D': 'A', 'E': 'B', 'F': 'E'
}

inv_s_table = {v: k for k, v in s_table.items()}

def encrypt(block):
    return ''.join(s_table[c] for c in block)

def decrypt(block):
    return ''.join(inv_s_table[c] for c in block)

original = "FA01AD"
current = original
count = 0

print(f"Циклично криптиране за блок: {original}\n")

while True:
    current = encrypt(current)
    count += 1
    print(f"{count}: {current}")
    if current == original:
        print(f"\nБлокът се върна обратно до оригинала след {count} криптирания.")
        break
