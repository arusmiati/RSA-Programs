# Program 3 | Decryption

# Decryption Function
def decrypt(key, n, ciphertext):
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    decrypt = [str(pow(int(char), key, n)) for char in ciphertext]
    # Return the array of bytes as a string
    plain = [chr(int(char2)) for char2 in decrypt]
    return ''.join(plain)

# Main Program
if __name__ == '__main__':
    print("===========================================================================================================")
    print("======================================== RSA Decrypter ====================================================")
    print(" ")

    y = input(" - Enter encryption message with space: ").split()
    d = int(input(" - Enter private key: "))
    n = int(input(" - Enter modulo inverse: "))

    print("\n - Decrypting message with private key (",d, ",", n, ") . . .")
    dencrypted_msg = decrypt(d, n, y)
    print(" - Your message is: ", dencrypted_msg)

    print(" ")
    print("============================================ END ==========================================================")
    print("===========================================================================================================")