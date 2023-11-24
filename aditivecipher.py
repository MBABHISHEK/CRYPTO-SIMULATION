import string 

alphabets=list(string.ascii_lowercase)

def encryption(plain_text,key):
    cipher_text = ""
    for char in plain_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position + key) % 26
            cipher_text += alphabets[new_position]
        else:
             cipher_text += char
    print("The text after encryption is :",cipher_text)
        
def decryption(cipher_text,key):
    plain_text = ""
    for char in cipher_text:
        if char in alphabets:
            position = alphabets.index(char)
            new_position = (position - key) % 26
            plain_text += alphabets[new_position]
        else:
            plain_text += char
    print("The text after decryption is : ",plain_text)

while True:
    print("----------------------------------------------------")
    print("Enter your choice:")
    choice = input("1.encryption \n2.decryption\n")
    
    if choice == "1":
        text = input("Type your message:").lower()
        key_given = int(input("enter the key:"))
        encryption(plain_text=text,key=key_given)
    
    elif choice == "2":
        text = input("Type your message:").lower()
        key_given = int(input("enter the key:"))
        decryption(cipher_text=text,key=key_given)
    
    else:
        print("Invalid choice.....Thank you!!")
        break
