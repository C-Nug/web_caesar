# Constants for ASCII values
lower_a = 97
uppper_A = 65
chrs_in_alphabet = 26

# Rotates a char through the alphabet rot places, wrapping around
# the alphabet
def rotate_char(char, rot):
    if char.islower() == True:
        rotated = chr((alpha_pos(char) + rot) % chrs_in_alphabet + lower_a)
        return rotated
    else:
        rotated = chr((alpha_pos(char) + rot) % chrs_in_alphabet + uppper_A)
        return rotated

# Assuming a letter is entered, this will return a character's
# numberical place in the alphabet, starting with a == 0
def alpha_pos(char):
    if char.islower() == True:
        return (ord(char) - lower_a)
    else:
        return (ord(char) - uppper_A)

def encrypt(message, rotate):
    encrypted = ""
    for ch in message:
        if ch.isalpha() == True:
            encrypted = encrypted + rotate_char(ch, rotate)
        else:
            encrypted = encrypted + ch
    return encrypted
