# Caesar Cipher .

alphabets = list('abcdefghijklmnopqrstuvwxyz')

option = int(input("(Press 0 for Encryption) (Press 1 for Decryption): "))

if option == 0:
    inputext = input("Enter the message you want to encrypt: ")    
    key = int(input("Enter the key you want to use: "))
elif option == 1:
    inputext = input("Enter the message you want to decrypt: ")
    key = int(input("Enter the key you want to use: "))
    key = -key
else:
    print("Invalid option.")  # if not 0 1
    exit()

inputtext_List = list(inputext.lower())  # Convert input to lowercase list

for i in range(len(inputtext_List)):
    if inputtext_List[i].isalpha():  # Only process alphabetic characters
        
        # Find the position of the current letter in alphabets
        current_pos = alphabets.index(inputtext_List[i])
        
        # Calculate the new position with the key
        new_pos = (current_pos + key) % 26
        
        # Update the letter in inputtext_List
        inputtext_List[i] = alphabets[new_pos]

result = ''.join(inputtext_List)  # Join the characters into a single string

print(f"\nYour input message was:   {inputext}")
print(f"You chose key:            {abs(key)}")

if option == 0:
    print(f"The encrypted message is: {result}")
elif option == 1:
    print(f"The decrypted message is: {result}")
