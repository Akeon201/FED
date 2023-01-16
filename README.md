# File-Encrypter-Decrypter

&nbsp;&nbsp;&nbsp;&nbsp;This program is an implementation of a simple file encryption and decryption tool using the Advanced Encryption Standard (AES) algorithm and the Galois/Counter Mode (GCM) of operation. The program starts by prompting the user to select whether they want to encrypt or decrypt a file by typing 1 or 2, respectively. The user is then prompted to enter the name of the file they want to encrypt or decrypt. Depending on the user's choice, the program will call the encrypt_file() or decrypt_file() function from the cryptoFunc module.

# Instructions

1. Make sure you have **Python** installed on your computer. You can check this by running the command **'python --version'** in your terminal or command prompt.
2. Install the python modules **os**, **cryptography** by running the command **'pip install os cryptography'** in the terminal or command prompt.
3. Open a terminal or command prompt and navigate to the directory where the python file is saved.
4. Run the command **'python main.py'**
5. The script will prompt you to type **1** for encrypt or **2** for decrypt. Depending on your choice, it will either encrypt or decrypt a file.
6. Next, the script will prompt you to give a **file name**. Input the name of the file you want to encrypt or decrypt.
7. Once the file name is entered, the script will run the corresponding encryption or decryption function. If the file exists and you have the necessary permission to access the file, the operation will be completed successfully.
8. If you get any error, make sure that the imported modules are imported correctly and make sure 'cryptoFunc.py' it is in the same directory as the script.

# Authors

Kenyon Leblanc
