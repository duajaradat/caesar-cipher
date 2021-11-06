# import nltk
# from nltk.corpus import words , names

# nltk.download('words',quiet=True)
# nltk.download('names',quiet=True)


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

def decrypt(decrypt_text : str , key :int):
    """
    decrypt function that takes in encrypted text and numeric shift which will restore the encrypted text back to its original form when correct key is supplied.
    Arguments: text as a string
    Returns : decrypted message as a string
    """   
    return encrypt(decrypt_text , -key) 