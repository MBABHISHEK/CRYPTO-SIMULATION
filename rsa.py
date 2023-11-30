import random 
import math

def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True   

def generate_prime(min, max):
    prime = random.randint(min, max)
    while not is_prime(prime):
        prime = random.randint(min, max)
    return prime    

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d

def encrypt(message, e, n):
    message_encoded = [ord(c) for c in message]
    ciphertext = [pow(c, e, n) for c in message_encoded]
    return ciphertext

def decrypt(ciphertext, d, n):
    decryption = [pow(c, d, n) for c in ciphertext]
    print("Decrypted Ciphertext",decryption)
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return decrypted_text

def main():
    p = generate_prime(50, 100)
    q = generate_prime(50,100)

    while p == q:
        q = generate_prime(50, 100)

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = random.randint(3, phi_n - 1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n - 1)

    d = mod_inverse(e, phi_n)    
    print("Public Key (e, n):", e)
    print("Private Key (d, n):", d)
    print("p and q are", p, q)

    while True:
        print("\nMenu:")
        print("1. Encrypt and Decrypt")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            plaintext = input("Enter the Plaintext: ")
            ciphertext = encrypt(plaintext, e, n)
            print("Encoded plaintext",[ord(c) for c in plaintext])
            print("Ciphertext:", ciphertext)
            decrypted_text = decrypt(ciphertext, d, n)
            print("Decrypted Text:", decrypted_text)
        elif choice == '2':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2")

if _name_ == "_main_":
    main()
