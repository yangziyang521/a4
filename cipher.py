import random
import string

def main():

  print("Welcome to the OTP cipher program.")
  print()

  # Read the given file
  with open("encrypted-message.txt") as file:
    given_entxt = file.read()
  
  # Read the given pad file
  with open ("pad.txt") as file:
    given_pad = file.read()

  # decipher the given txt file
  given_plaintxt = decipher(given_pad, given_entxt)
  print("The secret given message is:", given_plaintxt)
  print()


  # Prompt user for a length
  size = 1200
  # generate pad
  otp = generatePad(size)

  

  # encrypt: convert plaintexts to ciphertext with a pad
  ciphertext = encipher(otp, given_plaintxt)
  print("Using a one-time pad, the new cipher text is:", ciphertext)
  print()

  # decrypt
  plaintext = decipher(otp, ciphertext)
  print("After deciphering, the plain text is:", plaintext)
  

  with open("decrypted-message.txt", "w") as file:
    file.write(plaintext)

  


def generatePad(size):
  # create a string for all random uppercase letters
  allUpperCase = string.ascii_uppercase

  # Open an output file in write mode
  with open ("OTP.txt","w") as file:

    for i in range(size):

      # Use random choice function to output letters to the file
      file.write(random.choice(allUpperCase))
  
  # read the pad file
  with open ("OTP.txt") as file:
    pad = file.read()
  
  return pad


def encipher(pad, plaintext):
  
  encrypted = ""

  # create a inner index to count only for the letters.
  sequence = 0

  for i in range(len(plaintext)):

    if plaintext[i].isalnum():
      shift_ord = ord(pad[sequence])-65
      msg_ord = ord(plaintext[i])
      en_ord = shift_ord + msg_ord
      if plaintext[i].isupper():
        if en_ord > 90:
          en_ord -= 26
      else:
        if en_ord > 122:
          en_ord -= 26
      en_msg = chr(en_ord)
      encrypted += en_msg
      sequence += 1

    else:
      encrypted += plaintext[i]
      
  return encrypted
  

def decipher(pad, ciphertext):
  
  decrypted = ""
  
  # create a inner index to count only for the letters.
  sequence = 0

  for i in range(len(ciphertext)):
    
    if ciphertext[i].isalnum():
      
      shift_ord = ord(pad[sequence])-65
      msg_ord = ord(ciphertext[i])
      de_ord = msg_ord - shift_ord
      if ciphertext[i].isupper():
        if de_ord < 65:
          de_ord += 26
      else:
        if de_ord < 97:
          de_ord += 26
      de_msg = chr(de_ord)
      decrypted += de_msg
      sequence += 1
      

    else:
      decrypted += ciphertext[i]
      
  return decrypted


main()