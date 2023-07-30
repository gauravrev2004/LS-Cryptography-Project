import hashlib
from Crypto.Util.number import getPrime

def read_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise ValueError(f"File '{file_name}' not found.")
    except Exception as e:
        raise ValueError(f"Error occurred while reading the file: {e}")

def generate_rsa_signature(file_content):
    # Get SHA-256 hash of the file content
    hash_obj = hashlib.sha256()
    hash_obj.update(file_content)
    hash_value = hash_obj.digest()

    # Generate a random semiprime N
    while True:
        p = getPrime(2048)
        q = getPrime(2048)
        N = p * q
        if N.bit_length() == 4096:
            break

    # RSA digital signature
    e = 65537  # public exponent
    signature = pow(int.from_bytes(hash_value, byteorder='big'), pow(e,-1,(p-1)*(q-1)),N)

    return (N, e), hex(signature)[2:]

if __name__ == "__main__":
    try:
        file_name = input("Enter the name of the text file: ")
        file_content = read_file(file_name)
        keys, signature = generate_rsa_signature(file_content)

        print("\nDigital Signature:")
        print(f"Signature: {signature}")
        print(f"Public Key (N, e): {keys}")

    except ValueError as ve:
        print(ve)