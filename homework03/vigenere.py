def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = ""
    k = len(keyword)
    for i, letr in enumerate(plaintext):
        if letr.isalpha():
            shift = ord(keyword[i % k]) - (65 if keyword[i % k].isupper() else 97)
            char_ord = ord(letr)
            shifted_char_ord = char_ord + shift
            if letr.isupper():
                ciphertext += chr((shifted_char_ord - 65) % 26 + 65)
            else:
                ciphertext += chr((shifted_char_ord - 97) % 26 + 97)
        else:
            ciphertext += letr
    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    k = len(keyword)
    for i, letr in enumerate(ciphertext):
        shift = ord(keyword[i % k]) - (65 if keyword[i % k].isupper() else 97)
        char_ord = ord(letr)
        if letr.isalpha():
            shifted_char_ord = char_ord - shift
            if letr.isupper():
                plaintext += chr((shifted_char_ord - 65) % 26 + 65)
            else:
                plaintext += chr((shifted_char_ord - 97) % 26 + 97)
        else:
            plaintext += letr
    return plaintext
