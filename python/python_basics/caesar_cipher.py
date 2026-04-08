def caesar(text, shift, encrypt=True):
    """
    This function takes a string and an integer shift value, and returns the string encrypted using the Caesar cipher.
    """

    # Input validation
    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if not (1 <= shift <= 25):
        return 'Shift must be an integer between 1 and 25.'

    # Alphabet definition
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Shift logic
    n = shift if encrypt else -shift
    
    # Create shifted alphabet
    shifted_alphabet = alphabet[n % 26:] + alphabet[:n % 26]

    # Create translation table
    source = alphabet + alphabet.upper()
    target = shifted_alphabet + shifted_alphabet.upper()

    translation_table = str.maketrans(source, target)

    return text.translate(translation_table)

# Functions for encryption and decryption
def encrypt(text, shift): return caesar(text, shift) 
def decrypt(text, shift): return caesar(text, shift, encrypt=False)

# Test
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text)