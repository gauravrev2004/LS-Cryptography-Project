import hashlib

def read_file(file_name):
    try:
        with open(file_name, 'rb') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        raise ValueError(f"File '{file_name}' not found.")
    except Exception as e:
        raise ValueError(f"Error occurred while reading the file: {e}")

def verify_rsa_signature(file_content, N, signature_hex):
    try:
        # Convert the signature back to an integer
        signature = int(signature_hex, 16)

        # Calculate the hash of the file content
        hash_obj = hashlib.sha256()
        hash_obj.update(file_content)
        hash_value = hash_obj.digest()

        # Verify the signature
        decrypted_signature = pow(signature, 65537, N)
        if decrypted_signature == int.from_bytes(hash_value, byteorder='big'):
            return "accept"
        else:
            return "reject"
    except ValueError:
        raise ValueError("Invalid signature format.")
    except Exception as e:
        raise ValueError(f"Error occurred while verifying the signature: {e}")

if __name__ == "__main__":
    file_name = input("Enter the name of the text file: ")
    N = int(input("Enter the value of N: "))
    signature_hex = input("Enter the signature in hex: ")

    try:
        file_content = read_file(file_name)
        result = verify_rsa_signature(file_content, N, signature_hex)
        print(result)
    except ValueError as ve:
        print(ve)


