#main method prompts for keyword, setting, and encrypted text
#and prints the decrypted text
def main():
    #gather the keyword and setting
    keyword = input("Please enter the keyword:")
    setting = input("Please enter the setting:")
    counter = 0
 
    #generate the new "plain" alphabet and copy it
    #so we can generate a "new" (cipher) alphabet
    alphabets = []
    alphabets.append(build_plain_alphabet(keyword))
 
    #create the ciphered alphabet based on the setting
    for letter in setting:
        alphabets.append(setting_shift(alphabets[counter], letter))
        counter += 1
 
    #prompt for the text to decrypt and output plaintext
    text_to_decrypt = input("Please enter the text to decrypt: ").split(".")
    decrypted = (decrypt(alphabets, text_to_decrypt))
 
    for row in decrypted:
        print(row)
 
#build_plain_alphabet generates a new base alphabet from the keyword
def build_plain_alphabet(keyword):
    #start with standard english alphabet and empty list
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    new_alphabet = []
 
    #add unique letters from the keyword to the new alphabet
    for letter in keyword:
        if letter not in new_alphabet:
            new_alphabet.append(letter)
 
    #add the rest of the unused letters of the alphabet to the new one
    for letter in alphabet:
        if letter not in new_alphabet:
            new_alphabet.append(letter)
 
    #pass the new alphabet back to the caller
    return new_alphabet
 
#setting_shift shifts the base alphabet up or down
#based on the given letter of the setting (AKA substitution cipher)
def setting_shift(alphabet, letter):
    #create empty cipher and get the index of the passed letter from the alphabet
    cipher = []
    index = alphabet.index(letter)
 
    #starting at the given letter, begin adding the other letters with "wrap-around"
    #this is basically like cutting a deck of cards
    for i in range(index, len(alphabet)):
        cipher.append(alphabet[i])
    for i in range(0, index):
        cipher.append(alphabet[i])
 
    #pass the new cipher alphabet back to the caller
    return cipher
 
#decrypt generates the plaintext!
#Basically... we start with a list of encrypted strings. We examine each one
#individually and so the first we use cipher one to decrypt to the original
#mixed alphabet. The second one we use cipher two to decrypt,
#the third uses cipher 3 and so on.
def decrypt(alphabet, text):
    #create an empty list to stuff "translated" (decrypted) letters
    #and a list of decrpyted strings... and a counter (you'll see)
    trans_list = []
    decrypted = []
    counter = 1
 
    #for every row of our text go through the letters and add the
    #decrypted value to the trans_list then join them as a single
    #string and add that to the decrypted list. rinse and repeat
    for row in text:
        for letter in row:
            if letter != " ":
                trans_list.append(alphabet[0][alphabet[counter].index(letter)])
            else:
                trans_list.append(" ")
        decrypted.append("".join(trans_list))
        trans_list = []
        if counter == len(alphabet) - 1:
            counter = 1
        else:
            counter += 1
 
    #return the list of decrypted strings
    return decrypted
 
#call the main method!
main()
