import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    for letr in plaintext:
        if letr.isalpha():
            if letr.isupper():
                ciphertext += chr((ord(letr) + shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(letr) + shift - 97) % 26 + 97)
        else:
            ciphertext += letr
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ''
    for letr in ciphertext:
        if letr.isalpha():
            if letr.isupper():
                plaintext += chr((ord(letr) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(letr) - shift - 97) % 26 + 97)
        else:
            plaintext += letr
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    return best_shift
