import random

def create_alphabet_mapping():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    mapping = {char: idx for idx, char in enumerate(alphabet)}
    return mapping

def generate_random_key(message_length):
    return [random.randint(0, 25) for _ in range(message_length)]

def encrypt_vernam_with_mapping(message, key, alphabet_mapping):
    encrypted_message = ""
    for char, key_value in zip(message, key):
            is_upper = char.isupper()
            char_upper = char.upper()
            position = alphabet_mapping[char_upper]
            new_position = (position + key_value) % 26
            encrypted_char = chr(new_position + ord('A'))
            encrypted_char = encrypted_char.lower() if not is_upper else encrypted_char
            encrypted_message += encrypted_char
    return encrypted_message

def decrypt_vernam_with_mapping(encrypted_message, key, alphabet_mapping):
    return encrypt_vernam_with_mapping(encrypted_message, key, alphabet_mapping)

choice = input("Enter 'E' for encryption or 'D' for decryption: ").upper()

if choice == 'E':
    message = input("Enter a message: ")
    alphabet_mapping = create_alphabet_mapping()
    
    # Generate a random key of the same length as the message
    key = generate_random_key(len(message))

    result = encrypt_vernam_with_mapping(message, key, alphabet_mapping)
    print("Encrypted message:", result)
    print("Key:", key)

elif choice == 'D':
    # Decryption
    encrypted_message = input("Enter an encrypted message: ")
    key = list(map(int, input("Enter the key (space-separated integers): ").split()))

    alphabet_mapping = create_alphabet_mapping()

    result = decrypt_vernam_with_mapping(encrypted_message, key, alphabet_mapping)
    print("Decrypted message:", result)

else:
    print("Invalid choice. Please enter 'E' or 'D'.")
