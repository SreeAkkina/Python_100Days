alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(direction_shift, orginal_text, shift_amount):
    new_text = ""
    
    if direction_shift == 'decode':
        shift_amount = -shift_amount
    
    for letter in orginal_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            new_text += new_letter
        else:
            new_text += letter
    return new_text

"""def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    return cipher_text

def decrypt(encrypt_text, shifted_amount):
    decoded_text = ""
    for letter in encrypt_text:
        position = alphabet.index(letter)
        new_position = position - 5
        new_letter = alphabet[new_position]
        decoded_text += new_letter
    return decoded_text"""

cont = "yes"

while cont == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    text = input("Type your message: ").lower()
    shift = int(input("Type the shift number: "))
    
    if shift > 26:
        shift = shift % 26

    caeser_text = caeser(direction, text, shift)
    print(f"The {direction}d text is {caeser_text}")

    cont = input("Would you like to continue (yes or no) >>> ").lower()

"""if direction == 'encode':
    encrypted_text = encrypt(text, shift)
    print(f"The encrypted text is {encrypted_text}")

elif direction == 'decode':
    decode_text = decrypt(text, shift)
    print(f"The decoded text is {decode_text}")"""




