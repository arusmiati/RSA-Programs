import random

#Algoritma Euclid digunakan untuk menentukan FPB
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#Euclid's extended algorithm untuk menemukan invers perkalian dari dua angka
def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi//e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y1

        x2 = x1
        x1 = x
        d = y1
        y1 = y

    if temp_phi == 1:
        return d + phi

#Mengecek apakah inputan adalah bilangan prima
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True


def generate_key_pair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    
    # n = pq
    n = p * q

    phi = (p-1) * (q-1)

    #variabel e sebagai inisiasi koprima dari e dan phi(n)
    e = random.randrange(1, phi)

    #Algoritma Euclid untuk memverifikasi bahwa e dan phi(n) adalah koprima
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    #generate  private key
    d = multiplicative_inverse(e, phi)

    # Return public and private key_pair
    # Public key = (e, n) dan private key = (d, n)
    return ((e, n), (d, n))

if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print("===============================================================================================================")
    print("============================================= RSA Create Key ==================================================")
    print(" ")

    p = int(input(" - Masukkan Angka Prima (17, 19, 23, dst): "))
    q = int(input(" - Masukkan Angka Prima yang Lainnya (Berbeda dengan yang diinput sebelumnya): "))

    print(" - Generating Public Key dan Private Key . . .")

    public, private = generate_key_pair(p, q)

    print(" - public key = ", public, " dan private key = ", private)

    print(" ")
    print("=============================================== TO BE CONTINUE ===============================================")
    print("==============================================================================================================")