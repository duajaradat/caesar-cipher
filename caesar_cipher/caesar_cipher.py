
import nltk
from nltk.corpus import words , names




def encrypt(text :str,key :int):
    """
    Function to encrypt a text phrase and a numeric shift
    Arguments : text as string , key as int
    Returns : encrypted message as a string
    """
    encrypted_message = ''
    # a-z characters 
    for char in text:
        shifted_number = ord(char)+key
        if ord(char) >=97 and ord(char) <=122:
            if shifted_number > 122:
                shifted_number-=26
            if shifted_number < 97:
                shifted_number+=26  

        elif ord(char) >=65 and ord(char) <=90:
            if shifted_number > 90:
                shifted_number-=26
            if shifted_number < 65:
                shifted_number+=26 

        if (ord(char) >=65 and ord(char) <=90 ) or (ord(char) >=97 and ord(char) <=122): 
            encrypted_char=chr(shifted_number) 
        else:
            encrypted_char=char       

        encrypted_message+=encrypted_char 

    return encrypted_message

def decrypt(text_to_decrypt : str , key :int):
    """
    decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
    Arguments: text as a string
    Returns : decrypted message as a string
    """   
    return encrypt(text_to_decrypt , -key) 

def crack(text_to_decrypt : str):
    """
    crack function that will decode the cipher so that an encrypted message can be transformed into its original state WITHOUT access to the key.
    Arguments: text to decrypt as a string.
    Returns: decrypted message as a string
    """
    nltk.download('words',quiet=True)
    nltk.download('names',quiet=True)

    names_list = names.words() # first letter is uppercase
    # print(names_list) 
    words_list = words.words()  # all words in lowercase
    # print(words_list) 
    candidates =[]
    for i in range(26):
        decrypted=decrypt(text_to_decrypt ,i)
        candidates.append(decrypted)

    for candidate in candidates:
        phrase = candidate.split(' ')
   
        words_counter = 0
        for word in phrase:
            if word.lower() in words_list or word.lower() in names_list:
                words_counter+=1

        words_of_candidate=len(phrase)
        percentage = (words_counter/words_of_candidate)*100

        if percentage > 50:
            print(phrase,percentage)           
            return " ".join(phrase)

    


if __name__ == '__main__':
    crack("Te hld esp mpde zq etxpd, te hld esp hzcde zq etxpd.") 
    # pass   