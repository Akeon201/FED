import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def encrypt_file(file_name):
    try:
        # Generate a random AES key
        aes_key = os.urandom(32)
        # Save the AES key to a file
        with open("key.txt", "wb") as key_file:
            key_file.write(aes_key)

        # Generate a random nonce
        nonce = os.urandom(16)

        # Read the data from the file
        with open(file_name, "rb") as file:
            data = file.read()

        # Encrypt the data with the AES key
        cipher = Cipher(algorithms.AES(aes_key), modes.GCM(nonce), default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(data) + encryptor.finalize()
        tag = encryptor.tag

        # Save the encrypted data and nonce to the file
        with open(file_name, "wb") as file:
            file.write(ciphertext + nonce)
        with open("tag.txt", "wb") as file:
            file.write(tag)
    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def decrypt_file(file_name):
    try:
        # Read the AES key from key.txt
        with open("key.txt", "rb") as key_file:
            aes_key = key_file.read()

        # Read the encrypted data, nonce, and tag from the file
        with open(file_name, "rb") as file:
            encrypted_data = file.read()

        # Split the encrypted data, nonce
        ciphertext = encrypted_data[:-16]
        nonce = encrypted_data[-16:]
        with open("tag.txt", "rb") as file:
            tag = file.read()

        # Decrypt the data with the AES key
        cipher = Cipher(algorithms.AES(aes_key), modes.GCM(nonce, tag, min_tag_length=16), default_backend())
        decryptor = cipher.decryptor()
        data = decryptor.update(ciphertext) + decryptor.finalize()

        # Write the decrypted data to the file
        with open(file_name, "wb") as file:
            file.write(data)

    except FileNotFoundError:
        print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
