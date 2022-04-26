def caeser(msg, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_message = ""
    for c in msg:
        position = alphabet.find(c)
        new_position = (position+key)%len(alphabet)
        new_character = alphabet[new_position]
        new_message += new_character
    return new_message
key = 3
while True:
    message = input('Please enter a message: ')
    if message == 'q':break
    encry_message = caeser(message, key)
    decry_message = caeser(encry_message, -key)
    print('Encrypted message: ',encry_message)
    print('Decrypted message: ',decry_message)
    