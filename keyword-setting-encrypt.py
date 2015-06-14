#main method prompts for text to be encrypted, keyword, and setting
#then prints the encrypted text
def main():
    #gather the needed text
    text_to_encrypt = input("Please enter the text to encrypt: ").split(".")
    keyword = input("Please enter the keyword: ")
    setting = input("Please enter the setting: ")
    #some set up variables
    ciphers = []
    counter = 0
 
    #generate the first keyword alphabet then use the setting to generate
    #extra ciphers by shifting that alphabet, add them all to the ciphers list
    ciphers.append(generate_plain_alphabet(keyword, setting))
    for letter in setting:
        ciphers.append(shift_cipher(ciphers[counter], letter))
        counter += 1
 
    #encrypt the text then print it
    encrypted = (encrypt(text_to_encrypt, ciphers))
    for line in encrypted:
        print(line)
 
#generate_plain_alphabet creates the initial keyword-mixed alphabet
def generate_plain_alphabet(keyword, setting):
    #the standard english alphabet and a list for our new cipher
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    cipher = []
 
    #add unique letters of the keyword into the cipher
    for letter in keyword:
        if letter not in cipher:
            cipher.append(letter)
 
    #add in the rest of the letters of the alphabet
    for letter in alphabet:
        if letter not in cipher:
            cipher.append(letter)
 
    #pass the cipher back to the caller
    return cipher
 
#shift_cipher generates a new cipher by shifting the original
#keyword-mixed alphabet to start with the given letter
def shift_cipher(alphabet, letter):
    #a cipher list and index of the first letter
    cipher = []
    index = alphabet.index(letter)
 
    #starting at the given letter, begin adding the other letters with "wrap around"
    #this is basically like cutting a deck of cards
    for i in range(index, len(alphabet)):
        cipher.append(alphabet[i])
    for i in range(0, index):
        cipher.append(alphabet[i])
 
    #pass the cipher back to the caller
    return cipher
 
#encrypt generates the encrypted text!
#Basically... we start with a list of plaintext strings. We examine each one
#individually and so for the first we encode from our base alphabet to
#cipher one, for the second to cipher two, for the third to cipher three
#and so on for however many lines we have to encrypt. If we encrypt more lines
#than we have ciphers for we begin again at cipher 1.
def encrypt(text, ciphers):
    #a list of encrypted letters, list of encrypted strings and a counter
    enc_list = []
    encrypted = []
    counter = 1
 
    #encrypt the text into lists of characters and join them together as
    #strings to add to the final list
    for row in text:
        for letter in row:
            if letter != " ":
                enc_list.append(ciphers[counter][ciphers[0].index(letter)])
            else:
                enc_list.append(" ")
        encrypted.append("".join(enc_list))
        enc_list = []
        if counter == len(ciphers) -1:
            counter = 1
        else:
            counter += 1
 
    #pass the list of encrypted text back to the caller
    return encrypted
 
main()
