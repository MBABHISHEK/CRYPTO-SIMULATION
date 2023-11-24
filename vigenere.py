import string 

alphabets = list(string.ascii_lowercase)

def encryption(plain_text, key):
    cipher_text = ""
    key_index = 0

    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            key_char = key[key_index % len(key)]
            key_position = alphabets.index(key_char)
            new_position = (position + key_position) % 26
            cipher_text += alphabets[new_position]
            key_index += 1
        else:
             cipher_text += char

    print("The text after encryption is:", cipher_text)

def vigenere_decryption(cipher_text, key):
    plain_text = ""
    key_index = 0

    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            key_char = key[key_index % len(key)]
            key_position = alphabets.index(key_char)
            new_position = (position - key_position) % 26
            plain_text += alphabets[new_position]
            key_index += 1
        else:
            plain_text += char

    print("The text after Vigenere decryption is:", plain_text)

while True:
    print("----------------------------------------------------")
    print("Enter your choice:")
    choice = input("1.encryption \n2.decryption\n")
    
    if choice == "1":
        text = input("Type your message:").lower()
        key_given = input("Enter the key:").lower()
        if len(key_given) != len(text):
            print("Key is not having same length as that of plaintext..try again!!")
        else:    
            encryption(plain_text=text, key=key_given)
   
    elif choice == "2":
        text = input("Type your message:").lower()
        key_given = input("Enter the key:").lower()
        if len(key_given) != len(text):
            print("Key is not having same length as that of ciphertext..try again!!")
        else:   
            vigenere_decryption(cipher_text=text, key=key_given)
    
    else:
        print("Invalid choice.....Thank you!!")
        break

