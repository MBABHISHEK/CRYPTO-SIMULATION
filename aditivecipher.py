def create_alphabet_mapping():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping = {char: idx for idx, char in enumerate(alphabet)}
    return mapping

def encrypt_additive_with_mapping(message, key, alphabet_mapping):
    encrypted_message = ""
    for char in message:
             if char.isalpha():
                is_upper = char.isupper()
                char_upper = char.upper()
                position = alphabet_mapping[char_upper]
                new_position = (position + key) % 26
                encrypted_char = chr(new_position + ord('A'))
                # Convert back to the original case
                encrypted_char = encrypted_char.lower() if not is_upper else encrypted_char
                encrypted_message += encrypted_char
             else:
                encrypted_message += char
    return encrypted_message

def decrypt_additive_with_mapping(encrypted_message, key, alphabet_mapping):
    return encrypt_additive_with_mapping(encrypted_message, -key, alphabet_mapping)

choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()

if choice == 'E':
    message = input("Enter a message: ")
    
    key = int(input("Enter a key: "))
    alphabet_mapping = create_alphabet_mapping()
    result = encrypt_additive_with_mapping(message, key, alphabet_mapping)
    print("Encrypted message:", result)

elif choice == 'D':
    # Decryption
    encrypted_message = input("Enter an encrypted message: ")
    key = int(input("Enter the key: "))

    alphabet_mapping = create_alphabet_mapping()

    result = decrypt_additive_with_mapping(encrypted_message, key, alphabet_mapping)
    print("Decrypted message:", result)

else:
    print("Invalid choice. Please enter 'E' or 'D'.")
